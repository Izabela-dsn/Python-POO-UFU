#Izabela da Silva Neves 11811ECP026
class Pessoa(object):
    def __init__(self, nome ='', codigo = 0, salario = 1000):
        self.nome = nome
        self.codigo = codigo
        self.salario = salario 
        
from Trabalho3 import Pessoa

class Trabalhador(Pessoa):
    def __init__(self, nome = '', codigo = 0, salario = 1000, escolaridade = ''):
        Pessoa.__init__(self, nome, codigo, salario)
        self.escolaridade = escolaridade

    def salarioEscolaridade(self):
        if self.escolaridade == 'sem escola':
            salariototal = self.salario
        elif self.escolaridade == 'ensino basico':
            salariototal = self.salario + 10/100* self.salario
        elif self.escolaridade == 'ensino medio':
            salariototal = self.salario + 50/100*self.salario
        elif self.escolaridade == 'faculdade':
            salariototal = self.salario + 100/100*self.salario

        print('salario = ' + str(salariototal))

    def guardar(self):
        lista = [self.nome,self.codigo,self.escolaridade]
        print(lista)
            
a1 = Trabalhador("Geise", 56, 1000, 'ensino medio')
a2 = Trabalhador('Geronimo', 54,1000,'sem escola')
a3 = Trabalhador('Henrietta', 89,1000,'faculdade')
a4 = Trabalhador('Juliana', 25,1000,'ensino basico') 
a1.guardar()
a1.salarioEscolaridade()
a2.guardar()
a2.salarioEscolaridade()
a3.guardar()
a3.salarioEscolaridade()
a4.guardar()
a4.salarioEscolaridade()



