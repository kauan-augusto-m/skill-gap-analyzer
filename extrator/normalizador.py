import unicodedata

class Normalizador:
    # 1. Definimos as configurações de símbolos (dados separados do comportamento)
    SIMBOLOS_INICIO = "-'\"([{•+#"
    SIMBOLOS_FIM = ".,;:!?'\")}]"

    def normalizar(self, entrada):
        # Passo 1 & 2: Normaliza acentos (NFD) e converte para minúsculas
        texto_nfd = unicodedata.normalize("NFD", entrada)
        caracteres_filtrados = []
        for letra in texto_nfd:
            if unicodedata.combining(letra) == 0:
                caracteres_filtrados.append(letra)
        
        texto_limpo = "".join(caracteres_filtrados).lower()
        
        # Passo 3: Divide em palavras brutas
        palavras = texto_limpo.split()
        
        # Passo 4: Limpa o começo, o fim e descarta as palavras que viraram vazias
        palavras_tratadas = []
        for p in palavras:
            p_limpa = p.lstrip(self.SIMBOLOS_INICIO).rstrip(self.SIMBOLOS_FIM)
            if p_limpa:  # Se a palavra não estiver vazia, guarda!
                palavras_tratadas.append(p_limpa)
                
        # Passo 5: Junta tudo de volta com um espaço único
        return " ".join(palavras_tratadas)