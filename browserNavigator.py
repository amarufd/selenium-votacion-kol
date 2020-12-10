import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class BrowserNavigator:
    browser = None

    def votar(self):
        print("")
        self.browser.get('https://www.bupa.cl/concurso/bupa/maria-nicole-castillo-suarez-postulada-o-por-maria-nicole-castillo')

        self.browser.implicitly_wait(1)

        boton = self.browser.find_elements_by_id('btn-20201117192819')
        boton[0].click()

        time.sleep(1)

        print("votado")


    def __init__(self, browser):
        self.browser = browser