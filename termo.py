def filtra(lista_palavras, num_letras):
    palavras_filtradas = []
    caracteres_permitidos = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "

    for palavra in lista_palavras:
        palavra_filtrada = ""
        for c in palavra:
            if c in caracteres_permitidos:
                palavra_filtrada += c

        if len(palavra_filtrada) == num_letras:
            presente = False
            for p in palavras_filtradas:
                if p.lower() == palavra_filtrada.lower():
                    presente = True
                    break
            if not presente:
                palavras_filtradas.append(palavra_filtrada.lower())

    return palavras_filtradas
