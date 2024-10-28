from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class Data:
    # creating Guvi url 
    url = 'https://www.instagram.com/guviofficial/'

class Guvi_insta_automation:
    def __init__ (self):
        self.driver = webdriver.Chrome()

    def start(self):
        # starting the browser
        self.driver.get(Data().url) # passing url link
        self.driver.maximize_window() # maximizing window
        sleep(5)
        print("Successfully launched")

    def count_followers(self):
        result = [] # Created a empty list
        followers_Count = self.driver.find_elements(by=By.XPATH, value= '//li[@class="xl565be x1m39q7l x1uw6ca5 x2pgyrj"]/following-sibling::li') # got the Xpath value using parent-child relation
        for data in followers_Count:
            result.append(data.text) # appending the text to the empty list
        
        Followers_count= result[0]
        Following_Count= result[1]
        print("Followers: ", Followers_count)
        print("Following: ",Following_Count)

    
    def shutdown(self):
        # shutting the browser
        self.driver.close()
        print("Successfully closed")

# creating a object and linking the class name

automation = Guvi_insta_automation()
automation.start()
automation.count_followers()
automation.shutdown()