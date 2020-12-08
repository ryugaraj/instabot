import os
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from random import randint
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

options = Options()
options.headless = True
binary = FirefoxBinary(os.environ.get("FIREFOX_BIN"))
browser = webdriver.Firefox(options=options, firefox_binary=binary, executable_path=os.environ.get("GECKODRIVER_PATH"))
browser.implicitly_wait(5)
browser.get('https://www.instagram.com/')

sleep(2)


#Login

def login():
    
    username_input = browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
    username_input.send_keys(os.environ.get("runner1.u"))
    password_input = browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
    password_input.send_keys(os.environ.get("runner1.p"))
    login_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]")
    login_button.click()
    browser.implicitly_wait(5)
    not_now = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
    not_now.click()
    browser.implicitly_wait(5)
    not_now2 = browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
    not_now2.click()

login()

#Comments and Id's 

comments=['Wanna have some fun with me tonight 🍑💦',"Don't you dare see my story 🍑💦 ","I can be your bad girl tonight 🍑💦", "See my Big surprise dear 🍑🍑 it's waiting for you💦💦",
          "I want that big long and hard 🍌🍌💦💦","I wanna see a big 🍆🍆 and play with it💦💦 ","Everyone who reads this be happy ✨✨✨✨"]

insta_id=['https://www.instagram.com/9gag/','https://www.instagram.com/jessicananan029/'] 

def run():
    num_comment=0
    try:
        while 1:
            for i in insta_id:
                browser.get(i)
                post_links = []
                soup = BeautifulSoup(browser.page_source,'html.parser')
                posts = soup.findAll('a')
                for post in posts:
                    if '/p/' in post['href']:
                        post_links.append(post['href'])
                    
                if (len(post_links)>0):
                    browser.get("https://www.instagram.com/"+post_links[0])

                    soup2 = BeautifulSoup(browser.page_source,'html.parser')
                    so = soup2.find('div',class_="k_Q0X NnvRN")
                    timer = so.find('time',class_="_1o9PC Nzb55").text
                
                    if ("second" in timer):
                        num_comment+=1
                        like=browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/article/div[3]/section[1]/span[1]/button")
                        like.click()

                        browser.find_element_by_class_name('X7cDz').click()
                        browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea").send_keys(comments[randint(0,6)])
                        
                        post_btn=browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button")
                        post_btn.click()
                        
                        sleep(60)
                
                    if num_comment >=15:
                        num_comment=0
                        sleep(600)
            
    except Exception as e:
        print(e.__class__)
        run()
run()

browser.close()
