import sys
import os
from tkinter import messagebox
from PyQt5.uic import loadUi
#from PySide6.QtCore import QPoint
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsView
from PyQt5.QtGui import *
from QRCodeUI import *
from qrcode import *
from qrcode.main import QRCode
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import json




def resource_path(rel_path):
    ''' Get absolute path to resource'''
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_ppath = os.path.abspath(".")
    return os.path.join(base_path, rel_path)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        super().__init__()
        self.ui = Ui_MainWindow()
        self.qrHistory = {}
        self.loadHistory()


        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.currentImage = None
        self.currentLink = None
        self.currQR = None
        self.ui.setupUi(self)
        self.show()

        self.ui.viewHistoryButton.clicked.connect(self.switchToHistoryPage)
        self.ui.returnToHomeButton.clicked.connect(self.switchToMainPage)
        self.ui.downloadImageButton.clicked.connect(self.downloadImage)
        self.ui.generateQRButton.clicked.connect(self.generateQR)
        
        #set default screen
        self.switchToMainPage()


    def dumpHistory(self):
        print(self.qrHistory)
        try:
            with open(resource_path("qrHistory.json"), "w") as f:
                    json.dump(self.qrHistory, f)
        except Exception as e:
            print("An error occured", e)
        return
    
    def loadHistory(self):
        try:
            with open(resource_path("qrHistory.json"), "r") as f:
                    self.qrHistory = json.load(f)
                    print(self.qrHistory)
        except Exception as e:
            print("An error occured", e)

        return
    
    def downloadImage(self):
        if self.currentImage != None:
            file_path = filedialog.asksaveasfilename(initialfile="newImage.jpg",initialdir="..\Downloads\\",defaultextension=".ext", filetypes=[("JPEG","*.jpg"),("PNG","*.png"),("All Files", "*.*")])
            if file_path:
                # Display the selected path in a message box
                self.currentImage.save(resource_path(file_path))
                messagebox.showinfo("Success", f"You succesfully saved: {file_path}")
                self.qrHistory[file_path] = self.currentLink
                self.dumpHistory()            
            else:
                # User canceled the operation
                messagebox.showwarning("No Selection", "No folder selected")
            pass
        else:
            messagebox.showinfo("Error", f"Please generate QR code first")

    def switchToMainPage(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def switchToHistoryPage(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def generateQR(self):
        text = self.ui.qrLinkLineEdit.text()
        if text != "":
            self.currentLink = text
            self.currQR = QRCode()
            self.currQR.add_data(text)
            self.currentImage = self.currQR.make_image()
            '''save temp image top display in app'''
            messagebox.showinfo("Success", f"You succesfully created the qr code")
            self.currentImage.save(resource_path("QRCodes\qrImageLabelView.jpg"))
            try:
                self.ui.qrImageLabelView.setStyleSheet(f" QLabel {{ background-image: url({resource_path("QRCodes/qrImageLabelView.jpg")}); background-position: center; background-repeat: no-repeat; background-size: cover; }} ")
                pixmap = QPixmap("QRCodes\qrImageLabelView.jpg")
                self.ui.qrImageLabelView.setPixmap(pixmap)
            except Exception as e:
                print(e)

            
        else:
            print("Please enter text!!")


    def QRfilter(text):
        ''' Implement to filter out dangerous data'''
        return text

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())