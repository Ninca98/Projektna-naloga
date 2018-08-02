# PORABA GORIVA #

import tkinter as tk
from tkinter.font import Font
from tkinter import *



# Funkcija, ki pove, ali so v vnosnem polju samo števila in vejice oz. pike.
def ali_so_samo_stevila(vnos):
    # Najprej preverimo, koliko pik in vejic je v zapisu.
    vpisan_niz = str(vnos)
    stevec_vejic_in_pik = 0
    for element in vpisan_niz:
        if element == ',' or element == '.':
            stevec_vejic_in_pik += 1
        
    #Če v zapisu ni vejic/pik ali pa je samo 1, nadaljujemo s funkcijo.
    if stevec_vejic_in_pik <= 1:
        vpisan_niz_znakov = str(vnos).replace(',', '').replace('.', '')
        vpisan_seznam = list(vpisan_niz_znakov)
        for element in vpisan_seznam:
            if element not in {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}.values():
                return False
        return True
    
    # Če je v zapisu več kot 1 vejica/pika, funkcija vrne False.
    else:
        return False




class GorivoModel:
    def __init__(self, vmesnik):
        self.vnos1 = vmesnik.vnos1
        self.vnos2 = vmesnik.vnos2
        self.vnos3 = vmesnik.vnos3
        self.vnos4 = vmesnik.vnos4
        self.izpis12 = vmesnik.izpis12
        self.izpis34 = vmesnik.izpis34


    def izracun12(self):
        izracunana_poraba = 0

        # Najprej preverimo, ali so v vnosnih poljih samo števila.
        if ali_so_samo_stevila(self.vnos1.get()) and ali_so_samo_stevila(self.vnos2.get()):
            # Če je napisana dec. vejica, jo zamenjamo s piko.
            vnos1 = self.vnos1.get().replace(',', '.')
            vnos2 = self.vnos2.get().replace(',', '.')
            vnesena_kolicina_goriva = float(vnos1)
            vneseni_km = float(vnos2)
        
            if vnesena_kolicina_goriva == 0 and vneseni_km == 0:
                self.izpis12.delete(0, tk.END)
                self.izpis12.insert(0,'Vnesite vrednosti!')
                
            elif vnesena_kolicina_goriva == 0 and vneseni_km != 0:
                self.izpis12.delete(0, tk.END)
                self.izpis12.insert(0, 'Vnesite količino goriva!')
                
            elif vnesena_kolicina_goriva != 0 and vneseni_km == 0:
                self.izpis12.delete(0, tk.END)
                self.izpis12.insert(0, 'Vnesite kilometre!')
        
            else:           
                izracunana_poraba = round(vneseni_km / vnesena_kolicina_goriva , 4)
                self.izpis12.delete(0, tk.END)
                self.izpis12.insert(0, str(izracunana_poraba))

        # Če niso samo števila, funkcija vrne 'Neveljaven vnos'.        
        else:
            self.izpis12.delete(0, tk.END)
            self.izpis12.insert(0, 'Neveljaven vnos!')



    def izracun34(self):
        izracunana_cena = 0

        # Najprej preverimo, če je poraba sploh izračunana.
        if self.izpis12.get() in ['Vnesite vrednosti!', 'Vnesite količino goriva!', 'Vnesite kilometre!', 'Neveljaven vnos!']:
            self.izpis34.delete(0, tk.END)
            self.izpis34.insert(0, 'Izračunajte porabo!')

