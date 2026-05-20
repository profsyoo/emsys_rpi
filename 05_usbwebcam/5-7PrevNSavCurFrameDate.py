import cv2
from datetime import datetime      # ✅ [추가된 라인]

# Create camera object (V4L backend)
camera = cv2.VideoCapture(0, cv2.CAP_V4L)

# Set camera buffer size to 10
camera.set(cv2.CAP_PROP_BUFFERSIZE, 10)

def take_picture():
    """
    Capture a single frame after clearing the camera buffer.
    """
    size = int(camera.get(cv2.CAP_PROP_BUFFERSIZE))

    # Discard all frames currently stored in the buffer
    while size > 0:
        camera.grab()
        size -= 1

    ret, frame = camera.read()
    return frame if ret else None


count = 0
print("OpenCV loaded successfully")
print("Ready for key input")

try:
    frame = take_picture()

    while True:
        if frame is not None:
            cv2.imshow("picture", frame)

        key = cv2.waitKey(0)
        if key == 27:   # ESC
            break
        else:
            frame = take_picture()
            count += 1

            # ✅ [추가된 라인] 현재 시간 생성
            time_str = datetime.now().strftime("%Y%m%d_%H%M%S")

            # ✅ [변경된 라인]
            # 기존: file_name = f"image_5_7{count}.jpg"
            file_name = f"image_{time_str}_{count}.jpg"

            cv2.imwrite(file_name, frame)
            print(f"Saved: {file_name}")

except KeyboardInterrupt:
    print("\nProgram interrupted by user")

except Exception as e:
    print("An error occurred:", e)

finally:
    camera.release()
    cv2.destroyAllWindows()
    print("Camera released and windows closed")
