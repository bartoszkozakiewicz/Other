#App to help me organize my monthly spendings with a use of text files.

from tkinter import Y
import os
import datetime

kwotaPożywienie=KwotaImpreza=KwotaUczelnia=KwotaRozrywka=KwotaAkademik=KwotaBolt=0
selekcja = [kwotaPożywienie,KwotaImpreza,KwotaUczelnia,KwotaRozrywka,KwotaAkademik,KwotaBolt]
sekcje = { 'Pożywienie':kwotaPożywienie , 'Alkohol/Imprezy':KwotaImpreza , 'Okołouczelniane':KwotaUczelnia , "Rozrywka":KwotaRozrywka , "Akademik":KwotaAkademik,"Bolt/Uber":KwotaBolt }
saldo = 1500 
plik = "C:/Users/barto/OneDrive/Pulpit/Wydatki/Październik/Tracker.txt"
plikOblicz = "C:/Users/barto/OneDrive/Dokumenty/JavaScript/oblicz.txt"
data = datetime.date.today()


def running(sekcje, saldo, plik,plikOblicz):

    while True:
 
        kategoria = input("Jeżeli chcesz uzyskać wyciąg wpisz - wyciąg, jeżeli nie to wpisz dokładną nazwę sekcji, w której chcesz dodać wydatki spośród:\nPożywienie\nAlkohol/Imprezy\nOkołouczelniane\nRozrywka\nAkademik\nBolt/Uber\n: ")
        i=0
        x = "cos"
        y = "dupa"
        for wybor in sekcje:
            lista = list((sekcje.keys()))
            if str(kategoria)  == lista[i]:

                KwotaDodana = input("Podaj kwotę w złotówkach: \n")
                selekcja[i] += float(KwotaDodana)
                Opłata = float(KwotaDodana)
                saldo -= Opłata
                Komunikat = "Saldo: {}zł\n".format(saldo)

                if saldo <= 500 and saldo > 0:
                    print("UWAGA, powoli kończą się środki na ten miesiąc!!\n" + Komunikat)
                elif saldo <= 0:
                    print("UWAGA, nie masz już pieniędzy!!\n " + Komunikat)
                elif saldo >500:
                    print(Komunikat) 
                    
                break

            elif str(kategoria) == 'Koniec':
                
                x = "dupa"
                break

            elif str(kategoria) == 'wyciąg':
                
                x = "dupa"
                break
                                

            elif str(kategoria) != 'Koniec' and str(kategoria) != lista[i]: 

                if i < len(lista):
                    pass
                if i == len(lista):
                    break
                
            i+=1
                
            
        print("Aktualna kwota wydanych pieniędzy:\n")
        print("Pożywienie: {}zł".format(selekcja[0]))
        print("Alkohol/Imprezy: {}zł".format(selekcja[1]))
        print("Okołouczelniane: {}zł".format(selekcja[2]))
        print("Rozrywka: {}zł".format(selekcja[3]))
        print("Akademik: {}zł".format(selekcja[4]))
        print("Bolt/Uber: {}zł\n".format(selekcja[5]))

        if x == y:
            break
    

    if os.path.isfile(plikOblicz) and os.path.getsize(plikOblicz) == 0:
        obliczenia = open(plikOblicz, 'w')
        obliczenia.writelines("{}\n".format(0)+"{}\n".format(0)+"{}\n".format(0)+"{}\n".format(0)+"{}\n".format(0)+"{}\n".format(0)+"{}\n".format(1500))
        obliczenia.close()


    if os.path.isfile(plikOblicz):
        listaWydatki = []
        obliczenia = open(plikOblicz,'r')
        wydane = obliczenia.read()
        lines = wydane.split('\n')
        for line in lines:
            listaWydatki.append(line)
        obliczenia.close()

        #Do zapisywania w obliczenia.txt sum
        Pozywienie = selekcja[0]+float(listaWydatki[0])
        Alko = selekcja[1]+float(listaWydatki[1])
        Uczenie = selekcja[2]+float(listaWydatki[2])
        Rozrywka = selekcja[3]+float(listaWydatki[3])
        Akademik = selekcja[4]+float(listaWydatki[4])
        Bolt = selekcja[5]+float(listaWydatki[5])
        SaldoSum = float(listaWydatki[6])-selekcja[0]-selekcja[1]-selekcja[2]-selekcja[3]-selekcja[4]-selekcja[5]
        

        obliczenia = open(plikOblicz,'w')
        obliczenia.writelines("{}\n".format(Pozywienie))
        obliczenia.writelines("{}\n".format(Alko))
        obliczenia.writelines("{}\n".format(Uczenie))
        obliczenia.writelines("{}\n".format(Rozrywka))
        obliczenia.writelines("{}\n".format(Akademik))
        obliczenia.writelines("{}\n".format(Bolt))
        obliczenia.writelines("{}\n".format(SaldoSum))
        obliczenia.close()
        
    if str(kategoria) == "wyciąg" and os.path.isfile(plik):
        tracker = open(plik,'a')
        tracker.writelines("\t\t\t\t\t\t\t\t\t\tWYCIĄG  {}\n\n".format(data))
        tracker.write("Pożywienie: {}zł".format(Pozywienie)+"\nAlkohol/Imprezy: {}zł".format(Alko)+"\nOkołouczelniane: {}zł".format(Uczenie)+"\nRozrywka: {}zł".format(Rozrywka)+"\nAkademik: {}zł".format(Akademik)+"\nBolt/Uber: {}zł\n\n".format(Bolt))

        if SaldoSum <= 500 and SaldoSum > 0:
                tracker.writelines("\t\t\t\t\t\t\t!!UWAGA, powoli kończą się środki na ten miesiąc!!\n" +"\t\t\t\t\t\t\t\t" + "Saldo: {}zł\n".format(SaldoSum))
        elif SaldoSum <= 0:
                tracker.writelines("\t\t\t\t\t\t\t!!UWAGA, nie masz już pieniędzy!!\n\n " +"\t\t\t\t\t\t\t\t"+ "Saldo: {}zł\n".format(SaldoSum))
        elif SaldoSum >500:
                tracker.writelines("Saldo: {}zł\n\n".format(SaldoSum)) 
        tracker.close()      

    elif os.path.isfile(plik) and str(kategoria) != "wyciąg" :
        tracker = open(plik,'a')
        tracker.writelines("\t\t\t\t\t\t\t\t\t\tOPŁATY  {}\n\n".format(data))
        tracker.write("Pożywienie: {}zł".format(selekcja[0])+"\nAlkohol/Imprezy: {}zł".format(selekcja[1])+"\nOkołouczelniane: {}zł".format(selekcja[2])+"\nRozrywka: {}zł".format(selekcja[3])+"\nAkademik: {}zł\n\n".format(selekcja[4])+"\nBolt/Uber: {}zł\n\n".format(Bolt))

        if SaldoSum <= 500 and SaldoSum > 0:
                tracker.writelines("\t\t\t\t\t\t\t!!UWAGA, powoli kończą się środki na ten miesiąc!!\n" +"\t\t\t\t\t\t\t\t" + "Saldo: {}zł\n".format(SaldoSum))
        elif SaldoSum <= 0:
                tracker.writelines("\t\t\t\t\t\t\t!!UWAGA, nie masz już pieniędzy!!\n\n " +"\t\t\t\t\t\t\t\t"+ "Saldo: {}zł\n".format(SaldoSum))
        elif SaldoSum >500:
                tracker.writelines("Saldo: {}zł\n\n".format(SaldoSum)) 

        tracker.close()



running(sekcje,saldo,plik,plikOblicz)