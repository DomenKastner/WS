# -*- coding: utf-8 -*-

from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup


class Oseba:   # objekt Oseba
    def __init__(self, name, surname, city, email):
        self.name = name
        self.surname = surname
        #self.age = age
        self.city = city
        self.email = email

# URL iz katerega pobiramo podake in ta naslov damo v spremenljivko MAIN_URL
MAIN_URL = "https://scrapebook22.appspot.com/"

# MAIN_URL odpremo z url.open in ga preberemo z .read(). To damo v spremenljivko webpage
webpage = urlopen(MAIN_URL).read()

""" 
  Odprto in prebrano webpage sedaj pošljemo skozi BeautifulSoup za lažje skrejpanje in to 
  damo v spremenljivko nice_webpage. 
"""
nice_webpage = BeautifulSoup(webpage)
print(nice_webpage.html.head.title.string)


persons_data = []  #seznam v katerega vstavimo podatke



linki = nice_webpage.findAll("a")
for link in linki:
    if link.string == "See full profile":
        personal_page = BeautifulSoup(urlopen(MAIN_URL + link["href"]).read())

        personal_name = personal_page.findAll("h1")[-1].string
        name, surname = personal_name.split(" ")
        print (surname + " - " + name)

        p_city = personal_page.find("span", {"data-city"}).string
        city = p_city
        print (p_city)

        p_email = personal_page.find("span", {"class": "email"}).string
        email = p_email
        print (p_email)

        person = Oseba(name, surname, p_city, p_email)
        persons_data.append(person)

print(persons_data)

csv_file = open("persons_data.csv", "w")

for person in persons_data:
    csv_file.write(person.name + "," + person.surname + "," + person.city + "," + person.email + "\n")

csv_file.close()
