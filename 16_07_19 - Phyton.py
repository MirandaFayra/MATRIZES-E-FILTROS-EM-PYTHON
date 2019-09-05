#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n1 = input ('Digite um número: ')
n2 = input ('Digite um número: ')

n1 = int (n1)
n2 = int (n2)

if n1 > n2:
    print (str(n1) +' é maior que ' + str(n2))
    
elif n1 < n2:
    print (str(n1) +' é menor que ' + str(n2))
    
else:
  print('os números são iguais')
    


# In[ ]:


nota1 = float(input('Digite sua Primeira Nota: '))
nota2 = float(input('Digite sua Segunda Nota: '))
nota3 = float(input('Digite sua Terceira Nota: '))

media = (nota1+nota2+nota3)/3

if media >= 5 and media <= 10:
    print(' Aprovado! ')
elif media >= 3 and media <5:
    print('Recuperação')
elif media < 3 and media >=0:
    print('Reprovado')
else:
    print('Notas Invalidas')


# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[38]:


img = cv2.imread('P&B.jpg', 0)
plt.imshow(img,cmap='gray')
plt.axis('off')
# print(img)


# In[4]:


plt.figure(figsize= (10,10))
plt.imshow(img,cmap='gray')
plt.axis('off')


# ##LISTAS 

# Gravar valores dentro de uma mesma estrutura
# 

# In[6]:


nomes = [ 'Fayra', 'Tolentino', 'Miranda']


# In[7]:


# Para só acessar um item dentro da lista.Usar indice do elemento na lista = Nome da Variável e a posição no Indice

nomes [0]


# In[10]:


# Para saber o tipo de Elemento
type(nomes[2])


# In[12]:


# Para imprimir os valores no intervalo, sem pegar o ultimo
nomes[0:2]


# In[13]:


Percorrer Todos os  Elementos da lista dentro do intervalo que você deu, até o fim
nomes[1:]


# In[14]:


# Saber o tamanho da lista - Quantos os elementos que há na lista 
len (nomes)


# In[15]:


# Passar de Valor por valor, nos itens por item - FOR OF DO JS
for item in nomes:
    print(item)


# In[16]:


# SEGUNDA OPÇÃO - loop cotador -> LOOP DENTRO DO INTERVALO - FOR IN DO JS
for valor in range (0,5):
    print(valor)


# In[17]:


tamanho= len(nomes)
for indice in range (0,tamanho):
    print (nomes[indice])


# In[18]:


# Lista Dentro de Listas - devem ser separadas por virgulas - cada lista é uma tabela da linha
lista_2d= [[2,3,4],[3,6,7], [4,6,7]]
tamaho= len(lista_2d)
for indice in range(0,tamanho):
    print (lista_2d[indice])


# In[ ]:


# Percorrer Elemento por Elemento da Lista 2D e Somar em 5 o valor de cada uma delas
linhas = len(lista_2d)
# Para saber quantas colunas tem, pegar a primeira posição do indice como o valor 
colunas= len(lista_2d[0])

for linha in range(0, linhas):
        for coluna in range(0, colunas)
# Para somar 5 unidades nos núemros da tabela
        print(lista_2d[linha][coluna])


# In[ ]:


tamanho = len(lista_2d)


# In[26]:


# Fazer operações em todos os elementos da lista - operações dentro de imagens
array= np.array ([[2,3,4],[3,6,7], [4,6,7]])


# In[27]:


print(array)


# In[28]:


# Multiplicação de Matrizes 
np.dot(array,array)


# In[39]:


# Para pecorrer pixel por pixel da imagem
img2=img.copy()

linhas=len(img)
colunas=len(img[0])
    
for linha in range(linhas):
    for coluna in range(colunas):
        img2[linha][coluna]=0
            
plt.imshow(img,cmap='gray')
plt.axis('off')


# Filtro Passa Alta
# 
# Pixel em preto, em baixo do valor
# 

# In[58]:


# Copy é uma função
img3= img.copy()

linhas = len(img3)
colunas = len(img[0])

# Parametro de filtragem, condição para deixar ou não preto
limiar= 100

for linha in range(linhas):
    for coluna in range(colunas):
        pixel = img3[linha][coluna]
        if pixel < limiar:
            img3[linha][coluna]=0
            
plt.imshow(img3,cmap='gray')


# **Filtro passa Baixa**
# 

# In[57]:


# Copy é uma função
img3= img.copy()

linhas = len(img3)
colunas = len(img[0])

# Parametro de filtragem, condição para deixar ou não preto
limiar= 100

for linha in range(linhas):
    for coluna in range(colunas):
        pixel = img3[linha][coluna]
        if pixel > limiar:
            img3[linha][coluna]=255
  

    plt.imshow(img,cmap='gray')


# In[54]:


# Medir a iamgem
img4 = img.copy()
largura, altura = img4.shape

# Pegar o Valor médio da imagem - MEAN
media= img4.mean()

# Condição para a impressão

# NÃO ESQUECER DE IDENTARRRRRR!

for linha in range (largura):
    for coluna in range (altura):
        pixel=img4[linha] [coluna]
        if pixel > media:
            img4[linha][coluna]= 1
        else:
            img4[linha][coluna]= 0

# NÃO ESQUECER DE PRINTAR A IMAGEM E IMPRIMIR A OUTRA!           
plt.imshow(img4,cmap='gray')


# In[55]:


img = cv2.imread('flor.jpg', 1)
plt.imshow(img)


# In[64]:


# CONVERTER AS CORES PARA O TOM ORIGINAL DA IMAGEM
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# In[65]:


plt.imshow(img)


# In[67]:


red = img.copy()
# Zerando as Cores das Camadas
red [: ,:,1] = 0
red [: ,: ,2] = 0
plt.imshow(red)


# In[68]:


blue= img.copy()
# Zerando as Cores das Camadas
blue [: ,:,0] = 0
blue [: ,: ,1] = 0
plt.imshow(blue)


# In[69]:


green= img.copy()
# Zerando as Cores das Camadas
green [: ,:,0] = 0
green [: ,: ,2] = 0
plt.imshow(green)


# In[74]:


# Imagem Colorida tem três dimensões, portanto para percorrer toda a imagem precisa de três for (np.array)
#  ter [] pq é uma lista dentro de lista
kernel= np.array([
    [-1, -1, -1],
    [-1, 8, -1 ],
    [-1, -1, -1]
])

# Parametro , parametro (-1) e o nome da variável - 2D MAIUSCULO
saida = cv2.filter2D(img, -1, kernel)
plt.imshow(saida)


# In[ ]:




