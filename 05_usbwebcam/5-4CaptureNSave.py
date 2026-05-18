#may take some time
import cv2
camera = cv2.VideoCapture(0, cv2.CAP_V4L)
ret, image = camera.read( )
if ret == True:
	# Save the captured image via OpenCV function, imwrite
	cv2.imwrite('image_5_4.jpg', image)
else:
	print("Can't capture any frame via. the camera")
camera.release( )
