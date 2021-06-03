import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class BrowserNavigator:
    browser = None

    def votar(self):
        print("comenzando navegacion")
        self.browser.get('https://www3.animeflv.net/')

        self.browser.implicitly_wait(1)
        time.sleep(5)

        main = self.browser.find_element_by_class_name('Main')
        animesDisponibles = main.find_elements(By.TAG_NAME, "li")

        objetoSeleccionado = None
        for anime in animesDisponibles:
            #print(anime.text)
            strongs = anime.find_elements(By.TAG_NAME, "strong")
            #print(strongs)
            for strong in strongs:
                print(strong.text)
                if strong.text == 'Tensura Nikki: Tensei shitara Slime Datta Ken':
                    objetoSeleccionado = anime

        #boton = self.browser.find_elements_by_id('btn-20201117192819')
        if objetoSeleccionado is not None:
            objetoSeleccionado.find_element_by_tag_name("a").click()

        time.sleep(3)

        videoBox = self.browser.find_element_by_id('video_box')
        div = videoBox.find_element_by_tag_name('div')
        div.click()

        time.sleep(1)

        paginaActual = self.browser.current_window_handle
        todasLasPestanias = self.browser.window_handles

        for pestania in todasLasPestanias:
            if (pestania != paginaActual):
                self.browser.switch_to.window(pestania)

        videoBox = self.browser.find_element_by_id('video_box')
        self.browser.switch_to_frame(videoBox.find_element_by_tag_name('iframe'))
        img = self.browser.find_element_by_tag_name('img')
        img.click()

        time.sleep(3)

        action = ActionChains(self.browser)
        player = self.browser.find_element_by_id('player')
        action.move_to_element(player).perform()
        jwIconFullscreen = self.browser.find_element_by_class_name('jw-icon-fullscreen')
        jwIconFullscreen.click()

        print("reproduciendo")


    def __init__(self, browser):
        self.browser = browser