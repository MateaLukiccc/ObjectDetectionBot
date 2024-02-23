from ultralytics import YOLO

import numpy as np
import mss
import cv2
import time
import keyboard
import pyautogui
pyautogui.FAILSAFE = False

def plot_boxes(img, results, move=True):
    
    for box in results[0].boxes:
        cord = box.xyxy[0].tolist()
        cord = [round(x) for x in cord]
        labels = results[0].names[box.cls[0].item()]
        x1, x2, y1, y2 = cord[0], cord[1], cord[2], cord[3]
        cv2.rectangle(img, (x1, y1), (x2, y2), (0,0,255), 2)
        cv2.putText(img,labels, (50, 50) , cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
              
    return img


if __name__ == '__main__':
    model = YOLO("best.pt")

    sct = mss.mss()
    box = {
        'top': 0,
        'left': 0,
        'width': 1920,
        'height': 1080,
    }
    img = sct.grab(box)
    img = np.array(img)[:,:,:3]
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)


    print("-------- Press 's' to begin program! --------")
    while not keyboard.is_pressed("s"):
        time.sleep(.01)

    print("Starting program in 5 seconds.")
    time.sleep(5)

    while not keyboard.is_pressed("q"):
        start_time = time.time()
        img = sct.grab(box)
        img = np.array(img)[:,:,:3]
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        results = model.predict(img)  
        img = plot_boxes(img, results, True)
        
        # show the window with border boxes
        cv2.namedWindow("test", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("test",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        small = cv2.resize(img, (0,0), fx=0.75, fy=0.75) 
        cv2.imshow("test", small)


        if cv2.waitKey(1) == ord('q'):
            break
