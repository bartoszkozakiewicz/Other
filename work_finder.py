import lxml
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
import locale

def job_searching(skillsy):

    oferty = []
    #Pobieranie wartości ze strony pracuj.pl
    html_text = requests.get("https://www.pracuj.pl/praca/data%20science;kw/warszawa;wp?rd=30&et=1%2C17").text
    soup = BeautifulSoup(html_text,'lxml')

    #Przeszukiwanie ofert pracy na stronie data science - pracuj.pl
    jobs = soup.find_all('div',class_="listing_c1dc6in8")
    for job in jobs:
        slownik = {}
        #Odnalezienie nazwy stanowiska
        job_name = job.find('h2',class_="listing_buap3b6").a.text

        #Odnalezienie nazwy firmy
        company_name = job.find('div',class_ = "listing_c18jd7pe").h4.text

        #Podanie linku do oferty
        job_link = job.find('h2',class_="listing_buap3b6").a["href"]

        #Przejście do strony z ofertą
        job_text = requests.get(job_link).text
        soup_job = BeautifulSoup(job_text,'lxml')

        try:
            #Odnalezienie daty wygaśnięcia oferty
            expire_data = soup_job.find('div',class_="offer-viewDZ0got").text
        except:
            expire_data="--------"

        slownik["Job name"] = job_name
        slownik["Company name"] = company_name
        slownik["Job link"] = job_link
        slownik["Expiring data"] = expire_data[-11:]

        #Przeszukanie skilli na stanowisko
        skills_tab = soup_job.find('ul',class_="offer-viewEX0Eq-")
        try:
            skills = skills_tab.find_all('li',class_="offer-viewjJiyAa offer-vieweKR6vg")
            list_skills=[]
            for skill in skills:
                list_skills.append(skill.p.text)
            #print(list_skills)
            slownik["Skills"] = list_skills
        except:
            slownik["Skills"] =[]

        #Sprawdzenie warunku umiejętności  
        i=0
        for s in skillsy:
            if s.lower()  in  [x.lower() for x in slownik["Skills"]]:
                i+=1
        if i==0:   
            oferty.append(slownik)
    return oferty

def database_creation(oferts,filename):
    df = pd.DataFrame(oferts)

    locale.setlocale(locale.LC_TIME, 'pl_PL.UTF-8')
    #Podział na bazę danych z formatem angielskim i polskim
    df_pl = df[df['Expiring data'].str.contains('sty|lut|mar|kwi|maj|cze|lip|sie|wrz|paź|lis|gru|--------')]
    df_en = df[df['Expiring data'].str.contains('Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec')]

    # Konwersja dat do formatu polskiego
    df_pl['Expiring data'] = pd.to_datetime(df_pl['Expiring data'], format='%d %b %Y', errors='coerce')

    # Konwersja dat do formatu angielskiego
    locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')
    df_en['Expiring data'] = pd.to_datetime(df_en['Expiring data'], format='%d %b %Y', errors='coerce')

    # Połączenie spowrotem danych
    df = pd.concat([df_pl, df_en])

    df = df.sort_values('Expiring data')
    df.to_excel(filename+'.xlsx', index=False)
    
    print(df)
    print("-----------------------------------------------------")
    print(f"Dane zostały zapisane w pliku {filename}.xlsx")

def welcome():
    #Przywitanie użytkownika oraz ewentualne pominięcie ofert z konkretnym wymaganiem
    print("Wpisz umiejętność, która wyklucza ofertę pracy, jeżeli jest więcej to wypisz po przecinku (Umiejętności typu: linux,java,python...)")
    skillsy = input("> ")
    skillsy = skillsy.split(",")
    return skillsy


skillsy = welcome()
while True:
    print("Przetwarzanie...")

    oferts = job_searching(skillsy)
    database_creation(oferts,"DataScience_offers")

    print("Oczekiwanie 30 minut...")
    time.sleep(1800)
