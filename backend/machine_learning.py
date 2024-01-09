import cv2
import os
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
import tensorflow as tf
from keras import layers
from keras import models
from keras.models import Sequential, load_model
from keras.layers import Dense
from keras.optimizers import SGD
import numpy as np
import pickle
#import main

# Cascades
face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

# List of folder paths
folder_paths = [
    " "
    # Enter required folder paths of faces you want to train
]

# Machine Learning Section
def machine_learning():
    # These image paths are used for testing and seeing how accurate the machine learning is
    image_path = ''
    image_path2 = ''
    image_path3 = ''
    image_path4 = ''
    image_path5 = ''
    image_path6 = ''
    image_path7 = ''

    # Test images
    data = []
    labels = []
    for folder_path in folder_paths:
        for filename in os.listdir(folder_path):
            imagepath = os.path.join(folder_path, filename)
            image = cv2.imread(imagepath)
            image = cv2.resize(image, (32, 32))
            #image = image.flatten()
            data.append(image)

            # Extracting the class label from the image path and updating the labels list
            label = imagepath.split(os.path.sep) [-2]
            labels.append(label)
    print(data) 
    print(labels)

    # Scale the raw pixel intensities to the range [0, 1]
    data = np.array(data, dtype="float") / 255.0
    labels = np.array(labels)
    print(data)
    print(labels)  

    x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
    # convert the labels from integers to vectors 
    lb = LabelBinarizer()
    y_train = lb.fit_transform(y_train)
    y_test = lb.transform(y_test)

    # Implementing the CNN Architecure
    # Creating the Convolutional Base
    model = models.Sequential()
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))

    # Add Dense Layers on Top
    model.add(layers.Flatten())
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(8, activation='softmax')) # Match the number with the number of classes (amount of folders training)

    # Learning Rate
    INIT_LR = 0.01
    EPOCHS = 30

    # Compiling the model
    print("[INFO] training network...")
    opt = SGD(lr=INIT_LR)
    model.compile(loss="categorical_crossentropy", optimizer=opt, metrics=["accuracy"])
    H = model.fit(x=x_train, y=y_train, validation_data=(x_test, y_test),
	epochs=EPOCHS, batch_size=32)

    # Save the model and label binarizer
    model.save('my_model.h5')
    with open('lb.pickle', 'wb') as file:
        pickle.dump(lb, file)

    # Load the model for prediction
    model = load_model('my_model.h5')

    # Process the image for prediction
    img = cv2.imread(image_path7)
    img = cv2.resize(img, (32, 32))
    img = np.array([img], dtype="float") / 255.0


    # Make a prediction
    predictions = model.predict(img)
    print(predictions)
    i = predictions.argmax(axis=1) [0]
    print(i)
    real_label = lb.classes_[i]
    print("Classes:", lb.classes_)

    text = "{}: {:.2f}%".format(real_label, predictions[0][i] * 100)

    # Determining if the face meets the proper criteria of 80% match
    failed = "Does not meet criteria, press [S] to try again"
        
    if predictions[0][i] * 100 < 70:
        print(text)
        print(failed)
    else:
        print(text)
        #cv2.putText(unedited_img, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
	    #(0, 0, 255), 2)
        #cv2.imshow("Image", unedited_img)
        #cv2.waitKey(0)
    return model, lb, x_train, x_test, y_train, y_test, data

# section is used for my main.py code to access
def analyze(filename, model, lb):
    # Load the model for prediction
    c = 0 
    # Runs the picture 3x to confirm that it's the right person
    while c < 3:
        model = load_model('my_model.h5')

        # Process the image for prediction
        img = cv2.imread(filename)
        img = cv2.resize(img, (32, 32))
        img = np.array([img], dtype="float") / 255.0
            
        # Make a prediction
        predictions = model.predict(img)
        i = predictions.argmax(axis=1) [0]
        real_label = lb.classes_[i]

        text = "{}: {:.2f}%".format(real_label, predictions[0][i] * 100)

        # Determining if the face meets the proper criteria of 80% match
        failed = "Does not meet criteria, press [S] to try again"

        if predictions[0][i] * 100 < 70:
            return text, failed, lb.classes_
        return text, face, lb.classes_

machine_learning()
