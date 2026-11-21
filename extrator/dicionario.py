class DicionarioHabilidades:
    def __init__(self, dados, normalizador):
        raise NotImplementedError

    def resolver(self, termo):
        raise NotImplementedError

    @property
    def tamanho_maximo_janela(self):
        raise NotImplementedError