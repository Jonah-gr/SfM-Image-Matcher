import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
from src.config import SFM_PATH, objective_points

def find_nearest_camera(df, point):
    distances = cdist(df['CAMERA_POSITION'].tolist(), [point])
    nearest_index = distances.argmin()
    return (df.iloc[nearest_index], distances[nearest_index])

def get_nearest_images(df, show=True):
    for point in objective_points:
        nearest_camera = find_nearest_camera(df, point)

        if show:
            perspective_image_name = nearest_camera[0].NAME
            perspective_image = plt.imread(f"{SFM_PATH}/images/{perspective_image_name}")
            plt.imshow(perspective_image)
            plt.axis('off')
            plt.title('Perspective Image')
            plt.show()
        print(nearest_camera)