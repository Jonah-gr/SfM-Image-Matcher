import os
import pandas as pd
import numpy as np
from src.config import SFM_PATH



def quaternion_to_rotation_matrix(qw, qx, qy, qz):
    R = np.array([
        [1 - 2*qy**2 - 2*qz**2, 2*qx*qy - 2*qz*qw, 2*qx*qz + 2*qy*qw],
        [2*qx*qy + 2*qz*qw, 1 - 2*qx**2 - 2*qz**2, 2*qy*qz - 2*qx*qw],
        [2*qx*qz - 2*qy*qw, 2*qy*qz + 2*qx*qw, 1 - 2*qx**2 - 2*qy**2]
    ])

    return R


def add_camera_position_column(df):
    # camera position = -R^t * T
    rotation_matrices = np.array([quaternion_to_rotation_matrix(float(row['QW']), float(row['QX']), float(row['QY']), float(row['QZ'])) for _, row in df.iterrows()])
    inverse_rotation_matrices = np.transpose(rotation_matrices, axes=(0, 2, 1))
    translation_vectors = df[['TX', 'TY', 'TZ']].astype(float).values
    camera_positions = np.matmul(inverse_rotation_matrices, translation_vectors.reshape(-1, 3, 1)).squeeze()
    df['CAMERA_POSITION'] = [position.tolist() for position in camera_positions]


def load_image_data():
    with open(os.path.join(SFM_PATH, 'images.txt'), 'r') as file:
        lines = file.readlines()

    data = {
        'IMAGE_ID': [],
        'QW': [],
        'QX': [],
        'QY': [],
        'QZ': [],
        'TX': [],
        'TY': [],
        'TZ': [],
        'CAMERA_ID': [],
        'NAME': []
    }

    for line in lines:
        if "jpg" in line:
            line_data = line.strip().split(' ')
            image_id, qw, qx, qy, qz, tx, ty, tz, camera_id, name = line_data
            data['IMAGE_ID'].append(image_id)
            data['QW'].append(qw)
            data['QX'].append(qx)
            data['QY'].append(qy)
            data['QZ'].append(qz)
            data['TX'].append(tx)
            data['TY'].append(ty)
            data['TZ'].append(tz)
            data['CAMERA_ID'].append(camera_id)
            data['NAME'].append(name)

    df = pd.DataFrame(data)
    add_camera_position_column(df)
    return df

