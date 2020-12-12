from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from random import randint

#Login

browser = webdriver.Firefox()
browser.implicitly_wait(5)
browser.get('https://www.instagram.com/')

sleep(60)

username_input = browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
username_input.send_keys("angelverma007")
password_input = browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
password_input.send_keys("hgku4577")

login_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]")
login_button.click()
browser.implicitly_wait(5)
not_now = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
not_now.click()
browser.implicitly_wait(5)
not_now2 = browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
not_now2.click()


#Comments and Id's 

comments=[ 'Hello koi apna bada sa lund dikhaega 🍆🍆💦💦', 'Follow Me whatsapp pe chat krenge ✉️✉️ ',
 'Dm me aa jaiye 🙈 ek dusre ka dekhenge 🍆🍑','Aa jao bahut garam hu abhi 🍆💦', 'Kisi ke paas bada aur lamba lund hai to dm kre🍆💦',
'Sirf bade lund wale 🍆💦 Boys Follow kre 💋💋','main kaisi lgti hu 🍑 jara dekh ke batao 👙👙', 
'sab mujhe follow kro ❤️ jo chahe dungi🍑🍆💦 ', 'follow krke dm me aa jao 🙈 tumhare hosh uda dungi', 
'mere bf ka khada nhi hota hai koi hai jo meri pyaas bujha de 🍆🍆💦💦', 'Bahut horny hu yaar 🍆💦 jldi aao na dm me 💋💋',
'mera badan tadap rha hai tumhara 🍆💦 dekhne ko', 'koi to meri pyaas bujha do 🍆💦', 'Dm me aao follo krke 🙈 🍆💦',
 'koi mard hai bde lund wala jo meri jawani ki aag ko bujha sake 🍆💦🍆💦'] 

insta_id=['https://www.instagram.com/neha_rajput___143/','https://www.instagram.com/dimpalankita/',
'https://www.instagram.com/muskan_rajput517/','https://www.instagram.com/nisha_cute199/','https://www.instagram.com/renu__kumari_/',
'https://www.instagram.com/bindas_pooja/','https://www.instagram.com/muskan__varma/','https://www.instagram.com/pooja_sharma921/',
'https://www.instagram.com/nisha_sharma_57/','https://www.instagram.com/anita_kumari9/','https://www.instagram.com/kajal.sharmafc/',
'https://www.instagram.com/alia_7569/','https://www.instagram.com/kaurmeet.1313/','https://www.instagram.com/vandana__devi/']


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
                
                    if ('second' in timer )  or (("min" in timer) and ((timer[0]=='1')or (timer[0]=='2'))):
                        num_comment+=1
                        like=browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/article/div[3]/section[1]/span[1]/button")
                        like.click()

                        browser.find_element_by_class_name('X7cDz').click()
                        browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea").send_keys(comments[randint(0,14)])
                        
                        post_btn=browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button")
                        post_btn.click()
                
                    if num_comment >=15:
                        num_comment=0
                        sleep(600)
                sleep(0.5)
    except:
        run()
run()

browser.close()
