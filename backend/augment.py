### Code meant for augmenting the images

import cv2
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array, load_img
import os
import random

def custom_image_processing(image, prob=0.3, clip_limit=2.0, tile_grid_size=(8, 8)):

    # Apply contrast enhancement with a certain probability
    if random.random() < prob:
        # Ensure the image is in the correct color format
        if image.dtype != np.uint8:
            image = image.astype(np.uint8)

        # Convert to YUV color space
        img_yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)

        # Apply CLAHE to the luminance channel
        clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
        img_yuv[:,:,0] = clahe.apply(img_yuv[:,:,0])

        # Convert back to RGB color space
        image = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
    return image

def augment_images(folder):
    folder_path = f"\enter\\your\\folder\\path\\{folder}"

    datagen = ImageDataGenerator(
        rotation_range=20,
        width_shift_range=0.1,    
        height_shift_range=0.1,   
        shear_range=0.2,
        zoom_range=[0.8, 1.2],
        horizontal_flip=True,
        brightness_range=[0.5, 1.2],
        fill_mode='nearest'
    )

    files_and_dirs = os.listdir(folder_path)
    for filename in files_and_dirs:
        file_path = os.path.join(folder_path, filename)
        img = load_img(file_path)  # Load image
        image = img_to_array(img)  # Convert to numpy array
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # Convert to BGR format

        # Apply custom image processing
        processed_image = custom_image_processing(image)

        processed_image = processed_image.reshape((1,) + processed_image.shape)  # Reshape image

        # Generate and save augmented images
        for batch in datagen.flow(processed_image, batch_size=1, save_to_dir=folder_path, save_prefix='aug', save_format='jpg'):
            break  # Stop after generating one batch of augmented images per image
