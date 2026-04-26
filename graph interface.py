#PyQt5 introduction
#install PyQt5 : pip install PyQt5

import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow #importamos del paquete que instalamos los modulos que nos serviran para la interface grafica
from PyQt5.QtGui import QIcon #necesario importar este modulo para poder alterar el icono

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first GUI")
        self.setGeometry(0,0,500,500)
        #self.setGeometry(x,y,width,self.height)
        self.setWindowIcon(QIcon("librery/images/images presentacion.jpeg")) #se pone la ruta del icono dentro de QIcon.
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())#esto es necesario para que la pantalla no se cierre al instante, se usa "exec_" El otro es usado para codigo de base antiguos.

if __name__ == "__main__":
    main()