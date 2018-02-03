# -*- coding: utf-8 -*-

from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup


class Oseba:                                          # objekt Oseba
    def __init__(self, name, surname, city, email):
        self.name = name
        self.surname = surname
        #self.age = age
        self.city = city
        self.email = email

MAIN_URL = "https://scrapebook22.appspot.com/"

webpage = urlopen(MAIN_URL).read()

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

        p_city = personal_page.find(id=("data-city").string
        print (p_city)

        p_email = personal_page("span", {"class": "email"}).string
        print (p_email)

        person = Oseba(name, surname, p_city, p_email)
        persons_data.append(person)

print(persons_data)

csv_file = open("persons_data.csv", "w")

for person in persons_data:
    csv_file.write(person.name + "," + person.surname + "from: " + person.city + "," + person.email + "\n")

csv_file.close()
