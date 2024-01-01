import cv2
import os
import datetime

# Cascades
face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

# Folder path
folder_path = " " # Enter folder path where you want to save your files

def face_capture():
    cap = cv2.VideoCapture(0)
    last_capture_time = None
    capture_delay = 0  # seconds delay between captures

    try:
        while True:
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

            for (x, y, w, h) in faces:
                # Extract the region of interest (the face)
                roi_gray = frame[y:y+h, x:x+w]

                # Resize the face region to 150x150 pixels
                roi_gray_resized = cv2.resize(roi_gray, (150, 150))

                current_time = datetime.now()
                if last_capture_time is None or (current_time - last_capture_time).seconds > capture_delay:
                    # Generate a unique filename with timestamp
                    timestamp = current_time.strftime("%Y%m%d_%H%M%S")
                    filename = f"face_image_{timestamp}.jpg"
                    image_path = os.path.join(folder_path, filename)

                    # Save the resized image
                    cv2.imwrite(image_path, roi_gray_resized)
                    print(f"Image saved successfully as {filename}")
                    last_capture_time = current_time

            cv2.imshow('test', frame)
            
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

face_capture()