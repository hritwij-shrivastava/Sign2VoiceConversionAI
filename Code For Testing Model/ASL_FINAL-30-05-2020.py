import cv2
import time
import numpy as np
from threading import Thread
import vlc
from gtts import gTTS
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import sys
from PIL import Image
w=""
s=" "
model = load_model('gpu_model_epoch10.h5')
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), 0)
    crop_image = frame[100:300, 100:300]
    img = cv2.flip(crop_image, 1)
    frame=cv2.flip(frame, 1)
    cv2.imshow('a', frame)
    k = cv2.waitKey(125)
    j = 30
    if k == ord('a'):
        while j >= 10:
            ret, frame = cap.read()
            cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), 0)
            crop_image = frame[100:300, 100:300]
            img = cv2.flip(crop_image, 1)
            frame = cv2.flip(frame, 1)
            if j % 10 == 0:
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, str(j // 10), (250, 250), font, 7, (255, 255, 255), 10, cv2.LINE_AA)
            cv2.imshow('a', frame)
            cv2.waitKey(125)
            j = j - 1
        else:
            ret, frame = cap.read()
            cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), 0)
            crop_image = frame[100:300, 100:300]
            img = cv2.flip(crop_image, 1)
            frame = cv2.flip(frame, 1)
            cv2.imshow('a', frame)
            cv2.waitKey(1000)
            cv2.imwrite('camera.jpg', img)
            c=cv2.imread("camera.jpg")
            #cv2.imshow("output",c)
            mask = cv2.resize(c, (64, 64))
            img_array = np.array(mask)
            img_array_ex = np.expand_dims(img_array, axis=0)



            def keras_predict(model, image):
                data = np.asarray(image, dtype="float64")
                pred_probab = model.predict(data)[0]
                pred_class = list(pred_probab).index(max(pred_probab))
                return max(pred_probab), pred_class

            pred_probab, pred_class = keras_predict(model, img_array_ex)
            print(pred_class, pred_probab)
            count = pred_class
            if count == 0:
                def play_sound():
                    n = vlc.MediaPlayer("A.mp3")
                    n.play()
                thread = Thread(target=play_sound)
                thread.start()
                time.sleep(3)
                s="a"
                w = w + s
            elif count == 1:
                def play_sound1():
                    n = vlc.MediaPlayer("B.mp3")
                    n.play()
                thread = Thread(target=play_sound1)
                thread.start()
                time.sleep(3)
                s="b"
                w = w + s
            elif count == 2:
                def play_sound2():
                    n = vlc.MediaPlayer("C.mp3")
                    n.play()
                thread = Thread(target=play_sound2)
                thread.start()
                time.sleep(3)
                s="c"
                w = w + s
            elif count == 3:
                def play_sound3():
                    n = vlc.MediaPlayer("D.mp3")
                    n.play()
                thread = Thread(target=play_sound3)
                thread.start()
                time.sleep(3)
                s="d"
                w = w + s
            elif count == 4:
                def play_sound4():
                    n = vlc.MediaPlayer("E.mp3")
                    n.play()
                thread = Thread(target=play_sound4)
                thread.start()
                time.sleep(3)
                s="e"
                w = w + s
            elif count == 5:
                def play_sound5():
                    n = vlc.MediaPlayer("F.mp3")
                    n.play()
                thread = Thread(target=play_sound5)
                thread.start()
                time.sleep(3)
                s="f"
                w = w + s
            elif count == 6:
                def play_sound6():
                    n = vlc.MediaPlayer("G.mp3")
                    n.play()
                thread = Thread(target=play_sound6)
                thread.start()
                time.sleep(3)
                s="g"
                w = w + s
            elif count == 7:
                def play_sound7():
                    n = vlc.MediaPlayer("H.mp3")
                    n.play()
                thread = Thread(target=play_sound7)
                thread.start()
                time.sleep(3)
                s="h"
                w = w + s
            elif count == 8:
                def play_sound8():
                    n = vlc.MediaPlayer("I.mp3")
                    n.play()
                thread = Thread(target=play_sound8)
                thread.start()
                time.sleep(3)
                s="i"
                w = w + s
            elif count == 9:
                def play_sound9():
                    n = vlc.MediaPlayer("J.mp3")
                    n.play()
                thread = Thread(target=play_sound9)
                thread.start()
                time.sleep(3)
                s="j"
                w = w + s
            elif count == 10:
                def play_sound10():
                    n = vlc.MediaPlayer("K.mp3")
                    n.play()
                thread = Thread(target=play_sound10)
                thread.start()
                time.sleep(3)
                s="k"
                w = w + s
            elif count == 11:
                def play_sound11():
                    n = vlc.MediaPlayer("L.mp3")
                    n.play()
                thread = Thread(target=play_sound11)
                thread.start()
                time.sleep(3)
                s="l"
                w = w + s
            elif count == 12:
                def play_sound12():
                    n = vlc.MediaPlayer("M.mp3")
                    n.play()
                thread = Thread(target=play_sound12)
                thread.start()
                time.sleep(3)
                s="m"
                w = w + s
            elif count == 13:
                def play_sound13():
                    n = vlc.MediaPlayer("N.mp3")
                    n.play()
                thread = Thread(target=play_sound13)
                thread.start()
                time.sleep(3)
                s="n"
                w = w + s
            elif count == 14:
                def play_sound14():
                    n = vlc.MediaPlayer("O.mp3")
                    n.play()
                thread = Thread(target=play_sound14)
                thread.start()
                time.sleep(3)
                s="o"
                w = w + s
            elif count == 15:
                def play_sound15():
                    n = vlc.MediaPlayer("P.mp3")
                    n.play()
                thread = Thread(target=play_sound15)
                thread.start()
                time.sleep(3)
                s="p"
                w = w + s
            elif count == 16:
                def play_sound16():
                    n = vlc.MediaPlayer("Q.mp3")
                    n.play()
                thread = Thread(target=play_sound16)
                thread.start()
                time.sleep(3)
                s="q"
                w = w + s
            elif count == 17:
                def play_sound17():
                    n = vlc.MediaPlayer("R.mp3")
                    n.play()
                thread = Thread(target=play_sound17)
                thread.start()
                time.sleep(3)
                s="r"
                w = w + s
            elif count == 18:
                def play_sound18():
                    n = vlc.MediaPlayer("S.mp3")
                    n.play()
                thread = Thread(target=play_sound18)
                thread.start()
                time.sleep(3)
                s="s"
                w = w + s

            elif count == 19:
                def play_sound19():
                    n = vlc.MediaPlayer("T.mp3")
                    n.play()
                thread = Thread(target=play_sound19)
                thread.start()
                time.sleep(3)
                s="t"
                w = w + s
            elif count == 20:
                def play_sound20():
                    n = vlc.MediaPlayer("U.mp3")
                    n.play()
                thread = Thread(target=play_sound20)
                thread.start()
                time.sleep(3)
                s="u"
                w = w + s
            elif count == 21:
                def play_sound21():
                    n = vlc.MediaPlayer("V.mp3")
                    n.play()
                thread = Thread(target=play_sound21)
                thread.start()
                time.sleep(3)
                s="v"
                w = w + s
            elif count == 22:
                def play_sound22():
                    n = vlc.MediaPlayer("W.mp3")
                    n.play()
                thread = Thread(target=play_sound22)
                thread.start()
                time.sleep(3)
                s="w"
                w = w + s
            elif count == 23:
                def play_sound23():
                    n = vlc.MediaPlayer("X.mp3")
                    n.play()
                thread = Thread(target=play_sound23)
                thread.start()
                time.sleep(3)
                s="x"
                w = w + s
            elif count == 24:
                def play_sound24():
                    n = vlc.MediaPlayer("Y.mp3")
                    n.play()
                thread = Thread(target=play_sound24)
                thread.start()
                time.sleep(3)
                s="y"
                w = w + s
            elif count == 25:
                def play_sound25():
                    n = vlc.MediaPlayer("Z.mp3")
                    n.play()
                thread = Thread(target=play_sound25)
                thread.start()
                time.sleep(3)
                s="z"
                w = w + s
            elif count == 26:
                def play_sound26():
                    n = vlc.MediaPlayer("del.mp3")
                    n.play()
                thread = Thread(target=play_sound26)
                thread.start()
                time.sleep(3)
                w = w[:-1]
            elif count == 27:
                def play_sound27():
                    n = vlc.MediaPlayer("nothing.mp3")
                    n.play()
                thread = Thread(target=play_sound27)
                thread.start()
                time.sleep(3)

            elif count == 28:
                def play_sound28():
                    n = vlc.MediaPlayer("space.mp3")
                    n.play()
                thread = Thread(target=play_sound28)
                thread.start()
                time.sleep(3)
                s=" "
                w=w + s
            else:
                pass


    # Press Esc to exit
    elif k == 27:
        print(w)
        r = gTTS(text=w, lang='en', slow=False)
        r.save("r.mp3")


        def play_sound29():
            n = vlc.MediaPlayer("r.mp3")
            n.play()


        thread = Thread(target=play_sound29)
        thread.start()
        time.sleep(3)
        break
cap.release()
cv2.destroyAllWindows()
