import cv2
import numpy as np
from keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from keras.preprocessing import image
from PIL import ImageFile
import threading
import time
import datetime

def Camera():

    import __main__
       
    print("=== start camera ===")
    camera=threading.current_thread()

    capture = cv2.VideoCapture(0) 
        
    if capture.isOpened() is False:
        print("IO Error")

    cv2.namedWindow("Capture", cv2.WINDOW_AUTOSIZE)
    
    while getattr(camera, "decide", True):

        ret, im = capture.read()
        if ret == False:
            continue

        cv2.imshow("Capture", im)
        cv2.waitKey(500)        
        cv2.imwrite("image.png", im)
    
    capture.release()
    cv2.destroyAllWindows()

def Predict():
    
    import __main__
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    print("=== start predict ===")
    predict=threading.current_thread()

    model = VGG16(include_top=True, weights='imagenet', input_tensor=None, input_shape=None)
    
    while getattr(predict, "decide", True):

        filename = 'image.png'

        img = __main__.image.load_img(filename, target_size=(224, 224))
        image = __main__.image.img_to_array(img)
        image = np.expand_dims(image, axis=0)

        predict = model.predict(preprocess_input(image))
        results = decode_predictions(predict, top=5)[0]
        #picture = cv2.imread(filename)

        for result in results:
            print(result)

        #cv2.imshow('test', picture)
        #cv2.waitKey(1000)
        #cv2.destroyAllWindows()
        time.sleep(5)

if __name__=="__main__":

    camera = threading.Thread(target=Camera, name='camera')
    predict= threading.Thread(target=Predict, name='predict')

    camera.start()
    time.sleep(1)
    predict.start()
    time.sleep(1)

    while True: 
        print("=== Key in main ===")
        k = cv2.waitKey(1000)        
        if k >= 0:
            camera.decide = False
            predict.decide = False
            camera.join()
            time.sleep(1)
            predict.join()
            break        



