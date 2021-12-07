from confunc import download_server_Tk, get_config
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QFileDialog
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt
from sys import argv, exit as sys_exit
import psutil
import json
import os

class MainWindow(QWidget):
    """Main Window for MC-Server-Installer

    Args:
        QWidget ([type]): Parent class
    """
    def __init__(self, parent:QWidget = None):
        if parent is None:
            super().__init__()
        else:
            super().__init__(parent)
        self.initUI()
    
    def initUI(self):
        """Initialize UI"""
        self.setWindowTitle('MC-Server-Installer')
        self.setGeometry(300, 300, 300, 200)
        self.setWindowIcon(QIcon('icon.ico'))
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap('assets/pictures/background.png'))
        self.background.move(0, 0)
        self.versionlbl = QLabel('Version:', self)        
        self.versionlbl.move(20, 20)
        self.setFont(QFont('Arial', 15))
        self.show()

def main():
    """Main function"""
    app = QApplication(argv)
    window = MainWindow()
    app.setActiveWindow(window)
    app.exec_()

if __name__ == '__main__':
    main()