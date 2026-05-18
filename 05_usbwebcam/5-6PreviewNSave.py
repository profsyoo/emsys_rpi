import cv2
camera = cv2.VideoCapture(0, cv2.CAP_V4L)
# 프레임 크기를 320×240으로 하고, camera가 카메라로부터 읽어오는 주기(FPS)를
# 10으로 설정
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
camera.set(cv2.CAP_PROP_FPS, 10)

fourcc = cv2.VideoWriter_fourcc(*'DIVX') # 코덱 지정
writer = cv2.VideoWriter("video_5_6.avi", fourcc, 10, (320, 240)) # 10 fps 주기로 저장

print("Starting")
while True:
	ret, image = camera.read( )
	if ret == True:
		cv2.imshow('preview', image)
		writer.write(image)
	else:
		print("Can't capture any frame from the cam.")
	break

	# 1 밀리초 동안 ESC 키 입력을 기다린다.
	if cv2.waitKey(1) == 27: # 입력된 키가 ESC이면 while 반복문을 탈출
		break
writer.release( )
camera.release( )
cv2.destroyAllWindows( )
