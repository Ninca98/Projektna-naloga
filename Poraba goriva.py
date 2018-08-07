# PORABA GORIVA #

import tkinter as tk
# from tkinter.font import Font
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


    def izracun12(self, prvi_vnos, drugi_vnos):
        izracunana_poraba = 0

        # Najprej preverimo, ali so v vnosnih poljih samo števila.
        if ali_so_samo_stevila(prvi_vnos) and ali_so_samo_stevila(drugi_vnos):
            # Če je napisana dec. vejica, jo zamenjamo s piko.          
            vnesena_kolicina_goriva = float(prvi_vnos.replace(',', '.'))
            vneseni_km = float(drugi_vnos.replace(',', '.'))
        
            if vnesena_kolicina_goriva == 0 and vneseni_km == 0:
                return 'Vnesite vrednosti!'
                
            elif vnesena_kolicina_goriva == 0 and vneseni_km != 0:
                return 'Vnesite količino goriva!'
                
            elif vnesena_kolicina_goriva != 0 and vneseni_km == 0:
               return 'Vnesite kilometre!'
        
            else:           
                izracunana_poraba = round(vneseni_km / vnesena_kolicina_goriva , 4)
                return str(izracunana_poraba)


        # Če niso samo števila, funkcija vrne 'Neveljaven vnos'.        
        else:
            return 'Neveljaven vnos!'



    def izracun34(self, poraba, tretji_vnos, cetrti_vnos):
        izracunana_cena = 0

        # Najprej preverimo, če je poraba sploh izračunana.
        if poraba in ['Vnesite vrednosti!', 'Vnesite količino goriva!', 'Vnesite kilometre!', 'Neveljaven vnos!']:
            return 'Izračunajte porabo!'

##        # Preverimo, če je poraba slučajno 0.
##        elif self.izpis12.get() == 0:
##            self.izpis34.delete(0, tk.END)
##            self.izpis34.insert(0, 'Izračunajte porabo!')

        # V primeru, da je poraba izračunana, nadaljujemo s funkcijo.
        else:
            stevilska_poraba = float(poraba)
            if ali_so_samo_stevila(tretji_vnos) and ali_so_samo_stevila(cetrti_vnos):  
                vnesena_cena_goriva = float(tretji_vnos.replace(',', '.'))
                vneseni_nacrtovani_km = float(cetrti_vnos.replace(',', '.'))
            
        
                if vnesena_cena_goriva == 0 and vneseni_nacrtovani_km == 0:
                    return'Vnesite vrednosti!'
                    
                elif vnesena_cena_goriva == 0 and vneseni_nacrtovani_km != 0:
                    return 'Vnesite ceno goriva!'
                    
                elif vnesena_cena_goriva != 0 and vneseni_nacrtovani_km == 0:
                    return 'Vnesite načrtovane km!'
            
                else:           
                    izracunana_cena = round((vnesena_cena_goriva * vneseni_nacrtovani_km) / stevilska_poraba , 2)
                    return str(izracunana_cena)

            # Če niso samo števila, vrne 'Neveljaven vnos'.    
            else:
                return 'Neveljaven vnos!'


                


