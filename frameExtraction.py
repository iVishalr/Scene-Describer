import cv2
import os
import math
import sys
file_path = sys.argv[1]   
print(file_path)                               
vidcap= cv2.VideoCapture(file_path)  
try:
    if not os.path.exists('../data'): 
        os.makedirs('../data')
except OSError:
    print ('Error: Creating directory of data')
print("Extracting Frames")
fps = vidcap.get(cv2.CAP_PROP_FPS)
count = 0
success = True
i=0
while success:
  success,frame = vidcap.read()
  count+=1
  if i%150==0:       
    timestamp = math.floor(count/fps) 
    hours = 0
    minutes = 0
    seconds = 0
    if timestamp:
      seconds = timestamp % 60
      timestamp = timestamp/60
      minutes = timestamp % 60
      timestamp = timestamp/60
      hours = timestamp%60     
      if math.floor(seconds) < 10 and math.floor(minutes) > 9 and math.floor(hours) < 10:
        cv2.imwrite('../data/0'+str(math.floor(hours))+"-"+str(math.floor(minutes))+"-0"+str(math.floor(seconds))+'.jpg',frame)
      elif math.floor(hours) < 10 and math.floor(minutes) < 10 and math.floor(seconds) < 10:
        cv2.imwrite('../data/0'+str(math.floor(hours))+"-0"+str(math.floor(minutes))+"-0"+str(math.floor(seconds))+'.jpg',frame)
      elif math.floor(hours) < 10 and math.floor(minutes) < 10 and math.floor(seconds) > 10:
        cv2.imwrite('../data/0'+str(math.floor(hours))+"-0"+str(math.floor(minutes))+"-"+str(math.floor(seconds))+'.jpg',frame)
      elif math.floor(hours) < 10 and math.floor(minutes) > 10 and math.floor(seconds) > 10:
        cv2.imwrite('../data/0'+str(math.floor(hours))+"-"+str(math.floor(minutes))+"-"+str(math.floor(seconds))+'.jpg',frame)
  i+=1
  key = cv2.waitKey(1) & 0xFF
  if key == ord('q'):
    break
vidcap.release()
cv2.destroyAllWindows()
