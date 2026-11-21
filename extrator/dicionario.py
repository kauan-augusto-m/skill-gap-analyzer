class DicionarioHabilidades:
    def __init__(self, dados, normalizador):
        self._indice = {}
        self._tamanho_maximo_janela = 0

        for nome_canonico, apelidos in dados.items():
            termos = [nome_canonico, *apelidos]
            for termo in termos:
                termo_norm = normalizador.normalizar(termo)
                if termo_norm:
                    qtd_palavras = len(termo_norm.split())
                    self._tamanho_maximo_janela = max(
                        self._tamanho_maximo_janela, qtd_palavras
                    )
                    self._indice[termo_norm] = nome_canonico

    def resolver(self, termo):
        return self._indice.get(termo)

    @property
    def tamanho_maximo_janela(self):
        return self._tamanho_maximo_janela