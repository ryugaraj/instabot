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
  session.set_quota_supervisor(enabled=True,
                               peak_likes_hourly=70,
                               peak_comments_hourly=21,
                               peak_follows_hourly=48,
                               peak_follows_daily=100,
                               peak_unfollows_hourly=35,
                               peak_unfollows_daily=402)

  session.like_by_tags(['scarlettjohansson'], amount=50)
  session.set_do_comment(True, percentage=100)
  session.set_comments([u'My Girl is fire :fire:',
                        u'So Awesome :flushed:',
                        u'Amazing :heart_eyes:'])

  session.follow_user_followers(['scarlettjohanssonworld'], amount=50,
                                randomize=False, sleep_delay=10)
  '''session.unfollow_users(amount=30, allFollowing=True, style="LIFO",
                         unfollow_after=24*60*60, sleep_delay=5)'''
  session.end()

def runner2():
  session = InstaPy(username=os.environ.get("runner2.u"), password=os.environ.get("runner2.p"),
                              geckodriver_path = os.environ.get("GECKODRIVER_PATH"), browser_executable_path=os.environ.get("FIREFOX_BIN"),
                              headless_browser = True)

  session.login()
  session.set_quota_supervisor(enabled=True,
                               peak_likes_hourly=70,
                               peak_comments_hourly=21,
                               peak_follows_hourly=48,
                               peak_follows_daily=1000,
                               peak_unfollows_hourly=35,
                               peak_unfollows_daily=402)
  choose_acc = random.choice(['codecademy', 'freecodecamp', 'geeks_for_geeks', 'coderhumor', 'codes.learning'])
  session.like_by_tags(['coder'], amount=50)
  session.set_do_comment(True, percentage=100)
  session.set_comments([u'Nice :fire:',
                        u'So Awesome :flushed:',
                        u'Amazing :heart_eyes:'])

  session.follow_user_followers([choose_acc], amount=100,
                                randomize=False, sleep_delay=10)
while 1:
  runner2()
  runner1()
  time.sleep(1)
