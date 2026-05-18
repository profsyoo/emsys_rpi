import cv2
camera = cv2.VideoCapture(0, cv2.CAP_V4L)
try
  while True:
	  ret, image = camera.read( ) # Read a frame from the cam.
	  if ret == True:
		  cv2.imshow('preview', image) # show the frame in the preview window
	  else:
		  print("Can't capture any frame from the cam..")
		  break
	  # wait for 'ESC' key for 1 msec.
	  if cv2.waitKey(1) == 27: # if the key is 'ESC, break from while loop
		  break
except KeyboardInterrupt:
  pass
	
finally:	
  camera.release( )
  cv2.destroyAllWindows( )