class GorivoVmesnik:
    def __init__(self):
        self.okno = tk.Tk()
        self.okno.title('Poraba goriva')
        self.okvir_vnos = tk.Frame()
        self.okvir_zgo = tk.Frame()

        self.okvir_vnos.pack()
        self.okvir_zgo.pack(side = BOTTOM)
        
                                       
        self.naslov1 = tk.Label(self.okvir_vnos, text = 'Količina goriva')
        self.naslov2 = tk.Label(self.okvir_vnos, text = 'Prevoženi km')
        self.naslov3 = tk.Label(self.okvir_vnos, text = 'Cena goriva')
        self.naslov4 = tk.Label(self.okvir_vnos, text = 'Načrtovani km')
        self.naslov12 = tk.Label(self.okvir_vnos, text = 'Poraba')
        self.naslov34 = tk.Label(self.okvir_vnos, text = 'Cena vožnje')
        self.naslov_zgo = tk.Label(self.okvir_zgo, text = 'Zgodovina vnosov')

        self.enota1 = tk.Label(self.okvir_vnos, text = 'l')
        self.enota2 = tk.Label(self.okvir_vnos, text = 'km')
        self.enota3 = tk.Label(self.okvir_vnos, text = '€/l')
        self.enota4 = tk.Label(self.okvir_vnos, text = 'km')
        self.enota12 = tk.Label(self.okvir_vnos, text = 'km/l')
        self.enota34 = tk.Label(self.okvir_vnos, text = '€')
       
        self.vnos1 = tk.Entry(self.okvir_vnos, justify = 'center', bd = 3, width = 18)
        self.vnos2 = tk.Entry(self.okvir_vnos, justify = 'center', bd = 3, width = 18)
        self.vnos3 = tk.Entry(self.okvir_vnos, justify = 'center', bd = 3, width = 18)
        self.vnos4 = tk.Entry(self.okvir_vnos, justify = 'center', bd = 3, width = 18)
        
        self.izpis12 = tk.Entry(self.okvir_vnos, justify = 'center', bd = 5, width = 25)
        self.izpis34 = tk.Entry(self.okvir_vnos, justify = 'center', bd = 5, width = 25)

        self.gumb12 = tk.Button(self.okvir_vnos, text = '=>', command = self.izracun12, bd = 3, width = 4)
        self.gumb34 = tk.Button(self.okvir_vnos, text = '=>', command = self.izracun34, bd = 3, width = 4)
        
       
        self.naslov1.grid(row = 1, column = 1)
        self.naslov2.grid(row = 5, column = 1)
        self.naslov3.grid(row = 1, column = 9)
        self.naslov4.grid(row = 5, column = 9)
        self.naslov12.grid(row = 3, column = 6)
        self.naslov34.grid(row = 3, column = 14)
        self.naslov_zgo.pack()

        self.enota1.grid(row = 2, column = 2)
        self.enota2.grid(row = 6, column = 2)
        self.enota3.grid(row = 2, column =10)
        self.enota4.grid(row = 6, column = 10)
        self.enota12.grid(row = 4, column = 7)
        self.enota34.grid(row = 4, column = 15)
                       
        self.vnos1.grid(row = 2, column = 1)
        self.vnos2.grid(row = 6, column = 1)
        self.vnos3.grid(row = 2, column = 9)
        self.vnos4.grid(row = 6, column = 9)

        self.izpis12.grid(row = 4, column = 6)
        self.izpis34.grid(row = 4, column =14)

        self.gumb12.grid(row = 4, column = 4)
        self.gumb34.grid(row = 4, column = 12)

        self.okvir_vnos.grid_columnconfigure(0, minsize = 10)
        self.okvir_vnos.grid_columnconfigure(5, minsize = 5)
        self.okvir_vnos.grid_columnconfigure(8, minsize = 80)
        self.okvir_vnos.grid_columnconfigure(13, minsize = 5)
        self.okvir_vnos.grid_columnconfigure(15, minsize = 20)
        self.okvir_vnos.grid_rowconfigure(0, minsize = 10)
        self.okvir_vnos.grid_rowconfigure(7, minsize = 25)


        self.gorivo = GorivoModel(self)
        self.okno.mainloop()


    # Fukcija izračuna porabo na 4 dec. mesta iz količine goriva ter prevoženih km.          
    def izracun12(self):
        rezultat12 = self.gorivo.izracun12(self.vnos1.get(), self.vnos2.get())
        self.izpis12.delete(0, tk.END)
        self.izpis12.insert(0, rezultat12)

        if ali_so_samo_stevila(rezultat12):
            self.izpis_zgo = tk.Label(self.okvir_zgo, text='Količina goriva: {0} l,   prevoženi km: {1} km,   poraba: {2} km/l.'.format(self.vnos1.get(), self.vnos2.get(), self.izpis12.get()))
            self.izpis_zgo.pack()
            


    # Funkcija izračuna ceno načrtovane poti na 2 dec. mesti iz cene goriva, načrtovanih km te iz že prej izračunane porabe
    def izracun34(self):
        rezultat34 = self.gorivo.izracun34(self.izpis12.get(), self.vnos3.get(), self.vnos4.get())
        self.izpis34.delete(0, tk.END)
        self.izpis34.insert(0, rezultat34)

        if ali_so_samo_stevila(rezultat34):
            self.izpis_zgo = tk.Label(self.okvir_zgo, text='Poraba: {0} km/l,   cena goriva: {1} €,   načrtovani km: {2} km,   cena vožnje: {3} €.'.format(self.izpis12.get(), self.vnos3.get(), self.vnos4.get(), self.izpis34.get()))
            self.izpis_zgo.pack()


   
GorivoVmesnik()
    
