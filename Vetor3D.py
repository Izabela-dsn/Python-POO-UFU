import math
import numpy as np

class Vetor3D(object):

    def __init__(self, x=0, y=0, z=0):
        self.x1 = x
        self.y1 = y
        self.z1 = z

    def produto_escalar(self, numero, num):
        return (numero[0] * num[0]) + (numero[1] * num[1]) + (numero[2] * num[2])
        #print('Valor do produto escalar é: '+ str(produto_escalar))    

    def projecao(self,numero,num):
        escalar = ((numero[0] * num[0] + numero[1] * num[1] + numero[2] * num[2])/(num[0]**2 + num[1]**2 + num[2]**2))
        i = (escalar*num[0])
        j = (escalar*num[1])
        k = (escalar*num[2])
        print ('O vetor projeção de um um vetor a em um vetor b é:(' + str(i)+','+str(j)+ ','+ str(k)+')') 

    def angulo_entre_dois_vetores(self, numero, num):
        prodesc = self.produto_escalar(numero,num)
        prodnorma = math.sqrt(numero[0]**2 + numero[1]**2 + numero[2]**2) * math.sqrt(num[0]**2 + num[1]**2 + num[2]**2)
        cosseno = prodesc/prodnorma
        angulo_em_rad = math.acos(cosseno)
        angulo_em_graus = (angulo_em_rad * 360)/(2*3.14) 
        print('O angulo é: ' + str(angulo_em_graus))
               
    def print(self, numero, num):
        print(str(numero))
        print(str(num))

    def modulo(self,numero,num):
        modulo_vetor1 = math.sqrt(numero[0]**2 + numero[1]**2 + numero[2]**2)
        modulo_vetor2 = math.sqrt(num[0]**2 + num[1]**2 + num[2]**2)
        print('Modulo do primeiro vetor 3D: ',modulo_vetor1)
        print('Modulo do segundo vetor 3D: ',modulo_vetor2)

    def produto_vetorial(self,numero,num):
        vet1 = np.array(numero)
        vet2 = np.array(num)
        results = np.cross(vet1,vet2)
        print('O produto vetorial é:', results)

vetor1 = input('Digite os numeros que compoem o vetor em tres dimensoes:')
numerorecebidos = vetor1.split(",")
numero = [float(numero) for numero in numerorecebidos]
a,b,c = numero

vetor2 = input('Digite os numeros que compoem o segundo vetor em tres dimensoes:')
numrecebidos = vetor2.split(",")
num = [float(numero) for numero in numrecebidos]
a,b,c = num

vet = Vetor3D()
vet.print(numero,num) 
vet.modulo(numero,num)
vet.produto_escalar(numero,num) 
vet.projecao(numero,num)  
vet.angulo_entre_dois_vetores(numero,num)
vet.produto_vetorial(numero,num)    

ProdEsca = vet.produto_escalar(numero,num)
print('Valor do produto escalar é: '+ str(ProdEsca))