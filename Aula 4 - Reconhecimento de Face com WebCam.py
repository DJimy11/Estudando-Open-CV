import cv2

webcamera = cv2.VideoCapture(0)
'''webcamera.set(3, 640)
webcamera.set(4, 480)'''
while True:
    camera, frame = webcamera.read()
    cv2.imshow('Imagem da web camera', frame)

    if cv2.waitKey(1) == ord('q'):
        break


webcamera.release()
cv2.destroyAllWindows()
