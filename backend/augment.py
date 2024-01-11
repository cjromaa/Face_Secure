### Code meant for creating diversity within images

from keras.preprocessing.image import ImageDataGenerator
from keras.utils import array_to_img, img_to_array, load_img
import os

def augment_images(folder_name):
    folder_path = f"enter\\your\\folder\\path\\{folder_name}"
    datagen = ImageDataGenerator(
        rotation_range = 40,
        shear_range = 0.2,
        zoom_range = 0.2,
        horizontal_flip = True,
        brightness_range = (0.5,1.5)
    )

    files_and_dirs = os.listdir(folder_path)
    files = []
    for images in files_and_dirs:
        file = os.path.join(folder_path, images)
        files.append(file)
    #print(files)

    for x in files:
        img = load_img(x)
        image = img_to_array(img)
        image = image.reshape((1,) + image.shape)
        for batch in datagen.flow(image, batch_size = 1, save_to_dir=folder_path, save_prefix = 'aug', save_format = 'jpg'):
            break
