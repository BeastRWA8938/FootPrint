from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By

'''
Social Media Sites are stored in this list social_media you can add more if you like something specific.
'''
social_media = ['facebook','instagram','linkedin','snapchat','youtube','twitter','reddit','pinterest','github']

# stores all the sites found on the page.
site = []

# writes all the links in a text file.
def writelink(link):
    with open('links.txt', 'w') as file:
       file.writelines(link)


while True:
    user_input = input("Enter the name of the Person : ")

    # count number of spaces in the name
    count = user_input.count(' ')

    #loop to change space to +
    for i in range(count):
        user_input = user_input.replace(' ','+')
        
    # stores the response in res
    url = f"https://www.google.com/search?client=safari&rls=en&q={user_input}&ie=UTF-8&oe=UTF-8"

    '''
    including services - here path to the Chromedriver

    please enter the path for your chromedriver in the PATH variable
    PATH = '/Users/user/path/chromedriver'

    another alternative for it is to put chromedrive in the same folder and use os
    PATH = os.path.join(os.getcwd(),'chromedriver')
    '''
    PATH = os.path.join(os.getcwd(),'chromedriver')
    service = Service(executable_path=PATH)

    # initilize driver
    driver = webdriver.Chrome(service=service)
    
    # attempt a search
    driver.get(url)
    
    # pause for 5 sec
    time.sleep(5)

    # identify elements with tagname <a>
    lnks=driver.find_elements(By.TAG_NAME,"a")

    # traverse list
    for lnk in lnks:

        # get_attribute() to get all href
        a = lnk.get_attribute('href')
        if a != None:
            # filters for specific social media links
            for i in social_media:
                if i in a:
                    site.append(a)
                    site.append('\n')
    
    writelink(site)

    # pause for 5 sec
    time.sleep(5)

    # close the chrome window
    driver.close()
    break
