import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from LoginForm import KullaniciGiris

if __name__ == '__main__':

    app = QApplication(sys.argv)
    form = KullaniciGiris()
    form.show()
    sys.exit(app.exec())
