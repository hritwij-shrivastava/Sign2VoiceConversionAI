import cv2
#cap = cv2.VideoCapture('http://192.168.43.1:8080/video')
cap = cv2.VideoCapture(0)

i=25
l=0
while True:
    ret, frame = cap.read()
    cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), 0)
    crop_image = frame[100:300, 100:300]
    img = cv2.flip(crop_image, 1)
    frame=cv2.flip(frame, 1)
    cv2.imshow('a', frame)
    k = cv2.waitKey(125)
    j = 10
    if k == ord('a'):
        i = i + 1
        l = l + 1
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
            cv2.imwrite('D:/Project/Hand Gesture/sign/B/B' + str(i) + '.jpg', img)
            #print("i=",i)
            print(l,"i =",i)
            if(l==25):
                print("DONE")

    elif k == 27:
        break
cap.release()
cv2.destroyAllWindows()
