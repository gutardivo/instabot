from selenium import webdriver
from time import sleep
username = input("Username: ")
pw = input("Password: ")

class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome(executable_path='/Users/mac/Desktop/Python/chromedriver')
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(5)

    def get_unfollowers(self):
        self.driver.get("https://www.instagram.com/"+username)
        sleep(1)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("//div[@class='isgrP']")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scroll_box)
        
        fln_links = scroll_box.find_elements_by_tag_name('a')
        following = [name.text for name in fln_links if name != '']

        self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/div[2]/button')\
            .click()

        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()

        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("//div[@class='isgrP']")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scroll_box)
        
        flr_links = scroll_box.find_elements_by_tag_name('a')
        followers = [name.text for name in flr_links if name != '']

        self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/div[2]/button')\
            .click()
        
        whitelist = ['']
        not_following_back = [user for user in following if user not in followers and user not in whitelist]
        print(not_following_back)    


InstaBot(username,pw).get_unfollowers()