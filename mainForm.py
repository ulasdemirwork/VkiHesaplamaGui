import sys
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QMessageBox
from PyQt6 import uic

import Veritabanim

class MainGorev(QMainWindow):
    def __init__(self, kullanici_adi, vki):
        super(MainGorev, self).__init__()
        self.kullanici_adi = kullanici_adi
        self.vki = vki
        self.initUI()

    def initUI(self):
        self.setWindowIcon(QIcon("image/icon.jpg"))

        background_label = QLabel(self)
        background_label.setGeometry(0, 0, 800, 600)
        pixmap = QPixmap('image/icon.jpg')
        background_label.setPixmap(pixmap)
        background_label.setScaledContents(True)

        uic.loadUi('Forms/mainForm.ui', self)

        self.boy = self.findChild(QLineEdit, 'lineEdit_boy')
        self.kilo = self.findChild(QLineEdit, 'lineEdit_kilo')
        self.vkiGonder = self.findChild(QPushButton, 'btn_gonder')

        # Hangi widget'in None olduğunu belirlemek için print ifadeleri ekleyelim
        print(f"self.boy: {self.boy}")
        print(f"self.kilo: {self.kilo}")
        print(f"self.vkiGonder: {self.vkiGonder}")

        self.vkiGonder.clicked.connect(self.vkiFunction)

        self.label_kullanici_adi = self.findChild(QLabel, 'label_kullanici_adi')
        self.label_vki = self.findChild(QLabel, 'label_vki')

        if self.label_kullanici_adi:
            self.label_kullanici_adi.setText(f"Hoş geldiniz, {self.kullanici_adi}")

        if self.vki is None:
            self.label_vki.setText("Veri Girilmesi Gerekli")
        else:
            self.label_vki.setText(f"VKİ: {self.vki}")

    def vkiFunction(self):
        try:
            boy_text = self.boy.text().strip()
            kilo_text = self.kilo.text().strip()

            if not boy_text or not kilo_text:
                raise ValueError("Boy ve kilo alanları boş bırakılamaz.")

            boy = float(boy_text)
            kilo = float(kilo_text)

            if boy <= 0 or kilo <= 0:
                raise ValueError("Boy ve kilo pozitif sayılar olmalıdır.")

            vki = kilo / (boy / 100) ** 2

            veritabani = Veritabanim.Veritabani()
            if veritabani.VKIGuncelle(self.kullanici_adi, vki):
                self.label_vki.setText(f"VKİ: {vki:.2f}")
                QMessageBox.information(self, 'Başarılı', 'VKİ güncellendi.')
            else:
                QMessageBox.warning(self, 'Hata', 'VKİ güncellenemedi.')

        except ValueError as e:
            QMessageBox.warning(self, 'Hata', str(e))
            return  # Hata durumunda fonksiyondan çık

        except Exception as e:
            QMessageBox.critical(self, 'Hata', f"Beklenmedik bir hata oluştu: {str(e)}")
            return
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainGorev("user", 0)
    window.show()
    sys.exit(app.exec())
