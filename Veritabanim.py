import sqlite3

from PyQt6.QtWidgets import QMessageBox

import Veritabanim


class Veritabani():
    def __init__(self):
        super().__init__()
        self.connection = sqlite3.connect('kullanicilar.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS kullanicilar
                               (kullanici_adi TEXT, parola TEXT, parolaTekrar TEXT, vki FlOAT)''')

    def KullaniciEkle(self, kullanici_adi, parola, parolaTekrar):

        self.cursor.execute('SELECT kullanici_adi FROM kullanicilar WHERE kullanici_adi=?', (kullanici_adi,))
        if self.cursor.fetchone() is not None:
            QMessageBox.warning(None, 'Kayıt Başarısız', f"'{kullanici_adi}' kullanıcı adı zaten mevcut!")
            return False

        self.cursor.execute('INSERT INTO kullanicilar (kullanici_adi, parola, parolaTekrar) VALUES (?, ?, ?)',
                            (kullanici_adi, parola, parolaTekrar))
        self.connection.commit()
        QMessageBox.information(None, 'Kayıt Başarılı', 'Kullanıcı başarıyla kaydedildi.')
        return True
    def GirisYap(self, kullanici_adi, parola):
        self.cursor.execute('SELECT kullanici_adi FROM kullanicilar WHERE kullanici_adi=? AND parola=?',
                            (kullanici_adi, parola))
        if self.cursor.fetchone() is not None:
            QMessageBox.information(None, 'Giriş Başarılı', 'Giriş Yapıldı.')
            return True
        else:
            QMessageBox.warning(None, 'Giriş Başarısız', 'Kullanıcı adı veya parola yanlış!')
            return False

    def VKICek(self, kullanici_adi):
        self.cursor.execute('SELECT vki FROM kullanicilar WHERE kullanici_adi=?', (kullanici_adi,))
        row = self.cursor.fetchone()
        if row:
            return row[0]
        else:
            return None

    def VKIGuncelle(self, kullanici_adi, vki):
        try:
            self.cursor.execute('UPDATE kullanicilar SET vki=? WHERE kullanici_adi=?', (vki, kullanici_adi))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False
    def VeritabaniniKapat(self):
        self.connection.close()



