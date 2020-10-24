from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from tkinter import filedialog   
import  sys,tkinter,re,random
root = tkinter.Tk()
root.withdraw()
filePath = ""
class VTableEng:
    def __init__(self):
        self.alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890ĄĆĘŁŃÓŚŹŻabcdefghijklmnopqrstuvwxyząćęłńóśźż.,-?!;()\n :"
        self.chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890ĄĆĘŁŃÓŚŹŻabcdefghijklmnopqrstuvwxyząćęłńóśźż.,-?!;()\n :"
        self.table = ["" for i in range(len(self.chars))]
        
    def create(self):
        print("Rozmiar alfabetu: "+ str(len(self.chars))+"\n")
        for i,a in enumerate(self.table):
            
            if self.table[0]=="":
               self.table[i]=self.chars   
            
            else:
                c=self.chars[0]
                self.chars =self.chars.replace(c,'')
                self.chars= self.chars+ c
                self.table[i]=self.chars
              
    def encode(self,tekst,kod):
       
        while len(tekst)!=len(kod):
            if len(tekst)<len(kod):
                while len(tekst)<len(kod):
                    kod= kod[:-1]
            if len(tekst)>len(kod):
                kod=kod+kod
        encoded=""
        for i in range(len(tekst)): 
            a=tekst[i]
            b=kod[i]
            c=self.table[self.alphabet.find(b)][self.alphabet.find(a)]
            encoded=encoded+c
        return encoded
    def decode(self,encoded,kod):
       
        while len(encoded)!=len(kod):
            if len(encoded)<len(kod):
                while len(encoded)<len(kod):
                    kod= kod[:-1]
            if len(encoded)>len(kod):
                kod=kod+kod
        decoded=""
        for i in range(len(encoded)): 
            a=encoded[i]
            b=kod[i]
            bs=self.alphabet.find(b)
            alp=self.table[bs]
            acs=0        
            c=self.table[0][alp.find(a)]
            decoded=decoded+c
        return decoded
    

