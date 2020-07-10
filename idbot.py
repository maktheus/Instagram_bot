from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

url="https://www.instagram.com/p/CCHf5A1F2h2/"

class InstagramBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path="C:\code\BOT\geckodriver-v0.26.0-win64\geckodriver.exe")
  
            
    def entrar(self):
       
        driver = self.driver
        driver.get(url)
        time.sleep(3)

        entrar=driver.find_element_by_xpath("//a[@class='sqdOP  L3NKy   y3zKF    ZIAjV ']") 
        entrar.click()
        self.login()
    
    @staticmethod
    def type_like_a_person(sentence, single_input_field):
       
        print("going to start typing message into message share text area")
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1, 5) / 30)

    def login(self):
        driver = self.driver
        time.sleep(3)

         
        user_camp = driver.find_element_by_xpath("//input[@name='username']") 
        user_camp.click()
        user_camp.clear()
        user_camp.send_keys(self.username)

        password_camp = driver.find_element_by_xpath("//input[@name='password']")
        password_camp.click()
        password_camp.clear()
        password_camp.send_keys(self.password)
        password_camp.send_keys(Keys.RETURN)
        time.sleep(5)

        guarda= driver.find_element_by_xpath("//button[@class='sqdOP yWX7d    y3zKF     ']")
        guarda.click()
        time.sleep(5) 
        guard= driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']")
        guard.click()
        time.sleep(5)
        self.retorno()  


    def retorno(self):
        driver = self.driver
        driver.get(url)
        time.sleep(3)
        for x in range(10):
            try: 
                    comments = [
                        "@dekomao",
                        
                    ]  
                    driver.find_element_by_class_name("Ypffh").click()
                    comment_input_box = driver.find_element_by_class_name("Ypffh")
                    time.sleep(random.randint(1, 3))
                    self.type_like_a_person(
                        random.choice(comments), comment_input_box)
                    time.sleep(random.randint(1, 3))
                    driver.find_element_by_xpath(
                        "//button[contains(text(), 'Publicar')]"
                    ).click()
                    time.sleep(random.randint(1, 3))
            except Exception as e:
                print(e)
                time.sleep(3)
        

        


SorteioBot = InstagramBot('maktheus@gmail.com','m123456u')
SorteioBot.entrar()
