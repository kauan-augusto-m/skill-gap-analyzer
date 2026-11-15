import unicodedata
class Normalizador:
    
    def normalizar(self,entrada):
        texto_nfd = unicodedata.normalize("NFD", entrada)
        caracteres_filtrados = []
        for letra in texto_nfd:
                if unicodedata.combining(letra) == 0:
                    caracteres_filtrados.append(letra)
        texto_limpo = "".join(caracteres_filtrados).lower()
        return " ".join(texto_limpo.split())