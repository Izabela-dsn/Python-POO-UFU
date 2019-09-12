import math #Izabela da Silva Neves 11811ECP026
class Vetor2D(object):
    def __init__(self, X, Y, x1, y1):
        self.x= float(X)
        self.y= float(Y)
        # primeiro vetor/ vetor default
        self.x1 = 0
        self.y1 = 0

    def produto_escalar(self):
        produto_escalar = self.x1 * self.x + self.y1 * self.y
        print('Valor do produto escalar é: '+ str(produto_escalar))

    def modulo_vetor(self):
        modulo_vetor = math.sqrt(self.x**2 + self.y**2)
        print('Módulo do vetor com os números dados é: '+ str(modulo_vetor))   
        print('Módulo do vetor nulo é 0.\n')
#a é o vetor nulo b é o vetor receptor projeção de a em b
    def projecao(self):
        escalar = ((self.x1 * self.x + self.y1 * self.y)/math.pow((math.sqrt(self.x**2 + self.y**2)),2))
        i = (escalar*self.x)
        j = (escalar*self.y)
        print ('O vetor projeção de um um vetor a em um vetor b é:(' + str(i)+','+str(j)+ ')')

    def angulo_entre_dois_vetores(self): #nessa parte da um erro 
        angulo_entre_dois_vetores = math.cos((self.x1 * self.x + self.y1 * self.y)/math.sqrt(self.x**2 + self.y**2)*math.sqrt(self.x1**2 + self.y1**2))
        print('O angulo entre dois vetores é: ' + str(angulo_entre_dois_vetores))     

a = input('Digite o valor de x:')
b = input('Digite o valor de y:')
rec = Vetor2D(a,b,0,0)
rec.produto_escalar()
rec.modulo_vetor()
rec.angulo_entre_dois_vetores()
rec.projecao()
