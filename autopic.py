import cv2
import os
from datetime import datetime

# Cascades
face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

def face_capture(full_name_info):
    cap = cv2.VideoCapture(0)
    last_capture_time = None
    capture_delay = 0  # seconds delay between captures
    photo_count = 200 # Amount of images needed
    folder_path = f"enter\\your\\folder\\path\\{full_name_info}"
    os.makedirs(folder_path)
    
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
                    photo_count -= 1
                    
                    # Text 
                    text = str(photo_count)
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    fontScale = 1
                    color = (0, 255, 0)  # Green color in BGR
                    thickness = 2

                    # Get frame dimensions
                    frame_height, frame_width = frame.shape[:2]

                    # Get the text size
                    text_size = cv2.getTextSize(text, font, fontScale, thickness)[0]

                    # Calculate text position (top right)
                    text_x = frame_width - text_size[0] - 10  # 10 pixels margin from right
                    text_y = text_size[1] + 10  # 10 pixels margin from top

                    # Generate a unique filename with timestamp
                    timestamp = current_time.strftime("%Y%m%d_%H%M%S")
                    filename = f"face_image_{timestamp}.jpg"
                    image_path = os.path.join(folder_path, filename)

                    # Save the resized image
                    cv2.imwrite(image_path, roi_gray_resized)
                    print(f"Image saved successfully as {filename}")
                    last_capture_time = current_time

            # Put the text on the frame at the calculated position
            cv2.putText(frame, text, (text_x, text_y), font, fontScale, color, thickness)

            cv2.imshow('Autopic', frame)
            
            # Breaking the capture
            if cv2.waitKey(1) & 0xFF == ord('l'):
                print("Exiting system")
                break
    except KeyboardInterrupt:
        print("Interrupted by user, shutting down.")
    finally:
        # Release the capture and close any open windows
        cap.release()
        cv2.destroyAllWindows()
        return(full_name_info)
