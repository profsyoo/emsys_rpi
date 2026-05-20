import cv2
from datetime import datetime          # ✅ [추가된 라인]

camera = cv2.VideoCapture(0, cv2.CAP_V4L)

camera.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
camera.set(cv2.CAP_PROP_FPS, 10)

# ✅ [추가된 라인] 녹화 시작 시간 저장
start_time = datetime.now()
start_str = start_time.strftime("%Y%m%d_%H%M%S")

fourcc = cv2.VideoWriter_fourcc(*'DIVX')  # 코덱 지정

# ✅ [변경된 라인]
# 기존: writer = cv2.VideoWriter("video_5_6.avi", fourcc, 10, (320, 240))
temp_filename = "temp.avi"
writer = cv2.VideoWriter(temp_filename, fourcc, 10, (320, 240))

print("Starting")

try:
    while True:
        ret, image = camera.read()
        if ret == True:
            cv2.imshow('preview', image)
            writer.write(image)
        else:
            print("Can't capture any frame from the cam.")
            break

        if cv2.waitKey(1) == 27:  # ESC
            break

except KeyboardInterrupt:
    pass

finally:
    # ✅ [추가된 라인] 녹화 종료 시간 저장
    end_time = datetime.now()
    end_str = end_time.strftime("%H%M%S")

    writer.release()
    camera.release()
    cv2.destroyAllWindows()

    # ✅ [추가된 라인] 시작~종료 시간 포함한 최종 파일명 생성
    final_filename = f"video_{start_str}_to_{end_str}.avi"

    import os                          # ✅ [추가된 라인]
    os.rename(temp_filename, final_filename)

    print("Saved video:", final_filename)
