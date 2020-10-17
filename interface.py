from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from tkinter import filedialog 
   
import  sys,tkinter,re

root = tkinter.Tk()
root.withdraw()
filePath = ""
class VTableEng:
    def __init__(self):
        self.alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890ĄĆĘŁŃÓŚŹŻabcdefghijklmnopqrstuvwxyząćęłńóśźż.,-?\n :"
        #"ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890ĄĆĘŁŃÓŚŹŻ.,-?: "
        self.chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890ĄĆĘŁŃÓŚŹŻabcdefghijklmnopqrstuvwxyząćęłńóśźż.,-?\n :"
        self.table = ["" for i in range(len(self.chars))]
        
    def create(self):
        ran=False
        print("Rozmiar alfabetu: "+ str(len(self.chars))+"\n")
        for i,a in enumerate(self.table):
            
          #  if self.chars[0]=='A' and ran==True:
           #     break
            if self.table[0]=="":
               self.table[i]=self.chars   
              # print(self.table[i]+".\n")
            else:
                ran = True
                c=self.chars[0]
                self.chars =self.chars.replace(c,'')
                self.chars= self.chars+ c
                self.table[i]=self.chars
              #  print(self.table[i]+".\n")
    def encode(self,tekst,kod):
        #tekst=tekst.upper()
        #kod=kod.upper()
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
        #encoded=encoded.upper()
        #kod=kod.upper()
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
                self.setWindowTitle("Encryption Machine")
                #Tytułowy
                titleText = QLabel()
                titleText.setText("This is your Encryption Machine")
                titleText.setAlignment(Qt.AlignCenter)
                titleText.setStyleSheet("QLabel { color : rgb(178,183,187) ;}")
                titleText.setFont(QFont('Capriola',35))

                self.firstText=QLabel()
                self.firstText.setText("Enter message to encrypt")
                self.firstText.setStyleSheet("QLabel { color : rgb(122,193,66) ;}")
                self.firstText.setAlignment(Qt.AlignCenter)
                self.firstText.setFont(QFont('Capriola',20))
                #Pole tekstowe 
                self.firstMessage = QLineEdit()
                self.firstMessage.setPlaceholderText("Enter Message")
                self.firstMessage.setStyleSheet("  background-color : rgb(178,183,187);color : rgb(0,42,92);")
                self.firstMessage.setFont(QFont('Arial',15))
                #Pole klucza
                self.enckey = QLineEdit()
                self.enckey.setPlaceholderText("Enter key")
                self.enckey.setStyleSheet("  background-color : rgb(178,183,187);color : rgb(0,42,92);")
                self.enckey.setFont(QFont('Arial',15))
                #Pole Directory
                self.fDir = QLineEdit()
                self.fDir.setPlaceholderText("File Directory")
                self.fDir.setStyleSheet("  background-color : rgb(178,183,187);color : rgb(0,42,92);")
                self.fDir.setFont(QFont('Arial',15))
                #Pole Zaszyfrowane
                self.encText = QLineEdit()
                self.encText.setPlaceholderText("Encrypted Text")
                self.encText.setStyleSheet("  background-color : rgb(178,183,187);color : rgb(0,42,92);")
                self.encText.setFont(QFont('Arial',15))
                #Pole Odszyfrowane 
                self.decText = QLineEdit()
                self.decText.setPlaceholderText("Decrypted Text")
                self.decText.setStyleSheet("  background-color : rgb(178,183,187);color : rgb(0,42,92);")
                self.decText.setFont(QFont('Arial',15))
              
                #Szyfrowanie
                encryptButton = QPushButton()
                encryptButton.setText("Encrypt")
                encryptButton.clicked.connect(self.encryptClick)
                encryptButton.setFont(QFont('Impact',15))
                encryptButton.setStyleSheet("  background-color : rgb(178,183,187);color : rgb(0,42,92);")
            
                #Deszyfrowanie
                decryptButton = QPushButton()
                decryptButton.setText("Decrypt")
                decryptButton.clicked.connect(self.decryptClick)
                decryptButton.setFont(QFont('Impact',15))
                decryptButton.setStyleSheet("  background-color : rgb(178,183,187);color : rgb(0,42,92);")

                #Wybór pliku
                selectButton = QPushButton()
                selectButton.setText("CHOOSE FILE")
                selectButton.clicked.connect(self.selectClick)
                selectButton.setFont(QFont('Impact',15))
                selectButton.setStyleSheet("  background-color : rgb(178,183,187);color : rgb(0,42,92);")

                #Przycisk zapisu
                saveButton = QPushButton()
                saveButton.setText("Save File")
                saveButton.clicked.connect(self.saveClick)
                saveButton.setFont(QFont('Impact',15))
                saveButton.setStyleSheet("  background-color : rgb(178,183,187);color : rgb(0,42,92);")

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
                encLayout.addWidget(encryptButton)
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
            print("HELP")  

        def encryptClick(self):
            
            if len(self.enckey.text())==0:
                info= QMessageBox.about(self,"Error","Key too short")
            elif len(self.firstMessage.text())==0:
                info= QMessageBox.about(self,"Error","Message too short")
            else:
                self.encText.setText(self.obj.encode(self.firstMessage.text(),self.enckey.text()))
            #enkrypcja

        def decryptClick(self):
           self.decText.setText(self.obj.decode(self.encText.text(),self.enckey.text()))
        
         #znaki spoza alfabetu 
           


        def selectClick(self):
            filePath = filedialog.askopenfilename()
            if(len(filePath)>0):
                self.fDir.setText(filePath)
                f=open(filePath, "r",encoding="utf8")
                self.firstMessage.setText(f.read())
        def saveClick(self):
            d=  self.fDir.text()
            c=len(d)
            if (c<1):
               
                info= QMessageBox.about(self,"Error","Filename is too short")
            elif (d[c-1]=='/'):
                info= QMessageBox.about(self,"Error","Invalid Filename")   
                #Dodać obsługę błędu
            else:
                a=self.firstMessage.text()
                f = open(d, "w")
                f.write(a)
                f.close()
            

#

app = QApplication(sys.argv)

window = Window()
window.setFixedSize(1000,600)
window.setStyleSheet("background-color: rgb(0,42,92);")
#window.setStyleSheet("background-color: pink;")
window.show()

app.exec()
'''Szyfr vigenere'a 
'''

