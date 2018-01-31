import cv2
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
import numpy as np
from  keras.preprocessing.image import img_to_array
from  keras.preprocessing.image import load_img
import keras
from keras.utils import plot_model
from keras.callbacks import EarlyStopping
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense,Dropout,Flatten
from keras.layers import Conv2D,MaxPooling2D
from keras import backend as K



model=Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),activation='relu',input_shape=(28,28,1)))
model.add(Conv2D(64,(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10,activation='softmax'))

model.load_weights('mnist.h5')

model.compile(loss=keras.losses.categorical_crossentropy,optimizer=keras.optimizers.Adadelta(),metrics=['accuracy'])

img_path='image.png'

if __name__=="__main__":
    capture = cv2.VideoCapture(0)
    
    if capture.isOpened() is False:
        print("IO Error")

    cv2.namedWindow("Capture", cv2.WINDOW_AUTOSIZE)

    while True:

        ret, image = capture.read()

        if ret == False:
            continue

		#輪郭を抽出する
        image =cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

        x,y,w,h= cv2.boundingRect(image)
        #image = cv2.fastNIMeansDenosing(image)
        image = cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,0),2)
        rt, bw = cv2.threshold(image, 50,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        #im ,cont,hier = cv2.findContours(bw,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        #x,y,w,h= cv2.boundingRect(bw)
        bw = cv2.bitwise_not(bw)
        bw = cv2.rectangle(bw,(160,120),(480,360),(255,255,255),5)
        cv2.imshow("Capture", bw)
        k = cv2.waitKey(1)
        if k == 27:
            bw = image[120:360,160:480]
            rt, bw = cv2.threshold(bw, 50,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            bw = cv2.bitwise_not(bw)
            cv2.imwrite("image.png", bw)
            img = load_img(img_path,grayscale = True, target_size=(28,28))
            x=img_to_array(img)
            x /= 255
            x=np.expand_dims(x,axis=0)
            print(x.shape)
            model.summary()
            features= model.predict(x)
            print(features)
            print(np.argmax(features))
        if k == 42:
            break

    cv2.destroyAllWindows()

