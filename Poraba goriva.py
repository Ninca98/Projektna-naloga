# PORABA GORIVA #

import tkinter as tk
from tkinter.font import Font



class GorivoModel:
    def __init__(self):
        self.vnos1 = 0
        self.vnos2 = 0
        self.vnos3 = 0
        self.vnos4 = 0


    def izracun12(self):
        izracunana_poraba = 0
        vnesena_kolicina_goriva = int(self.vnos1)
        vneseni_km = int(self.vnos2)
        if vnesena_kolicina_goriva == 0 and vneseni_km == 0:
            self.izpis12 ='Vnesite vrednosti!'
        elif vnesena_kolicina_goriva == 0 and vneseni_km != 0:
            self.izpis12 ='Vnesite količino goriva!'
        elif vnesena_kolicina_goriva != 0 and vneseni_km == 0:
            self.izpis12 ='Vnesite kilometre!'
        else:
            izracunana_poraba = round(vneseni_km / vnesena_kolicina_goriva , 2)
            self.izpis12 = str(izracunana_poraba)
    
            



class GorivoVmesnik:
    def __init__(self):
        self.gorivo = GorivoModel()
        self.okno = tk.Tk()
         
        
                        
        self.naslov = tk.Label(self.okno, text='PORABA GORIVA')
        self.naslov1 = tk.Label(self.okno, text = 'Količina goriva')
        self.naslov2 = tk.Label(self.okno, text = 'Prevoženi km')
        self.naslov3 = tk.Label(self.okno, text = 'Cena goriva')
        self.naslov4 = tk.Label(self.okno, text = 'Načrtovani km')
        self.naslov12 = tk.Label(self.okno, text = 'Poraba')
        self.naslov34 = tk.Label(self.okno, text = 'Cena vožnje')

        self.enota1 = tk.Label(self.okno, text = 'l')
        self.enota2 = tk.Label(self.okno, text = 'km')
        self.enota3 = tk.Label(self.okno, text = '€/l')
        self.enota4 = tk.Label(self.okno, text = 'km')
        self.enota12 = tk.Label(self.okno, text = 'km/l')
        self.enota34 = tk.Label(self.okno, text = '€')
       
        self.vnos1 = tk.Entry(self.okno, justify = 'center')
        self.vnos2 = tk.Entry(self.okno, justify = 'center')
        self.vnos3 = tk.Entry(self.okno, justify = 'center')
        self.vnos4 = tk.Entry(self.okno, justify = 'center')
        
        self.izpis12 = tk.Entry(justify = 'center')
        self.izpis34 = tk.Entry(justify = 'center')

        self.gumb12 = tk.Button(self.okno, text = '=>', command = self.izracun12())
        self.gumb34 = tk.Button(self.okno, text = '=>') #command = self.izracun34
        
        
        self.naslov.grid(row = 0, column = 0)
        self.naslov1.grid(row = 2, column = 0)
        self.naslov2.grid(row = 6, column = 0)
        self.naslov3.grid(row = 2, column = 8)
        self.naslov4.grid(row = 6, column = 8)
        self.naslov12.grid(row = 4, column = 5)
        self.naslov34.grid(row = 4, column = 13)

        self.enota1.grid(row = 3, column = 1)
        self.enota2.grid(row = 7, column = 1)
        self.enota3.grid(row = 3, column = 9)
        self.enota4.grid(row = 7, column = 9)
        self.enota12.grid(row = 5, column = 6)
        self.enota34.grid(row = 5, column = 14)
                       
        self.vnos1.grid(row = 3, column = 0)
        self.vnos2.grid(row = 7, column = 0)
        self.vnos3.grid(row = 3, column = 8)
        self.vnos4.grid(row = 7, column = 8)

        self.izpis12.grid(row = 5, column = 5)
        self.izpis34.grid(row = 5, column =13)

        self.gumb12.grid(row = 5, column = 3)
        self.gumb34.grid(row = 5, column = 11)



    def izracun12(self):
        self.gorivo.izracun12()


   
GorivoVmesnik()
    