class Window(QMainWindow):
        def __init__(self, *args, **kwargs):
                self.obj = VTableEng()
                self.obj.create()
                super(Window, self).__init__(*args, *kwargs)
                self.setWindowTitle("Szyfr Vigenere'a")
                #Tytułowy
                titleText = QLabel()
                titleText.setText("Szyfr Vigenere'a")
                titleText.setAlignment(Qt.AlignCenter)
                titleText.setStyleSheet("QLabel { color : rgb(178,183,187) ;}")
                titleText.setFont(QFont('Capriola',40))

                self.firstText=QLabel()
                self.firstText.setText("Wpisz wiadomość do zaszyfrowania")
                self.firstText.setStyleSheet("QLabel { color : rgb(122,193,66) ;}")
                self.firstText.setAlignment(Qt.AlignCenter)
                self.firstText.setFont(QFont('Capriola',25))
                #Pole tekstowe 
                self.firstMessage = QLineEdit()
                self.firstMessage.setPlaceholderText("Wiadomość")
                self.firstMessage.setStyleSheet("  background-color : rgb(178,183,187);color : rgb(0,42,92);")
                self.firstMessage.setFont(QFont('Arial',15))
                #Pole klucza
                self.enckey = QLineEdit()
                self.enckey.setPlaceholderText("Klucz")
                self.enckey.setStyleSheet("  background-color : rgb(178,183,187);color : rgb(0,42,92);")
                self.enckey.setFont(QFont('Arial',15))
                #Pole Directory
                self.fDir = QLineEdit()
                self.fDir.setPlaceholderText("Ścieżka pliku")
                self.fDir.setStyleSheet("  background-color : rgb(178,183,187);color : rgb(0,42,92);")
                self.fDir.setFont(QFont('Arial',15))
                #Pole Zaszyfrowane
                self.encText = QLineEdit()
                self.encText.setPlaceholderText("Zaszyfrowany tekst")
                self.encText.setStyleSheet("  background-color : rgb(178,183,187);color : rgb(0,42,92);")
                self.encText.setFont(QFont('Arial',15))
                #Pole Odszyfrowane 
                self.decText = QLineEdit()
                self.decText.setPlaceholderText("Odszyfrowany tekst")
                self.decText.setStyleSheet("  background-color : rgb(178,183,187);color : rgb(0,42,92);")
                self.decText.setFont(QFont('Arial',15))
              
                #Szyfrowanie
                encryptButton = QPushButton()
                encryptButton.setText("Szyfruj")
                encryptButton.clicked.connect(self.encryptClick)
                encryptButton.setFont(QFont('Impact',15))
                encryptButton.setStyleSheet("  background-color : rgb(178,183,187);color : rgb(0,42,92);")
            
                #Deszyfrowanie
                decryptButton = QPushButton()
                decryptButton.setText("Odszyfruj")
                decryptButton.clicked.connect(self.decryptClick)
                decryptButton.setFont(QFont('Impact',15))
                decryptButton.setStyleSheet("  background-color : rgb(178,183,187);color : rgb(0,42,92);")

                #Wybór pliku
                selectButton = QPushButton()
                selectButton.setText("Wybierz plik")
                selectButton.clicked.connect(self.selectClick)
                selectButton.setFont(QFont('Impact',15))
                selectButton.setStyleSheet("  background-color : rgb(178,183,187);color : rgb(0,42,92);")

                #Przycisk zapisu
                saveButton = QPushButton()
                saveButton.setText("Zapisz Plik")
                saveButton.clicked.connect(self.saveClick)
                saveButton.setFont(QFont('Impact',15))
                saveButton.setStyleSheet("  background-color : rgb(178,183,187);color : rgb(0,42,92);")

                #Przycisk zapisu
                readEncButton = QPushButton()
                readEncButton.setText("Zaszyfrowany tekst")
                readEncButton.clicked.connect(self.openEncrypted)
                readEncButton.setFont(QFont('Impact',15))
                readEncButton.setStyleSheet("  background-color : rgb(178,183,187);color : rgb(0,42,92);")

                #Help button
                self.helpButton = QPushButton()
                self.helpButton.setText("( i )")
                self.helpButton.clicked.connect(self.helpClick)
                self.helpButton.setFont(QFont('Impact',15))
                self.helpButton.setStyleSheet("  background-color : rgb(178,183,187);color : rgb(0,42,92);")
                
                helpLayout = QHBoxLayout()
                helpLayout.addWidget(self.helpButton)
                helpLayout.setAlignment(Qt.AlignLeft)
                helpLayoutW = QWidget()
                helpLayoutW.setLayout(helpLayout)


                #Layout przycisku Wyboru pliku
                selectLayout = QHBoxLayout()
                selectLayout.addWidget(selectButton)
                selectLayout.addWidget(self.firstMessage)
                selectLayoutW = QWidget()
                selectLayoutW.setLayout(selectLayout)

                #Layout pola wiadomości i klucza
                textLayout1 = QHBoxLayout()
                textLayout1.addWidget(encryptButton)
                textLayout1.addWidget(self.enckey)
                textLayoutWid1=QWidget()
                textLayoutWid1.setLayout(textLayout1)

                #Layout przycisków enkrypcji i dekrypcji
                decLayout1= QHBoxLayout()
                decLayout1.addWidget(decryptButton)
                decLayout1.addWidget(self.decText)
                decLayWid1= QWidget()
                decLayWid1.setLayout(decLayout1)

                #Layout directory 
                dirLayout= QHBoxLayout()
                dirLayout.addWidget(saveButton)
                dirLayout.addWidget(self.fDir)
                
                dirLayout.setAlignment(Qt.AlignCenter)
                dirLayWid=QWidget()
                dirLayWid.setLayout(dirLayout)
                #Layout Zaszyfrowanego i szyfruj
                encLayout= QHBoxLayout()
                encLayout.addWidget(readEncButton)
                encLayout.addWidget(self.encText)
                encLayoutWid1= QWidget()
                encLayoutWid1.setLayout(encLayout)
                     
                mainMenu = QVBoxLayout()
               
                mainMenu.addWidget(helpLayoutW)
                mainMenu.setAlignment(Qt.AlignCenter)
                mainMenu.addWidget(titleText)
                mainMenu.addWidget(self.firstText)
                mainMenu.addWidget(selectLayoutW)
               
                mainMenu.addWidget(dirLayWid)
                mainMenu.addWidget(textLayoutWid1)
                mainMenuWid= QWidget()
                mainMenuWid.setLayout(mainMenu)
                mainMenu.addWidget(encLayoutWid1)
                mainMenu.addWidget(decLayWid1)
                
                self.setCentralWidget(mainMenuWid)

   
        def helpClick(self):    
            info= QMessageBox()
            info.setWindowTitle("Info")
            info.setStyleSheet("QMessageBox{background-color : white}")
            info.setText("Autor: Krzysztof Sułkowski\nIndeks: 140785\n\nAlgorytm Vigenere'a\nAlgorytm Vigenere'a jest algorytmem z grupy algorytmów polialfabetycznych. Prezentowany program opiera się na algorytmie szyfrowania opartym na tablicy. \nPrzykładowa tablica: \n\n\t A B C D E \tSzyfrowane hasło: B A C A\n\t B C D E A \tKlucz szyfrowania: C E D E \n\t C D E A B \tZaszyfrowane hasło: D E A E\n\t D E A B C\n\t E A B C D"+
            "\n\nW poziomie wyszukiwany jest kolejno każdy znak szyfrowanego hasła. W pionie wyszukiwany jest kolejno każdy znak szyfru. Zaszyfrowane hasło powstaje w wyniku odczytania znaków znajdujących się w miejscu przecięcia odpowiadających sobie znaków hasła i klucza. \n\nZaimplementowany program pozwala na wpisanie treści wiadomości lub wczytanie jej z pliku tekstowego. Klucz szyfrowania można wpisać ręcznie lub wygenerować go automatycznie. Zaszyfrowane hasło można zapisać do pliku tekstowego. Alfabet obejmuje małe i wielkie litery alfabetu polskiego, cyfry oraz podstawowe znaki interpunkcyjne.")  
           # info.setFont(QFont("Arial",13))
            info.exec_()              
        def encryptClick(self):
            
            if len(self.enckey.text())==0:
                info= QMessageBox()
                info.setWindowTitle("Błąd")
                info.setText("Zbyt krótki klucz. Wygenerować nowy?")
                info.setStyleSheet("QMessageBox{background-color : white}")
                info.addButton("Generuj", QMessageBox.YesRole) 
                info.addButton("Anuluj", QMessageBox.NoRole)
                #info.question(self, 'Błąd klucza', "Niepoprawny klucz. Wygenerować nowy?", info.Yes | info.No, info.No)
                result=info.exec()
                if result==0:
                    print("Hello")
                    self.enckey.setText(self.randomKey(self.obj.alphabet))
                

            elif len(self.firstMessage.text())==0:
                info= QMessageBox()
                info.setWindowTitle("Błąd")
                info.setText("Wiadomość za krótka")
                info.setStyleSheet("QMessageBox{background-color : white}")
                info.exec()
                
            else:
                text=self.enckey.text()
                ran=True
                for i in range (len(text)):
                    if text[i] not in self.obj.alphabet:
                        info= QMessageBox()
                        info.setWindowTitle("Błąd")
                        info.setText("Błędny alfabet klucza.")
                        info.setStyleSheet("QMessageBox{background-color : white}")
                        info.exec()
                        ran=False
                        break
                       
                text=self.firstMessage.text()
                for i in range (len(text)):
                    if text[i] not in self.obj.alphabet:
                        info= QMessageBox()
                        info.setWindowTitle("Błąd")
                        info.setText("Błędny alfabet wiadomości.")
                        info.setStyleSheet("QMessageBox{background-color : white}")
                        info.exec()
                        ran=False
                        break
                        
                if ran==True:
                    self.encText.setText(self.obj.encode(self.firstMessage.text(),self.enckey.text()))         
        def randomKey(self,alphabet):
            key=""
            for i in range(10):
                key=key+alphabet[random.randint(0,len(alphabet))]
            return key   
        def decryptClick(self):
           self.decText.setText(self.obj.decode(self.encText.text(),self.enckey.text()))
        def selectClick(self):
            filePath = filedialog.askopenfilename()
            if(len(filePath)>0):
                self.fDir.setText(filePath)
                f=open(filePath, "r",encoding="utf8")
                self.firstMessage.setText(f.read())
                f.close()
        def saveClick(self):
            d=  self.fDir.text()
            c=len(d)
            if (c<1):
                info= QMessageBox()
                info.setWindowTitle("Błąd")
                info.setText("Niepoprawna nazwa pliku")
                info.setStyleSheet("QMessageBox{background-color : white}")
                info.exec()
            elif (d[c-1]=='/'):
                info= QMessageBox()
                info.setWindowTitle("Błąd")
                info.setText("Niepoprawna nazwa pliku ")
                info.setStyleSheet("QMessageBox{background-color : white}")
                info.exec()
            else:
                a=self.encText.text()
                f = open(d, "w",encoding="utf8")
                f.write(a)
                f.close()
        def openEncrypted(self):
            filePath = filedialog.askopenfilename()
            if(len(filePath)>0):
                f=open(filePath, "r",encoding="utf8")
                self.encText.setText(f.read())
                f.close()
        
#

app = QApplication(sys.argv)

window = Window()
window.setFixedSize(900,500)
window.setStyleSheet("background-color: rgb(0,42,92);")
#window.setStyleSheet("background-color: pink;")
window.show()

app.exec()


