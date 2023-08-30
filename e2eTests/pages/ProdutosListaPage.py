from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from e2eTests.locators import ProdutosListaLocators
from e2eTests.pages.PageObject import PageObject


class ProdutosListaPage(PageObject):

    def __init__(self, driver=None):
        super().__init__(driver)

    def is_resultado_page(self):
        try:
            self.driver.find_element(By.XPATH, ProdutosListaLocators.title_resultado_busca_xpath)
            return True
        except:
            return False

    def acessar_primeiro_produto(self):
        # Aguarda até que o elemento seja clicável
        elemento = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, ProdutosListaLocators.item_primeiro_buscado_xpath))
        )
        # Clica no elemento após o carregamento
        elemento.click()
