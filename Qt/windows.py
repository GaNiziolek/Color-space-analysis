from PyQt5.QtWidgets import (QMainWindow, QWidget, QPushButton,
                             QVBoxLayout, QHBoxLayout, QApplication,
                             QLabel)
from PyQt5.QtGui import QIcon, QPixmap, QImage
from imTrans import imgTransform as imT
import numpy as np


class StartWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 640, 480)
        # Botões
        self.central_widget = QWidget()
        self.bt_MostraImg = QPushButton('Mostrar Imagem', self.central_widget)
        
        # Imagens
        lb_img1 = QLabel(self)
        image1 = imT('qt_OpenCV\Laterais_da_Peca.jpeg').show()
        image1 = QImage(image1, image1.shape[1], image1.shape[0], QImage.Format_RGB888)
        lb_img1.setPixmap(QPixmap(image1))
        
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.addWidget(lb_img1)
        self.layout.addWidget(self.bt_MostraImg)
        self.setCentralWidget(self.central_widget)