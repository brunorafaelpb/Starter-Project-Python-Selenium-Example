from selenium.webdriver.common.by import By
from e2eTests.locators import HomeLocators
from e2eTests.pages.PageObject import PageObject


class HomePage(PageObject):
    base_url = 'https://www.amazon.com.br/'

    def __init__(self, driver=None):
        super().__init__(driver)
        self.acessar_homepage()

    def acessar_homepage(self):
        self.driver.get(self.base_url)

    def digitar_texto_busca(self, texto_busca):
        busca = self.driver.find_element(By.ID, HomeLocators.input_busca_item_id)
        busca.clear()
        busca.send_keys(texto_busca)

    def clicar_botao_buscar(self):
        self.driver.find_element(By.ID, HomeLocators.btn_buscar_id).click()
