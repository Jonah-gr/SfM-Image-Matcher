import os
from src.config import SFM_PATH
from src.get_frames import split_video_into_frames
from src.get_cam_poses import load_image_data
from src.visualize import visualize
from src.get_nearest import get_nearest_images


def start_sfm():
    os.system(f".\COLMAP.bat automatic_reconstructor --image_path {SFM_PATH}/images --workspace_path {SFM_PATH}")
    os.system(f".\COLMAP.bat model_converter --input_path {SFM_PATH}/sparse/0 --output_path {SFM_PATH} --output_type TXT")


if __name__ == "__main__":
    split_video_into_frames()
    start_sfm()
    df = load_image_data()
    visualize(df)
    get_nearest_images(df)

