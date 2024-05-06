import os
import shutil
import enlighten
import pycolmap
from pycolmap import logging
from pathlib import Path
from src.config import SFM_PATH, CUDA
from src.get_frames import split_video_into_frames
from src.get_cam_poses import load_image_data
from src.visualize import visualize
from src.get_nearest import get_nearest_images


def start_sfm_cuda():
    os.system(f".\COLMAP.bat automatic_reconstructor --image_path {SFM_PATH}/images --workspace_path {SFM_PATH}")
    os.system(f".\COLMAP.bat model_converter --input_path {SFM_PATH}/sparse/0 --output_path {SFM_PATH} --output_type TXT")


def incremental_mapping_with_pbar(database_path, image_path, sfm_path):
    num_images = pycolmap.Database(database_path).num_images
    with enlighten.Manager() as manager:
        with manager.counter(
            total=num_images, desc="Images registered:"
        ) as pbar:
            pbar.update(0, force=True)
            reconstructions = pycolmap.incremental_mapping(
                database_path,
                image_path,
                sfm_path,
                initial_image_pair_callback=lambda: pbar.update(2),
                next_image_callback=lambda: pbar.update(1),
            )
    return reconstructions


def start_sfm():
    output_path = Path(f"{SFM_PATH}/")
    image_path = output_path / "images"
    database_path = output_path / "database.db"
    sfm_path = output_path / "sparse"

    output_path.mkdir(exist_ok=True)
    logging.set_log_destination(logging.INFO, output_path / "INFO.log.")

    if database_path.exists():
        database_path.unlink()
    pycolmap.extract_features(database_path, image_path)
    pycolmap.match_exhaustive(database_path)

    if sfm_path.exists():
        shutil.rmtree(sfm_path)
    sfm_path.mkdir(exist_ok=True)

    recs = incremental_mapping_with_pbar(database_path, image_path, sfm_path)
    for idx, rec in recs.items():
        logging.info(f"#{idx} {rec.summary()}")

    
def export_model():
    reconstruction = pycolmap.Reconstruction(Path(f"{SFM_PATH}/") / "sparse/0")
    reconstruction.write_text(Path(f"{SFM_PATH}/"))



if __name__ == "__main__":
    split_video_into_frames()

    if CUDA:
        start_sfm_cuda()
    else:
        start_sfm()
        export_model()

    df = load_image_data()
    visualize(df)
    get_nearest_images(df, show=False)