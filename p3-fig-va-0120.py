import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Nicole Robles NC 0120
print("Nicole Robles  NC = 0120")
print("UIII Act3 colocar puntos a una imagen  en blanco y negro")

# Cargar imagen y convertir de BGR a RGB para Matplotlib
img_cornelio = cv2.imread("corneliovega.jpeg")
img_rgb = cv2.cvtColor(img_cornelio, cv2.COLOR_BGR2RGB)

plt.imshow(img_rgb)
plt.title("Cornelio Vega y Nicole Robles 0120")
plt.show()

print("+-+-+- Puntos en la imagen -+-+-+")
plt.imshow(img_rgb)
x = [100, 100, 300, 340]
y = [100, 400, 500, 300]
plt.scatter(x, y, s=20, c="red")
plt.show()

print("+-+-+- Cuadro en la imagen -+-+-+")
plt.imshow(img_rgb)
x = [160, 160, 460, 460, 160]
y = [450, 150, 150, 450, 450]
plt.plot(x, y, color="blue", linewidth=2)
plt.show()

print("+-+-+- Circulo verde en la imagen -+-+-+")
plt.imshow(img_rgb)

N = 30  # lados del poligono
x = np.zeros((N + 1,))
y = np.zeros((N + 1,))
(xc, yc) = (340, 320)
r = 150  # radio

for i in range(N + 1):
    t = 2 * np.pi / N * i
    x[i] = xc + r * np.cos(t)
    y[i] = yc + r * np.sin(t)

plt.plot(x, y, c="green")
plt.show()