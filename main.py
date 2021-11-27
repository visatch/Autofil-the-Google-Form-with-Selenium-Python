from selenium import webdriver
import random,time
from faker import Faker

option=webdriver.ChromeOptions()

browser = webdriver.Chrome("V:\Freelance\Self-Study\python\chromedriver.exe")
list_phone = {'012','011','098','070','069','013','092','077'}

browser.get("https://docs.google.com/forms/d/e/1FAIpQLSdlyltw0dudZYQu5oJ5HaKwpkIckmyjQyzFx9oEWuMWDqeFKA/viewform")
time.sleep(3)

browser.find_element_by_xpath('//*[@id="identifierId"]').send_keys("flexflexbox01@gmail.com")
browser.find_element_by_xpath('//*[@id="identifierNext"]/div/button').click()
time.sleep(3)
browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys("123123aA#")
browser.find_element_by_xpath('//*[@id="passwordNext"]/div/button').click()

faker = Faker()
Faker.seed(0)

time.sleep(5)

for i in range(5):
    browser.get("https://docs.google.com/forms/d/e/1FAIpQLSdlyltw0dudZYQu5oJ5HaKwpkIckmyjQyzFx9oEWuMWDqeFKA/viewform")
    
    #email
    browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input').send_keys(faker.email())
    #name
    browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(faker.name())
    #fb name
    browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(faker.name())
    #fb link
    browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("www.facebook.com/" + faker.first_name().lower())
    
    #dob
    browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input').send_keys("3252000")

    #phone number
    phone_number = str(faker.random_elements(elements=list_phone,length=1)[0]) + str(faker.random_int(min=100000,max=999999))
    browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(phone_number)

    #ign
    browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(faker.first_name().lower()+faker.last_name().lower())

    #id
    browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(str(faker.random_int(min=100000000000,max=999999999999)))

    # Mythic Glory 1000 points, Mythic 300 stars, Legend
    list_rank = {'Mythic Glory 1000 points', 'Mythic 300 stars', 'Legend'}
    browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(str(faker.random_elements(elements=list_rank,length=1)[0]))

    int_random = faker.random_int(min=1,max=5)
    browser.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div[1]/div[{int_random}]').click()

    int_random = faker.random_int(min=1,max=5)
    browser.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div/span/div/div[{int_random}]').click()

    #first button add file
    browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div[2]/span').click()

    time.sleep(3)
    browser.switch_to.frame(browser.find_element_by_class_name('picker-frame'))
    print("4")
    time.sleep(5)
    # tap on tab my drive
    # browser.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div/div[4]/div').click()
    # browser.find_element_by_xpath('//*[@id=":g.select-files-button"]/div').click()
    browser.find_element_by_xpath('//*[@id=":6"]').click()

    time.sleep(5)

    browser.find_element_by_xpath('//*[@id=":1a.docs.0.1oe7tESa9uNnUC75FdYuqzPtPbLYz7QFi"]/div[2]').click()
    browser.find_element_by_xpath('//*[@id="picker:ap:2"]').click()
    time.sleep(3)

    print('refresh bro')
    browser.refresh()
    # browser.switch_to.alert.accept()

    print("inserting 2nd picture here")
    # iframe = browser.find_element_by_class_name('freebirdLightBackground')
    # browser.switch_to.frame(iframe)
    time.sleep(5)
    browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div[2]').click()

    print("2")
    time.sleep(5)

    newFrame = browser.find_element_by_class_name('picker-frame')
    browser.switch_to.frame(newFrame)

    print("3")
    time.sleep(3)

    print("4")
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id=":6"]').click()

    time.sleep(5)

    browser.find_element_by_xpath('//*[@id=":1a.docs.0.1y0K2G4AYgKQu0m4WRkR5sb-dgkG2d6-H"]/div[2]').click()
    browser.find_element_by_xpath('//*[@id="picker:ap:2"]').click()
    time.sleep(3)

    browser.switch_to_default_content()

    browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span').click()
