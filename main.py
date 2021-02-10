import time
from random import randint

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from browserNavigator import BrowserNavigator
import threading
import platform

def main():

    print("Loading browser...")
    browser = None

    options = Options()
    options.headless = True

    if platform.system() == 'Linux' or platform.system() == 'Darwin':
        print('Corriendo en Linux')
        driver = webdriver.Firefox(options=options)
    else:
        print('Corriendo en Windows')
        driver = webdriver.Firefox(
            executable_path='.\drivers\geckodriver.exe',
            options=options
        )

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
        main()
        #hiloDomi = threading.Thread(target=main)
        #hiloDomi.daemon = True  # die with the program
        #hiloDomi.start()
        #print("Voto Nro° {}".format(str(i)))
        #i += 1
        #hiloDomi = threading.Thread(target=main)
        #hiloDomi.daemon = True  # die with the program
        #hiloDomi.start()
        #value = randint(3, 5)
        #time.sleep(value)