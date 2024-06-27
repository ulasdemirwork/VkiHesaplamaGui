from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLabel, QMessageBox
from PyQt6 import uic
import RegisterForm
import Veritabanim
import mainForm


class KullaniciGiris(QMainWindow):
    def __init__(self):
        super(KullaniciGiris, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowIcon(QIcon("image/icon.jpg"))

        background_label = QLabel(self)
        background_label.setGeometry(0, 0, 800, 600)
        pixmap = QPixmap('image/icon.jpg')

        background_label.setPixmap(pixmap)
        background_label.setScaledContents(True)



        uic.loadUi('Forms/loginForm.ui', self)
        self.KullaniciAdi = self.findChild(QLineEdit, 'lineEdit_kullaniciadi')
        self.Parola = self.findChild(QLineEdit, 'lineEdit_parola')
        self.Parola.setEchoMode(QLineEdit.EchoMode.Password)
        self.GirisButton = self.findChild(QPushButton, 'btn_giris')
        self.KayitButton = self.findChild(QPushButton, 'btn_kayitol')
        self.GirisButton.clicked.connect(self.loginFunction)
        self.KayitButton.clicked.connect(self.openRegisterForm)


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
        # Kullanıcı kayıt işlemi
        kullanici_adi = self.KullaniciAdi.text().strip()
        parola = self.Parola.text().strip()

        if kullanici_adi == "" or parola == "":
            QMessageBox.warning(self, 'Boş Alanlar', 'Lütfen tüm alanları doldurun.')
            return
        veritabani = Veritabanim.Veritabani()
        if veritabani.GirisYap(kullanici_adi, parola):
            vki = veritabani.VKICek(kullanici_adi)  # VKİ değerini veritabanından çek

            self.mainform = mainForm.MainGorev(kullanici_adi,vki)
            self.mainform.show()
            self.close()
        else:
            return

    def openRegisterForm(self):
        try:
            self.registerForm = RegisterForm.KullaniciKayit()
            self.registerForm.show()
            self.close()
        except Exception as e:
            QMessageBox.critical(self, 'Hata', f'Kayıt formu açılamadı: {str(e)}')