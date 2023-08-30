from e2eTests.pages.HomePage import HomePage
from e2eTests.pages.ProdutosListaPage import ProdutosListaPage


class HomeTest:

    def test_acessar_homepage(self, abrir_homepage):
        home_page = abrir_homepage
        assert home_page.is_page(home_page.base_url)

    def test_buscar_produto(self, abrir_homepage):
        home_page = abrir_homepage
        home_page.digitar_texto_busca("FIFA 23 - PlayStation 5")
        home_page.clicar_botao_buscar()
        produtos_lista_page = ProdutosListaPage(home_page.driver)
        assert produtos_lista_page.is_resultado_page()
