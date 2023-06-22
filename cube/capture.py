import cv2

def from_file(path):
    # Load the Rubik's Cube image
    image = cv2.imread(path)

    # Preprocess the image (e.g., resize, crop, enhance, etc.)
    # Here's an example of resizing the image to a specific width and height
    width, height = 640, 480
    resized_image = cv2.resize(image, (width, height))

    # Perform any additional preprocessing steps as needed

    # Display the preprocessed image
    cv2.imshow('Preprocessed Image', resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def from_stream():
    # Create a video capture object
    video_capture = cv2.VideoCapture(0)  # 0 represents the default camera

    while True:
        # Read a frame from the video stream
        ret, frame = video_capture.read()

        # Display the frame
        cv2.imshow('Video Stream', frame)

        # Check for key press to capture the frame
        key = cv2.waitKey(1)
        if key == ord('c'):  # Press 'c' key to capture the frame
            # Preprocess the captured frame (e.g., resize, crop, enhance, etc.)
            # Here's an example of resizing the image to a specific width and height
            width, height = 640, 480
            resized_image = cv2.resize(frame, (width, height))

            # Perform any additional preprocessing steps as needed

            # Display the preprocessed image
            cv2.imshow('Preprocessed Image', resized_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            break

        # Check for key press to exit the program
        if key == ord('q'):  # Press 'q' key to quit
            break

    # Release the video capture object and close windows
    video_capture.release()
    cv2.destroyAllWindows()

    
if __name__=="__main__":
    from_stream()