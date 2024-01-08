import cv2
import os
import openai    
from openai import OpenAI
import mysql.connector
from mysql.connector import Error
import tensorflow as tf
from keras.models import Sequential, load_model
import pickle
from datetime import datetime
from machine_learning import machine_learning
from machine_learning import analyze
import time

# Cascades
face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

# Folder path
folder_path = "" # Enter your folder path

# Using GPT API to create HTML page that has individual information
def gpt_api(gpt_info, name, filename):
    print("Building Personal HTML page....")
    main_prompt = f"Create an HTML page that displays information about {name}. Include the following details: {gpt_info}. Also include the photo {filename} into the website. Format it neatly with headers and paragraphs and use CSS to style it and make it look professional and appealing"
    try:
        client = OpenAI(api_key=" ") # Enter your GPT API key
        # Generate HTML Content
        response = client.chat.completions.create(
            model = "gpt-4-1106-preview",
            messages=[
                {
                    "role": "system",
                    "content": "You will be provided instructions on how to build an HTML page of invidiuals information"
                },
                {
                    "role": "user",
                    "content": main_prompt
                }
            ],
            #temperature=0.7,
            stop="</html>"
        )
        
        # Extract and print HTML content
        html_content = response.choices[0].message.content

        # Finding certain word so it only writes the relevant information
        word_to_find = "<!DOCTYPE html>"
        index = html_content.find(word_to_find)
        if index != -1:
            content_to_write = html_content[index:]
            with open("test.html", "w") as html_file:
                html_file.write(content_to_write)
        else:
            print("Word not found")
        #print(content_to_write)
    except Exception as e:
        print(f"An error occurred: {e}")
    
    # Starting up the file automatically
    try:
        os.startfile(" ") # Starts the file of wherever your test.html file is
    except Exception as e:
        print(f"An error occurred: {e}")

def add_user():
    import autopic
    import adding_users
    full_name_info = input("Enter your full name: ")
    ethnicity_info = input("Enter your ethnicity: ")
    gender_info = input("Enter your gender: ")
    address_info = input("Enter city you live in: ")
    employment_info = input("Enter employment info: ")
    school_info = input("Enter school you attend: ")
    major_info = input("Enter major you're currently pursuing: ")
    print("WE WILL NOW BE TAKING PHOTOS OF YOUR FACE")
    time.sleep(1)
    autopic.face_capture(full_name_info)
    adding_users.add_to_sql_database(full_name_info,ethnicity_info,gender_info,address_info,employment_info,school_info,major_info)
    face_capture()
    
# Connecting to SQL database
def sql_connect():
    try:
        # Connect to the MySQL database
        db = mysql.connector.connect(
            host="",                    # Enter your database
            user="",                    # Enter your MySQL username
            passwd="",                  # Enter your password to your database
            database=""                 # Enter the database you want to access
        )
        if db.is_connected():
            print('Successfully connected to the database.')
    except Error as e:
        print(f"The error '{e}' occurred")
        exit()

    db.close()

# Connecting to database and quering information for given target
def access_database(name, filename):
    try:
        # Connect to the MySQL database
        db = mysql.connector.connect(
            host="",                    # Enter your database
            user="",                    # Enter your MySQL username
            passwd="",                  # Enter your password to your database
            database=""                 # Enter the database you want to access
        )
        if db.is_connected():
            print(f'Querying {name}.......')
        cursor = db.cursor()

        # Function to fetch and print information
        def fetch_and_print_info(query, information):
            chat_gpt_info = []
            cursor.execute(query)
            results = cursor.fetchall()
            for row in results:
                if name in row:
                    information = f"{information}{row[3]}"
                    chat_gpt_info.append(information)
            return chat_gpt_info
            
        # Information that's gonna be sent to GPT 4 API
        gpt_info = []

        # Getting Gender Information
        gender = "Gender Information: "
        gpt_info.extend(fetch_and_print_info("SELECT * FROM users JOIN gender_info ON users.id = gender_info.users_id", gender))

        # Getting Ethnicity Information
        ethnicity = "Ethnicity Information: "
        gpt_info.extend(fetch_and_print_info("SELECT * FROM users JOIN ethnicity_info ON users.id = ethnicity_info.users_id", ethnicity))

        # Getting Address Information
        address = "Address Information: "
        gpt_info.extend(fetch_and_print_info("SELECT * FROM users JOIN address_info ON users.id = address_info.users_id", address))
    
        # Getting Occupation Information
        occupation = "Occupation Information: "
        gpt_info.extend(fetch_and_print_info("SELECT * FROM users JOIN occupation_info ON users.id = occupation_info.users_id", occupation))

        # Getting School Information
        school = "School Information: "
        gpt_info.extend(fetch_and_print_info("SELECT * FROM users JOIN school_info ON users.id = school_info.users_id", school))

        #print(gpt_info)
        #print(name)
        gpt_api(gpt_info, name, filename)

    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        if db.is_connected():
            cursor.close()
            db.close()
            print("MySQL connection is closed")

