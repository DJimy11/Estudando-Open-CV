import cv2

webcamera = cv2.VideoCapture(0)
classificadorVideo = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
classificadorOlho = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')


while True:
    camera, frame = webcamera.read()

    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    deteta = classificadorVideo.detectMultiScale(cinza)

    for (x, y, l, a) in deteta:
        cv2.rectangle(frame, (x, y), (x + l, y + a), (255, 0, 0), 2)
        pegaOlho = frame[y:y + a, x:x + l]
        OlhoCinza = cv2.cvtColor(pegaOlho, cv2.COLOR_BGR2GRAY)
        localizaOlho = classificadorOlho.detectMultiScale(OlhoCinza)
        for (ox, oy, ol, oa) in localizaOlho:
            cv2.rectangle(pegaOlho, (ox, oy), (ox + ol, oy + oa), (0, 255, 0), 2)

    cv2.imshow('Video WebCam', frame)
    if cv2.waitKey(1) == ord('q'):
        break

webcamera.release()
cv2.destroyAllWindows()