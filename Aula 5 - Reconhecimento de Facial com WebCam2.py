import cv2

webcamera = cv2.VideoCapture(0)
classificador = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

while True:
    camera, frame = webcamera.read()
    #cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    deteta = classificador.detectMultiScale(cinza)
    for (x, y, l, a) in deteta:
        cv2.rectangle(frame, (x, y), (x + l, y + a), (255, 0, 0), 2)
    
    cv2.imshow('Video WebCamera', frame)
    if cv2.waitKey(1) == ord('q'):
        break

webcamera.release()
cv2.destroyAllWindows()
