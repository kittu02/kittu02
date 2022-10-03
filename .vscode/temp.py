#import the opencv library
import cv2

vid = cv2.VideoCapture(0)
#any name at vid variable
while(True):
  # it will capture the video frame by frame
  ret, frame = vid.read()
  # display the resulting frame
  cv2.imshow('frame',frame)
  # it will wait every one second for q ascii value
  if cv2.waitKy(1) & 0xFF == ord('q'):
    break
#after the loop release the cap object
vid.release()
#destroy all windows after ending program
cv2.destroyAllWindows()
