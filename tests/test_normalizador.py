# Regra de Normalização:
# O processo de normalização limpa e padroniza o texto bruto convertendo todas as letras para minúsculas 
# e removendo marcas de acentuação (separando caracteres base de seus diacríticos via Unicode NFD). 
# Em seguida, aplica uma limpeza de pontuação baseada na posição do símbolo em relação às palavras: 
# remove totalmente pontuações isoladas e símbolos de pontuação de frase (como vírgulas, parênteses, dois-pontos, 
# ponto e vírgula, exclamação, interrogação, aspas e marcadores como bullets). Símbolos especiais que compõem 
# termos técnicos são preservados com base em suas posições válidas — como o ponto no início (.net) ou no meio (node.js), 
# hífens e barras no interior de palavras compostas (front-end, ci/cd), e os sinais de mais e cerquilha quando anexados 
# ao final (c++, c#) —, enquanto pontos finais isolados no término de palavras ou frases são descartados. 
# Por fim, múltiplos espaços e quebras de linha são condensados em um único espaço padrão.

import pytest
from extrator.normalizador import Normalizador

CASOS_TESTE = [
    ("Python", "python"),
    ("Inglês", "ingles"),
    ("Configuração", "configuracao"),
    ("PostgreSQL,", "postgresql"),
    ("(Docker)", "docker"),
    ("java.", "java"),
    ("experiência com Java.", "experiencia com java"),
    ("C++", "c++"),
    ("C#", "c#"),
    (".NET", ".net"),
    ("Node.js,", "node.js"),
    ("Node.js.", "node.js"),
    ("C++.", "c++"),
    ("C#.", "c#"),
    (".NET.", ".net"),
    ("Requisitos: Python, Docker e .NET (obrigatório).", "requisitos python docker e .net obrigatorio"),
    ("Python\n\nDocker   AWS", "python docker aws"),
    ("- Python\n• Docker", "python docker"),
    ("", ""),
    ("... , !?", ""),
    ("front-end", "front-end"),
    ("CI/CD", "ci/cd"),
    ("Stack; banco: PostgreSQL! 'Redis'?", "stack banco postgresql redis"),
]

@pytest.mark.parametrize("entrada, esperado", CASOS_TESTE)
def test_normalizador(entrada, esperado):
    normalizador = Normalizador()
    assert normalizador.normalizar(entrada) == esperado