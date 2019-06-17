import cv2
# cams_test = 500
# for i in range(0, cams_test):
#     cap = cv2.VideoCapture(i)
#     test, frame = cap.read()
#     if test:
#         print("i : "+str(i)+" /// result: "+str(test))
#     else:
#     	break

def clearCapture(capture): 
    capture.release() 
    cv2.destroyAllWindows() 

def countCameras(): 
    n = 0 
    for i in range(10): 
     try: 
      cap = cv2.VideoCapture(i) 
      ret, frame = cap.read() 
      cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
      clearCapture(cap) 
      n += 1 
     except: 
      clearCapture(cap) 
      break 
    return n 

print (countCameras()) 