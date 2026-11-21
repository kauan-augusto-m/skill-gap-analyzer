from extrator.dicionario import DicionarioHabilidades
from extrator.normalizador import Normalizador


def test_resolver_apelido():
    dados = {
        "PostgreSQL": ["postgres", "psql"],
    }
    dicionario = DicionarioHabilidades(dados, Normalizador())

    assert dicionario.resolver("postgres") == "PostgreSQL"


def test_tamanho_maximo_janela_conta_canonico():
    dados = {
        "Amazon Web Services": ["aws"],
        "Java": [],
    }
    dicionario = DicionarioHabilidades(dados, Normalizador())

    assert dicionario.tamanho_maximo_janela == 3