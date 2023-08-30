from selenium.webdriver.common.by import By
from e2eTests.locators import CarrinhoLocators
from e2eTests.pages.PageObject import PageObject


class CarrinhoPage(PageObject):

    def __init__(self, driver=None):
        super().__init__(driver)

    def is_carrinho_page(self):
        try:
            self.driver.find_element(By.XPATH, CarrinhoLocators.title_carrinho_xpath)
            return True
        except:
            return False

    def check_nome_produto_no_carrinho(self, nome_produto):
        nome_produto_carrinho = self.driver.find_element(By.XPATH, CarrinhoLocators.txt_nome_primeiro_produto_xpath).text
        return nome_produto in nome_produto_carrinho
