# -*- coding: utf-8 -*-

from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup


class Oseba:   # objekt Oseba
    def __init__(self, name, surname, age, city, email):
        self.name = name
        self.surname = surname
        self.age = age
        self.city = city
        self.email = email

# URL iz katerega pobiramo podake in ta naslov damo v spremenljivko MAIN_URL
MAIN_URL = "https://scrapebook22.appspot.com/"

# MAIN_URL odpremo z url.open in ga preberemo z .read(). To damo v spremenljivko webpage
webpage = urlopen(MAIN_URL).read()

# Odprto in prebrano webpage sedaj pošljemo skozi BeautifulSoup za lažje skrejpanje in to
# damo v spremenljivko nice_webpage.

nice_webpage = BeautifulSoup(webpage)
print(nice_webpage.html.head.title.string)

persons_data = []  #seznam v katerega se shranijo podatke

linki = nice_webpage.findAll("a")  # poišče vse "a" tage v nice_webpage
for link in linki:
    if link.string == "See full profile":  # Če je link z stringom "See full profile"
    # Odpremo in preberemo povezavo vsakega profila posebaj in to damo v spremenljivko personal_page
        personal_page = BeautifulSoup(urlopen(MAIN_URL + link["href"]).read())

    # Ker sta na strani 2 "h1" in je ime in priimek drugi izberemo tega z [-1]
        personal_name = personal_page.findAll("h1")[-1].string
        name, surname = personal_name.split(" ")
        print (surname + " - " + name)

    #Ker imamo več "li" moramo izbrati .findAll in z [x]izbrati njegov položaj
        persons_age = personal_page.findAll("li")[1].string
        print (persons_age)

    # V sprem. persons_city shranimo pot do vrednost za izpis. Ker ima data-city različne vrednosti
    # damo za ispis te value True.
        persons_city = personal_page.find("span", {"data-city": True}).string
        print (persons_city)

    # V sprem. personal_email shranimo pot do vrednost za izpis
        personal_email = personal_page.find("span", {"class": "email"}).string
        print (personal_email)

    #V sprem. person damo vse do sedaj zbrane podatke
        person = Oseba(name, surname, persons_age, persons_city, personal_email)
        persons_data.append(person)  # V list person_data damo vse vrednosti k jih imamo v  spre. person


print(persons_data)  # print v interpreter

csv_file = open("persons_data.csv", "w")  # Ustvari in odpre CSV dat.

for person in persons_data:  # Podatki osebe person v seznamu person_data
    # Spodaj vpišemo v kakem vrstnem redu želimo izpis podatkov v CSV dat.
    csv_file.write(person.name + "," + person.surname + "," + person.age + "," + person.city + "," + person.email + "\n")

    # Vedno na koncu zapri CSV file
csv_file.close()
