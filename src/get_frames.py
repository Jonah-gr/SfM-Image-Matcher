import cv2
import os

def split_video_into_frames(video_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)
    
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
    video_path = "sfm_project"
    output_folder = "sfm_project/images"
    split_video_into_frames(video_path, output_folder)
