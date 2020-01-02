from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys, os


class Window(QMainWindow):
    def __init__(self, lista = []):
        super().__init__()
        Window.setWindowTitle(self, "Lista Encadeada")
        Window.resize(self,441, 414)
        self.setupUi()
        self.lista = lista

    def setupUi(self):

        self.insere = QtWidgets.QPushButton("INSERE",self)
        self.insere.setGeometry(QtCore.QRect(50, 130, 75, 23))
        self.insere.setObjectName("INSERE")
        self.insere.clicked.connect(self.Insere)

        self.remove = QtWidgets.QPushButton("REMOVE",self)
        self.remove.setGeometry(QtCore.QRect(50, 170, 75, 23))
        self.remove.setObjectName("remove")
        self.remove.clicked.connect(self.Remove)

        self.print_maior = QtWidgets.QPushButton( "MAIOR",self)
        self.print_maior.setGeometry(QtCore.QRect(50, 220, 75, 23))
        self.print_maior.setObjectName("print_maior")
        self.print_maior.clicked.connect(self.Maior)

        self.print_menor = QtWidgets.QPushButton("MENOR",self)
        self.print_menor.setGeometry(QtCore.QRect(50, 260, 75, 23))
        self.print_menor.setObjectName("print_menor")
        self.print_menor.clicked.connect(self.Menor)

        self.imprime = QtWidgets.QPushButton("IMPRIME",self)
        self.imprime.setGeometry(QtCore.QRect(50, 310, 75, 23))
        self.imprime.setObjectName("imprime")
        self.imprime.clicked.connect(self.imprim)

        self.lista = QtWidgets.QLabel("Lista:",self)
        self.lista.setGeometry(QtCore.QRect(60, 60, 47, 13))
        self.lista.setObjectName("lista")

        self.insere_valor_aqui = QtWidgets.QLineEdit(self)
        self.insere_valor_aqui.setGeometry(QtCore.QRect(170, 130, 113, 20))
        self.insere_valor_aqui.setObjectName("insere_valor_aqui")

        self.indereovalorprasertirado = QtWidgets.QLineEdit(self)
        self.indereovalorprasertirado.setGeometry(QtCore.QRect(170, 170, 113, 20))
        self.indereovalorprasertirado.setObjectName("indereovalorprasertirado")

        self.recebe_maior_num = QtWidgets.QLabel(self)
        self.recebe_maior_num.setGeometry(QtCore.QRect(170, 220, 111, 16))
        self.recebe_maior_num.setFrameShape(QtWidgets.QFrame.Box)
        self.recebe_maior_num.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.recebe_maior_num.setText("")
        self.recebe_maior_num.setObjectName("recebe_maior_num")

        self.recebe_menor_num = QtWidgets.QLabel(self)
        self.recebe_menor_num.setGeometry(QtCore.QRect(170, 260, 111, 16))
        self.recebe_menor_num.setFrameShape(QtWidgets.QFrame.Box)
        self.recebe_menor_num.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.recebe_menor_num.setText("")
        self.recebe_menor_num.setObjectName("recebe_menor_num")

        self.recebe_a_lista = QtWidgets.QLabel(self)
        self.recebe_a_lista.setGeometry(QtCore.QRect(100, 60, 251, 16))
        self.recebe_a_lista.setFrameShape(QtWidgets.QFrame.Box)
        self.recebe_a_lista.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.recebe_a_lista.setText("")
        self.recebe_a_lista.setObjectName("recebe_a_lista")
        
#falta: pop-up avisando que a lista ta vazia/ condição do remove / erros e excessões 
    def Insere(self):
        try:#pega o valor pelo lugar indicado
            valor = int(self.insere_valor_aqui.text())
            self.lista.append(valor)
            # self.recebe_a_lista.setText(str(self.lista))
            self.insere_valor_aqui.setText("")
        except ValueError:
            QMessageBox.warning(self, 'ATENÇÃO', "Somente valores inteiros more")

    def Remove(self):
        try:
            #quando o insere valor ta vazio ele imprime a lista lá em cima
            if self.indereovalorprasertirado.text() == '':
                self.recebe_a_lista.setText(str(self.lista[::-1]))
                #QMessageBox.warning(self,"ATENÇÃO", "Lista vazia more")
            else: 
                #se não está vazio ele coloca o num que quer tirar da lista e retira
                data = int(self.indereovalorprasertirado.text())
                self.lista.remove(data)
        except ValueError:
            QMessageBox.warning(self,'ATENÇÃO', "Só inteiros more")  #pop-up de erro  
                   
    def Maior(self):
        maximo = max(self.lista)
        self.recebe_maior_num.setText(str(maximo))
        #except:

    def Menor(self):
        minimo = min(self.lista)
        self.recebe_menor_num.setText(str(minimo)) 
        #except:       

    def imprim(self):
        if self.lista == []:#se a lista estiver vazia : mensagem de erro
            QMessageBox.warning(self, 'ATENÇÃO', 'Lista vazia more')
        else:    
            self.recebe_a_lista.setText(str(self.lista[::-1]))#imprime a lista de trás para frente

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
        