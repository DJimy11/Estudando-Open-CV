import cv2


carregaFace = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
carregaOlho = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')
imagem = cv2.imread('Imagens/img5.jpg')
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
faces = carregaFace.detectMultiScale(cinza)

for (x, y, l, a) in faces:
    reconhecer = cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 255, 0), 2)
    localOlho = reconhecer[y:y + a, x:x + l]
    olhoCinza = cv2.cvtColor(localOlho, cv2.COLOR_BGR2GRAY)
    detetado = carregaOlho.detectMultiScale(olhoCinza, scaleFactor=1.07, minNeighbors=3)

    for (ox, oy, ol, oa) in detetado:
        cv2.rectangle(localOlho, (ox, oy), (ox + ol, oy + oa), (0, 0, 255), 2)

cv2.imshow('Olhos e Faces detetados', imagem)
cv2.waitKey()