from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#start of the script, waiting for the page to load
browser = webdriver.Firefox()
browser.get("https://play2048.co")

#function to "play" the game spamming the arrows in a pattern
def gameplayer():
    for i in range(0, 10):
        htmlElem = browser.find_element_by_tag_name('html')
        htmlElem.send_keys(Keys.UP)
        htmlElem.send_keys(Keys.RIGHT)
        htmlElem.send_keys(Keys.DOWN)
        htmlElem.send_keys(Keys.LEFT)
    return None

#try & except loop to see if the game ended, not done yet
#the script doesn't stop at the end of the game
while True:
    try:
       browser.find_element_by_class_name("retry-button")
       print("Game Over!")
       exit()
    except:
        gameplayer()
