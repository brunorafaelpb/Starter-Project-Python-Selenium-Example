from selenium.webdriver.common.by import By
from e2eTests.locators import ProdutoLocators
from e2eTests.pages.PageObject import PageObject


class ProdutoPage(PageObject):

    def __init__(self, driver=None):
        super().__init__(driver)

    def adicionar_produto_ao_carrinho(self):
        nome_produto = self.driver.find_element(By.ID, ProdutoLocators.title_nome_produto_id).text
        self.driver.find_element(By.ID, ProdutoLocators.btn_adicionar_carrinho_id).click()
        return nome_produto

    def ir_para_carrinho_apos_adicionar_item(self):
        self.driver.find_element(By.ID, ProdutoLocators.btn_ir_para_carrinho_id).click()
