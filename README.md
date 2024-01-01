# Secure Facial Recognition System

## PLEASE NOTE THIS IS STILL A WIP PROJECT!

## Description
This project, titled "Secure Facial Recognition System," integrates advanced technologies such as OpenCV, TensorFlow, and the OpenAI GPT API to create a comprehensive facial recognition and information retrieval system. The system is capable of identifying individuals from a dataset of facial images, querying a MySQL database for their information, and then dynamically generating a personalized HTML page with this information.

## Features
- **Facial Recognition**: Utilizes OpenCV to detect and recognize faces from live camera feeds or images.
- **Information Retrieval**: Connects to a MySQL database to fetch personal details associated with the recognized individual.
- **Dynamic Web Page Generation**: Employs the GPT API to generate a neatly formatted HTML page containing the individual's information, including their photo.
- **Machine Learning Model**: A custom TensorFlow model trained on a dataset of facial images to improve recognition accuracy.

## How It Works
1. **Face Detection**: The system first captures images from a camera feed. Using OpenCV's `haarcascade_frontalface_alt2.xml`, it detects faces in these images.
2. **Face Recognition**: The detected faces are then processed through a TensorFlow-based neural network to identify the individual.
3. **Database Querying**: Upon successful identification, the system queries a MySQL database to retrieve associated personal information.
4. **HTML Page Generation**: The GPT API is used to create an HTML page displaying the individual's information and photo in a user-friendly format.
5. **Result Display**: This HTML page is then automatically opened for viewing.

## Planned Features
- **Manual User Entry**: Implementing a feature to manually enter new users into the system. This will allow for adding individuals who are not already in the database.
- **Database Integration**: Enhancing the system to automatically update and add new entries to the MySQL database. This integration will ensure that the database remains current and comprehensive.
- **User Interface for Data Entry**: Developing a user-friendly interface for entering and managing user data, making it easier to add or update information without directly interacting with the database.

## Setup and Usage
1. **Dependencies**: Ensure you have Python, OpenCV, TensorFlow, Keras, and MySQL installed.
2. **Database Setup**: Create a MySQL database with tables for users and their information.
3. **Model Training**: Train the TensorFlow model with your dataset of facial images.
4. **API Keys**: Set up your OpenAI GPT API key.
5. **Running the System**: Start the facial recognition by running the script. Once a face is recognized and matched, the system will fetch data and generate an HTML page.

## Note
- You have to set up your own MySQL database. You can make it any way you want however, you have to edit the code so it queries everything properly.
- The `folder_paths` in `machine_learning.py` should be set to the directory containing your dataset of facial images.
- Modify `analyze()` function in `machine_learning.py` to match the number of people in your dataset.
- Always keep your OpenAI GPT API key secure and confidential.

## Contributions
This project is open for contributions and improvements. Feel free to fork the repository, make changes, and submit a pull request.

---

This project demonstrates a practical application of facial recognition, database management, and dynamic web content generation using cutting-edge technologies. It's a perfect example of how AI can be integrated into real-world applications.
