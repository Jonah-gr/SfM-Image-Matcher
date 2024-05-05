import cv2
import os
from src.config import SFM_PATH


def split_video_into_frames():
    output_folder = os.path.join(f"{SFM_PATH}/images")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(f"{SFM_PATH}/video.mp4")
    
    frame_count = 0
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            break
        
        frame_path = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_path, frame)
        
        frame_count += 1
    
    cap.release()


if __name__ == "__main__":
    split_video_into_frames()
