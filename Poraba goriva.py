# PORABA GORIVA #

import tkinter as tk
from tkinter.font import Font



# Funkcija, ki pove, ali so v vnosnem polju samo števila in vejice oz. pike.
def ali_so_samo_stevila(vnos):
    vpisan_niz = str(vnos).replace(',', '').replace('.', '')
    vpisan_seznam = list(vpisan_niz)
    for element in vpisan_seznam:
        if element not in {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}.values():
            return False
    return True




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
        if ali_so_samo_stevila(self.vnos1.get()) == True and ali_so_samo_stevila(self.vnos2.get()) == True:
            # Če je napisana dec. vejica, jo zamenjamo s piko.
            if ',' in self.vnos1.get() or ',' in self.vnos2.get():
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

            # Tu je napisana dec. pika, zato ni potrebno popravljati vnosa.
            else:
                vnesena_kolicina_goriva = float(self.vnos1.get())
                vneseni_km = float(self.vnos2.get())
                
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
            if ali_so_samo_stevila(self.vnos3.get()) == True and ali_so_samo_stevila(self.vnos4.get()) == True:
                if ',' in self.vnos3.get() or ',' in self.vnos4.get():
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
                        self.izpis34.insert(0, 'Vnesite nacrtovane kilometre!')
                
                    else:           
                        izracunana_cena = round((vnesena_cena_goriva * vneseni_nacrtovani_km) / poraba , 2)
                        self.izpis34.delete(0, tk.END)
                        self.izpis34.insert(0, str(izracunana_cena))

                else:
                    vnesena_cena_goriva = float(self.vnos3.get())
                    vneseni_nacrtovani_km = float(self.vnos4.get())
                    
                    if vnesena_cena_goriva == 0 and vneseni_nacrtovani_km == 0:
                        self.izpis34.delete(0, tk.END)
                        self.izpis34.insert(0,'Vnesite vrednosti!')
                        
                    elif vnesena_cena_goriva == 0 and vneseni_nacrtovani_km != 0:
                        self.izpis34.delete(0, tk.END)
                        self.izpis34.insert(0, 'Vnesite ceno goriva!')
                        
                    elif vnesena_cena_goriva != 0 and vneseni_nacrtovani_km == 0:
                        self.izpis34.delete(0, tk.END)
                        self.izpis34.insert(0, 'Vnesite nacrtovane kilometre!')
                
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
        #self.gorivo = GorivoModel(self)
        # ???????.title('Poraba goriva')
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

        self.gumb12 = tk.Button(self.okno, text = '=>', command = self.izracun12)
        self.gumb34 = tk.Button(self.okno, text = '=>', command = self.izracun34)
        
        
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

        self.okno.mainloop()


    # Fukcija izračuna porabo na 4 dec. mesta iz količine goriva ter prevoženih km.          
    def izracun12(self):
        self.gorivo = GorivoModel(self)
        self.gorivo.izracun12()


    # Funkcija izračuna ceno načrtovane poti na 2 dec. mesti iz cene goriva, načrtovanih km te iz že prej izračunane porabe
    def izracun34(self):
        self.gorivo = GorivoModel(self)
        self.gorivo.izracun34()


   
GorivoVmesnik()
    
