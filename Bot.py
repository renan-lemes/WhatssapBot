from selenium import webdriver
import time as t


class WhatssapBot:
    def __init__(self):
        self.mensagem = 'Olá esse é oooo bot do dat ლ(╹◡╹ლ)'
        self.grupos = ['Sim JB você é meu filho.', 'Tadeu']
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMenssagens(self):
        # <span dir="auto" title="Tadeu"
        # <div class="_2lMWa"><div tabindex="-1" class="p3_M1">
        # <span data-testid="send" data-icon="send" class="">
        self.driver.get('https://web.whatsapp.com/')
        t.sleep(30)
        for grupo in self.grupos:
            grupo = self.webdriver.find_element_by_xpath(
                f"//span[@title='{ grupo }']")
            t.sleep(3)
            grupo.click()
            chatbox = self.driver.find_element_by_class_name('_2lMWa')
            t.sleep(3)
            chatbox.click()
            chatbox.send_keys(self.mensagem)
            botao_envio = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
            t.sleep(3)
            botao_envio.click()
            t.sleep(5)


bot = WhatssapBot()
bot.EnviarMenssagens()
