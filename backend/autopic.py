import cv2
import os
from datetime import datetime

# Cascades
face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

def face_capture(full_name_info):
    folder_path = f"enter\\your\\folder\\path\\{full_name_info}"
    os.makedirs(folder_path)
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Set a lower resolution for faster processing
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    photo_count = 1000  # Amount of images needed

    try:
        while photo_count > 0:
            ret, frame = cap.read()
            if not ret:
                continue

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

            for (x, y, w, h) in faces:
                roi_gray_resized = cv2.resize(gray[y:y+h, x:x+w], (150, 150))  # Resize the face region

                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"face_image_{timestamp}{photo_count}.jpg"
                image_path = os.path.join(folder_path, filename)

                cv2.imwrite(image_path, roi_gray_resized)  # Save the resized image
                print(f"Image saved successfully as {filename}")

                photo_count -= 1
                if photo_count == 0:
                    break

            if photo_count == 0:
                break

            if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit early
                break

    except KeyboardInterrupt:
        print("Interrupted by user, shutting down.")
    finally:
        cap.release()
        cv2.destroyAllWindows()
        return(full_name_info)
