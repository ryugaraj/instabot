from instapy import InstaPy
from selenium import webdriver
import os
import random
import time
def runner1():
  session = InstaPy(username=os.environ.get("runner1.u"), password=os.environ.get("runner1.p"),
                              geckodriver_path = os.environ.get("GECKODRIVER_PATH"), browser_executable_path=os.environ.get("FIREFOX_BIN"),
                              headless_browser = True)

  session.login()
  session.follow_user_followers(['scarlettjohanssonworld'], amount=50,
                                randomize=True, sleep_delay=10)
  session.unfollow_users(amount=40, allFollowing=True, style="LIFO",unfollow_after=24*60*60, sleep_delay=5)
  session.end()

while 1:

  runner1()
  time.sleep(7*60*60)
  