def face_capture():
    cap = cv2.VideoCapture(0)
    last_capture_time = None
    capture_delay = 0  # seconds delay between captures
    text = 'Analyzing....'
    text_2 = ''
    
    # Load model and LabelBinarizer here
    model = load_model('my_model.h5')
    with open('lb.pickle', 'rb') as file:
        lb = pickle.load(file)

    try:
        while True:
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
            x, y, w, h = 0, 0, 0, 0  

            for (x, y, w, h) in faces:
                # Extract the region of interest (the face)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                roi_gray = frame[y:y+h, x:x+w]

                # Resize the face region to 150x150 pixels
                roi_gray_resized = cv2.resize(roi_gray, (150, 150))

                # Check if enough time has passed since the last capture
                if cv2.waitKey(1) & 0xFF == ord('s'):
                    current_time = datetime.now()
                    if last_capture_time is None or (current_time - last_capture_time).seconds > capture_delay:
                        # Generate a unique filename with timestamp
                        timestamp = current_time.strftime("%Y%m%d_%H%M%S")
                        filename = f"face_image_{timestamp}.jpg"
                        current_path = " " # Wherever your current_path is
                        image_path = os.path.join(current_path, filename)
                        

                        # Save the resized image in saved_faces folder
                        cv2.imwrite(image_path, roi_gray_resized)
                        print(f"Image saved successfully as {filename}")
                        last_capture_time = current_time

                        # Sending the photo to the machine learning to determine who the person is
                        person_identified, individual, classes = analyze(image_path, model, lb)
                        person_identified_text = f'{person_identified}...'

                        # Font for person_identified
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        fontScale = 1
                        color = (0, 255, 0)  # Green color in BGR
                        thickness = 2

                        # Put the text on the frame
                        cv2.putText(frame, person_identified_text, (x, y - 10), font, fontScale, color, thickness)
                        text = person_identified_text

                        # Accessing and Querying SQL database
                        if individual in classes:
                            print("Person Identified:", person_identified)
                            access_database(individual, filename)
                        else:
                            print(individual) # This will print that the user is not recognized in the database
                            add_user() 
            
            # Font for person_identified
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (0, 255, 0)  # Green color in BGR
            thickness = 2

            cv2.putText(frame, text, (x, y - 10), font, fontScale, color, thickness)

            # Welcome text
            welcome_text = f'Welcome {text_2}'
            # Get frame dimensions
            frame_height, frame_width = frame.shape[:2]

            # Get the text size
            text_size = cv2.getTextSize(welcome_text, font, fontScale, thickness)[0]

            # Calculate text position (top right)
            text_x = frame_width - text_size[0] - 10  # 10 pixels margin from right
            text_y = text_size[1] + 10  # 10 pixels margin from top

            cv2.putText(frame, welcome_text, (text_x, text_y), font, fontScale, color, thickness)
                        
            cv2.imshow('Face Secure Authentication', frame)
            
            # Breaking the capture
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Exiting system")
                break
    except KeyboardInterrupt:
        print("Interrupted by user, shutting down.")
    finally:
        # Release the capture and close any open windows
        cap.release()
        cv2.destroyAllWindows()

if sql_connect() == None:
    face_capture()
