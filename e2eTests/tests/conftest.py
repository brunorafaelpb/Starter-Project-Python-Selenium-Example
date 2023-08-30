import time

import pytest
from e2eTests.pages.HomePage import HomePage
from e2eTests.pages.ProdutosListaPage import ProdutosListaPage
from e2eTests.pages.ProdutoPage import ProdutoPage


@pytest.fixture()
def abrir_homepage():
    print("Acessando a página principal")
    home_page = HomePage()
    home_page.acessar_homepage()
    yield home_page


@pytest.fixture()
def adicionar_produto_carrinho(abrir_homepage):
    home_page = abrir_homepage
    print("Buscando produto")
    home_page.digitar_texto_busca("FIFA 23 - PlayStation 5")
    home_page.clicar_botao_buscar()
    produtos_lista_page = ProdutosListaPage(home_page.driver)
    produtos_lista_page.acessar_primeiro_produto()
    produto_page = ProdutoPage(produtos_lista_page.driver)
    nome_produto = produto_page.adicionar_produto_ao_carrinho()
    yield produto_page, nome_produto
