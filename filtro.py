# IMPORTAR BIBLIOTECAS DE PYTHON
import cv2
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# IMPRIMIR IMAGEM
img = cv2.imread('P&B.jpg', 0)
plt.imshow(img,cmap='gray')
plt.axis('off')

# AJUSTAR DIMENSÃO IMAGENS
plt.figure(figsize= (10,10))
plt.imshow(img,cmap='gray')
plt.axis('off')

# CRIAR LISTAS




