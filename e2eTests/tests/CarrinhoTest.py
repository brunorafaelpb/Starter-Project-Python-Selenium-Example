from e2eTests.pages.HomePage import HomePage
from e2eTests.pages.ProdutosListaPage import ProdutosListaPage
from e2eTests.pages.ProdutoPage import ProdutoPage
from e2eTests.pages.CarrinhoPage import CarrinhoPage


class CarrinhoTest:

    # SEM USO DE FIXTURE
    def test_adicionar_item_ao_carrinho(self):
        home_page = HomePage()
        home_page.acessar_homepage()
        home_page.digitar_texto_busca("FIFA 23 - PlayStation 5")
        home_page.clicar_botao_buscar()
        produtos_lista_page = ProdutosListaPage(home_page.driver)
        produtos_lista_page.acessar_primeiro_produto()
        produto_page = ProdutoPage(produtos_lista_page.driver)
        nome_produto = produto_page.adicionar_produto_ao_carrinho()
        produto_page.ir_para_carrinho_apos_adicionar_item()
        carrinho_page = CarrinhoPage(produto_page.driver)
        assert carrinho_page.is_carrinho_page()
        assert carrinho_page.check_nome_produto_no_carrinho(nome_produto)

    # COM USO DE FIXTURE
    def test_adicionar_item_ao_carrinho_com_fixture(self, adicionar_produto_carrinho):
        produto_page, nome_produto = adicionar_produto_carrinho
        produto_page.ir_para_carrinho_apos_adicionar_item()
        carrinho_page = CarrinhoPage(produto_page.driver)
        assert carrinho_page.is_carrinho_page()
        assert carrinho_page.check_nome_produto_no_carrinho(nome_produto)
