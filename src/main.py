import os
from src.get_frames import split_video_into_frames
from src.get_cam_poses import load_image_data
from src.visualize import visualize
from src.get_nearest import get_nearest_images


video_path = "sfm_project"
output_folder = "sfm_project/images"

points = [[0.5, 0.4, 0.3]] ### example

def start_sfm():
    os.system(".\COLMAP.bat automatic_reconstructor --image_path sfm_project/images --workspace_path sfm_project")
    os.system(".\COLMAP.bat model_converter --input_path sfm_project/sparse/0 --output_path sfm_project --output_type TXT")


if __name__ == "__main__":
    split_video_into_frames(video_path, output_folder)
    start_sfm()
    df = load_image_data()
    visualize(df)
    get_nearest_images(df, points)

