import sqlite3
import sys

from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLabel, QMessageBox
from PyQt6 import uic

import LoginForm
import Veritabanim


class KullaniciKayit(QMainWindow):
    def __init__(self):
        super(KullaniciKayit, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowIcon(QIcon("image/icon.jpg"))

        background_label = QLabel(self)
        background_label.setGeometry(0, 0, 800, 600)
        pixmap = QPixmap('image/icon.jpg')

        background_label.setPixmap(pixmap)
        background_label.setScaledContents(True)

        uic.loadUi('Forms/RegisterForm.ui', self)
        self.KullaniciAdi = self.findChild(QLineEdit, 'lineEdit_kullaniciadi')
        self.Parola = self.findChild(QLineEdit, 'lineEdit_parola')
        self.Parola.setEchoMode(QLineEdit.EchoMode.Password)
        self.ParolaTekrar = self.findChild(QLineEdit, 'lineEdit_parolatekrar')
        self.ParolaTekrar.setEchoMode(QLineEdit.EchoMode.Password)
        self.GirisButton = self.findChild(QPushButton, 'btn_giris')
        self.KayitButton = self.findChild(QPushButton, 'btn_kayitol')
        self.GirisButton.clicked.connect(self.loginFunction)
        self.KayitButton.clicked.connect(self.registerFunction)

        self.GirisButton.setStyleSheet("background-color: green; color: white;")
        self.KayitButton.setStyleSheet("""
                    QPushButton {
                        background-color: transparent;
                        color: white;
                        border: 2px solid black;
                        border-radius: 10px;
                        padding: 5px;
                    }
                    QPushButton:hover {
                          background-color: white;
                          color: black;
                    }
                """)
        self.GirisButton.setStyleSheet("""
                           QPushButton {
                               background-color: transparent;
                               color: white;
                               border: 2px solid black;
                               border-radius: 10px;
                               padding: 5px;
                           }
                           QPushButton:hover {
                               background-color: white;
                               color: black;
                           }
                       """)
    def loginFunction(self):
        self.loginform = LoginForm.KullaniciGiris()
        self.loginform.show()
        self.close()

    def registerFunction(self):
        kullanici_adi = self.KullaniciAdi.text().strip()
        parola = self.Parola.text().strip()
        parola_tekrar = self.ParolaTekrar.text().strip()


        veritabani = Veritabanim.Veritabani()
        if kullanici_adi == "" or parola == "" or parola_tekrar == "":
            QMessageBox.warning(self, 'Boş Alanlar', 'Lütfen tüm alanları doldurun.')
            return
        if veritabani.KullaniciEkle(kullanici_adi, parola, parola_tekrar):
            veritabani.VeritabaniniKapat()
            self.loginFunction()