##        # Preverimo, če je poraba slučajno 0.
##        elif self.izpis12.get() == 0:
##            self.izpis34.delete(0, tk.END)
##            self.izpis34.insert(0, 'Izračunajte porabo!')

        # V primeru, da je poraba izračunana, nadaljujemo s funkcijo.
        else:
            poraba = float(self.izpis12.get())
            if ali_so_samo_stevila(self.vnos3.get()) and ali_so_samo_stevila(self.vnos4.get()):  
                vnos3 = self.vnos3.get().replace(',', '.')
                vnos4 = self.vnos4.get().replace(',', '.')
                vnesena_cena_goriva = float(vnos3)
                vneseni_nacrtovani_km = float(vnos4)
            
        
                if vnesena_cena_goriva == 0 and vneseni_nacrtovani_km == 0:
                    self.izpis34.delete(0, tk.END)
                    self.izpis34.insert(0,'Vnesite vrednosti!')
                    
                elif vnesena_cena_goriva == 0 and vneseni_nacrtovani_km != 0:
                    self.izpis34.delete(0, tk.END)
                    self.izpis34.insert(0, 'Vnesite ceno goriva!')
                    
                elif vnesena_cena_goriva != 0 and vneseni_nacrtovani_km == 0:
                    self.izpis34.delete(0, tk.END)
                    self.izpis34.insert(0, 'Vnesite načrtovane km!')
            
                else:           
                    izracunana_cena = round((vnesena_cena_goriva * vneseni_nacrtovani_km) / poraba , 2)
                    self.izpis34.delete(0, tk.END)
                    self.izpis34.insert(0, str(izracunana_cena))

            # Če niso samo števila, vrne 'Neveljaven vnos'.    
            else:
                self.izpis34.delete(0, tk.END)
                self.izpis34.insert(0, 'Neveljaven vnos!')


                


class GorivoVmesnik:
    def __init__(self):
        self.okno = tk.Tk()
        self.okno.title('Poraba goriva')
        self.okvir12 = tk.Frame()
        #self.okvir34 = tk.Frame()
        #self.okvir_skupen = tk.Frame()
        self.okvir_zgo = tk.Frame()

        self.okvir12.pack()#side = LEFT)
        #self.okvir34.pack(side = RIGHT)
        #self.okvir_skupen.pack()
        self.okvir_zgo.pack(side = BOTTOM)
        
                                       
        self.naslov1 = tk.Label(self.okvir12, text = 'Količina goriva')
        self.naslov2 = tk.Label(self.okvir12, text = 'Prevoženi km')
        self.naslov3 = tk.Label(self.okvir12, text = 'Cena goriva')
        self.naslov4 = tk.Label(self.okvir12, text = 'Načrtovani km')
        self.naslov12 = tk.Label(self.okvir12, text = 'Poraba')
        self.naslov34 = tk.Label(self.okvir12, text = 'Cena vožnje')
        self.naslov_zgo = tk.Label(self.okvir_zgo, text = 'Zgodovina vnosov') #justify = 'left'

        self.enota1 = tk.Label(self.okvir12, text = 'l')
        self.enota2 = tk.Label(self.okvir12, text = 'km')
        self.enota3 = tk.Label(self.okvir12, text = '€/l')
        self.enota4 = tk.Label(self.okvir12, text = 'km')
        self.enota12 = tk.Label(self.okvir12, text = 'km/l')
        self.enota34 = tk.Label(self.okvir12, text = '€')
       
        self.vnos1 = tk.Entry(self.okvir12, justify = 'center', bd = 3, width = 18)
        self.vnos2 = tk.Entry(self.okvir12, justify = 'center', bd = 3, width = 18)
        self.vnos3 = tk.Entry(self.okvir12, justify = 'center', bd = 3, width = 18)
        self.vnos4 = tk.Entry(self.okvir12, justify = 'center', bd = 3, width = 18)
        
        self.izpis12 = tk.Entry(self.okvir12, justify = 'center', bd = 5, width = 25)
        self.izpis34 = tk.Entry(self.okvir12, justify = 'center', bd = 5, width = 25)

        self.gumb12 = tk.Button(self.okvir12, text = '=>', command = self.izracun12, bd = 3, width = 4)
        self.gumb34 = tk.Button(self.okvir12, text = '=>', command = self.izracun34, bd = 3, width = 4)
        

       
        self.naslov1.grid(row = 2, column = 0)
        self.naslov2.grid(row = 6, column = 0)
        self.naslov3.grid(row = 2, column = 8)
        self.naslov4.grid(row = 6, column = 8)
        self.naslov12.grid(row = 4, column = 5)
        self.naslov34.grid(row = 4, column = 13)
        self.naslov_zgo.grid(row = 8, column = 0)

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


        self.gorivo = GorivoModel(self)
        self.okno.mainloop()


    # Fukcija izračuna porabo na 4 dec. mesta iz količine goriva ter prevoženih km.          
    def izracun12(self):
        self.gorivo.izracun12()


    # Funkcija izračuna ceno načrtovane poti na 2 dec. mesti iz cene goriva, načrtovanih km te iz že prej izračunane porabe
    def izracun34(self):
        self.gorivo.izracun34()


   
GorivoVmesnik()
    
