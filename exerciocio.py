class Resistor(object):

    def __init__ (self, resistencia = 0, maxpotencia = 0):
        self.resistencia = r
        self.maxpotencia = m

    def resistorSerie(self,resistor1,resistor2):

        resistorequivalente = resistor1[0] + resistor2[0]
        if resistor1 [1] < resistor2[1]:
            maxpotenciaequi = resistor1[1]
        else:
            maxpotenciaequi = resistor2[1] 

        print('EM SERIE: resistor = ' + str(resistorequivalente) + '\nmaxpotencia = ' + str(maxpotenciaequi))       

    def resistorParalelo(self, resistor1,resistor2):
        resistenciaequiemparalelo = resistor1[0]*resistor2[0] / resistor1[0]+resistor2[0]
        if resistor1 [1] < resistor2[1]:
            maxpotenciaequi = resistor1[1]
        else:
            maxpotenciaequi = resistor2[1] 

        print('EM PARALELO: resistor = ' + str(resistenciaequiemparalelo) + '\nmaxpotencia = ' + str(maxpotenciaequi))    

re = input('adicione a resistencia e a maxima potencia do resistor 1: ')
valorecebido = re.split(' ')
resistor1 = [float(valor) for valor in valorecebido]
r,m = resistor1

re2 = input('adicione a resistencia e a maxima potencia do resistor 2: ')
valorecebidos = re2.split(' ')
resistor2 = [float(valor) for valor in valorecebidos]
r,m = resistor2

R = Resistor()
R.resistorSerie(resistor1, resistor2)
R.resistorParalelo(resistor1,resistor2)