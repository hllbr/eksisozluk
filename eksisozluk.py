from selenium import webdriver
import random 
import time

browser =webdriver.Firefox()

url = "https://eksisozluk.com/yazilimcilarin-turkiyeyi-terk-etmesi--5480403?p="


pageCount = 1
entries =[]
entryCount = 1

while pageCount <= 10:
    randomPage = random.randint(1,90)
    newUrl = url + str(randomPage)
    browser.get(newUrl)
    
    elements = browser.find_elements_by_css_selector(".content")
    for element in elements:
        entries.append(element.text)
    time.sleep(2)
    pageCount += 1
with open("entries.text","w",encoding = "UTF-8") as file:
    for entry in entries:
        file.write(str(entryCount) +".\n" +entry + "\n")
        file.write("*************\n")
        entryCount += 1
    


browser.close()




