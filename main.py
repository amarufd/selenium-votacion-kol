import time
from random import randint

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from browserNavigator import BrowserNavigator
import threading

def main():

    print("Loading browser...")
    browser = None

    options = Options()
    options.headless = True

    browser = webdriver.Firefox(options=options)

    page = BrowserNavigator(browser)

    #links_company_lyon = page.get_companies_name('https://www.linkedin.com/search/results/companies/?keywords=Lyon')
    page.votar()

    print("Closing browser...")
    browser.close()


if __name__ == '__main__':
    i = 0
    while True:
        print("Voto Nro° {}".format(str(i)))
        i += 1
        hiloDomi = threading.Thread(target=main)
        hiloDomi.daemon = True  # die with the program
        hiloDomi.start()
        #print("Voto Nro° {}".format(str(i)))
        #i += 1
        #hiloDomi = threading.Thread(target=main)
        #hiloDomi.daemon = True  # die with the program
        #hiloDomi.start()
        value = randint(0, 10)
        time.sleep(value)