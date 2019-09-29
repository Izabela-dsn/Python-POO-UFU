class Tempo(object):

    def __init__(self, hora, minuto, segundo):
        self.h = hora
        self.min = minuto
        self.seg = segundo
     
    def imprimirhoras(self):
        if self.seg and self.min > 60:
            print('Entrada de horas invalida, tente novamente')
        elif self.h > 24:
            print('Entrada de horas invalida, tente novamente')

    #gerar o tempo de permanencia (subtracao dos dois tempos)
    def tempo_de_permanencia(self):
        totalh = numero[0] - num[0] 
        totalm = numero[1] - num[1] 
        totals = numero[2] - num[2]
        print("Tempo de permanência " + str(abs(totalh)) + ':' + str(abs(totalm)) + ':' + str(abs(totals)))   

        #valor cobrado pela permanencia
        if abs(totalh) > 0:
           valordahora = totalh * 7 + totalm/7 + totals/7
           valordahora = round(valordahora,2)
        print('Valor a ser cobrado pela permanecia: R$' + str(abs(float(valordahora))))

#solicitação da hora de entrada
horarios = input('Digite o horario de entrada (hh:mm:ss):')
numerorecebidos = horarios.split(":")
numero = [int(numero) for numero in numerorecebidos]
Hora, Minuto, Segundo = numero

#solicitação da hora de saida
horarios2 = input('Digite o horario de saída (hh:mm:ss) :')
numrecebido = horarios2.split(':')
num  = [int(num) for num in numrecebido]
Hora,Minuto,Segundo = num


class Estacionamento(Tempo):

    def __init__(self,hora,minuto,segundo, placa, marca):
        Tempo.__init__(self,hora,minuto,segundo)
        self.Placa = placa
        self.Marca = marca

    def imprimir_informacoes_preliminares(self):
        print("Sua placa é " + str.upper(self.Placa) + " e a marca do seu carro é " + str.upper(self.Marca))
 
#solicitação da placa e marca do carro
p = input('Digite a placa do seu carro:')
m = input('Digite a marca do seu carro:')
        
temp = Estacionamento(Hora,Minuto,Segundo,p,m)
temp.imprimirhoras()
temp.imprimir_informacoes_preliminares()
temp.tempo_de_permanencia()

