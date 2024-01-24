import random
from tkinter import *

class Finestra():
    def __init__(self):
        self.root = Tk()
        self.root.title('Generatore Password 1.0')
        self.root.geometry("300x70")
        self.root.resizable(False, False)
        self.root.iconbitmap("img/favicon/fav.ico")
        
        self.entry_password = Entry(self.root, justify='center', width=25)
        self.entry_password.grid(row=0, column=0, padx=10, pady=10)
        
        self.button_password = Button(self.root, text="Genera Password", command=self.genera)
        self.button_password.grid(row=0, column=1, padx=10, pady=10)
        
        self.root.mainloop()
    
    def genera(self):
        self.entry_password.delete(0, END)
        tupla = ('a','b','c','d','e','f','g','h','i','l','m','n','o','p','q','r','s','t','u','v','z',
                 'A','B','C','D','E','F','G','H','I','L','M','N','O','P','Q','R','S','T','U','V','Z',
                 'w','y','j','k','x','w','Y','K','X','W',
                 '1','2','3','4','5','6','7','8','9','0')
        stringa = ""

        for _ in range(16):
            i = random.choice(tupla)
            stringa = stringa + i
            print(i, end='')
        self.entry_password.insert(0, stringa)
    
f = Finestra()

