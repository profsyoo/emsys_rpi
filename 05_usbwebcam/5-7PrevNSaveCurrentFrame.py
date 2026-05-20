import cv2

# Create camera object (V4L backend)
camera = cv2.VideoCapture(0, cv2.CAP_V4L)

# Set camera buffer size to 10
camera.set(cv2.CAP_PROP_BUFFERSIZE, 10)

def take_picture():
    """
    Capture a single frame after clearing the camera buffer.
    """
    # Read current buffer size
    size = int(camera.get(cv2.CAP_PROP_BUFFERSIZE))

    # Discard all frames currently stored in the buffer
    while size > 0:
        camera.grab()   # camera.read() can also be used
        size -= 1

    # Read the most recent frame from the buffer
    ret, frame = camera.read()
    return frame if ret else None


count = 0
print("OpenCV loaded successfully")
print("Ready for key input")

try:
    # Capture one frame first
    frame = take_picture()

    while True:
        # cv2.waitKey() works only if a window is created by imshow()
        if frame is not None:
            cv2.imshow("picture", frame)

        # If ESC key is pressed, exit the loop
        # Otherwise, capture an image and save it as a file
        key = cv2.waitKey(0)  # 0 means wait indefinitely for a key input
        if key == 27:         # ESC key
            break
        else:
            frame = take_picture()  # Capture the current frame
            count += 1
            file_name = f"image_5_7{count}.jpg"
            cv2.imwrite(file_name, frame)  # Save the frame as a JPG file
            print(f"Saved: {file_name}")

except KeyboardInterrupt:
    # Handle Ctrl+C interruption
    print("\nProgram interrupted by user")

except Exception as e:
    # Handle unexpected errors
    print("An error occurred:", e)

finally:
    # Release camera and destroy all OpenCV windows
    camera.release()
    cv2.destroyAllWindows()
    print("Camera released and windows closed")
