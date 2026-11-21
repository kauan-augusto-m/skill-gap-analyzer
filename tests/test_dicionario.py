from extrator.dicionario import DicionarioHabilidades
from extrator.normalizador import Normalizador


def test_resolver_apelido():
    dados = {
        "PostgreSQL": ["postgres", "psql"],
    }
    dicionario = DicionarioHabilidades(dados, Normalizador())

    assert dicionario.resolver("postgres") == "PostgreSQL"