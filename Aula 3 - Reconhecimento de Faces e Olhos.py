import cv2

carregaFace = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
carregaOlho = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

imagem = cv2.imread('imagens/img7.jpg')
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
faces = carregaFace.detectMultiScale(cinza)

for (x, y, l, a) in faces:
    imagem = cv2.rectangle(imagem, (x, y), (x + l, y + a), (255, 0, 0), 2)
    localOlho = imagem[y:y + a, x:x + l]
    OlhoCinza = cv2.cvtColor(localOlho, cv2.COLOR_BGR2GRAY)
    detetado = carregaOlho.detectMultiScale(OlhoCinza, scaleFactor=1.07, minNeighbors=2, maxSize=(90, 90))

    for (ox, oy, ol, oa) in detetado:
        cv2.rectangle(localOlho, (ox, oy), (ox + ol, oy + oa), (0, 0, 255), 2)

cv2.imshow('Reconhece Faces e Olhos', imagem)
cv2.waitKey()
