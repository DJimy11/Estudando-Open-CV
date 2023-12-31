import cv2


carregaAlgoritmo = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
imagem = cv2.imread('Imagens/img6.jpg')
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
faces = carregaAlgoritmo.detectMultiScale(cinza, scaleFactor=1.08, minNeighbors=1, minSize=(5, 5))
print(faces)

for (x, y, l, a) in faces:
    cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 255, 0), 2)

cv2.imshow('faces', imagem)
cv2.waitKey()
