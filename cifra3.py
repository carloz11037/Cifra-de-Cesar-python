from analise1 import texto_certo_contado

def decifrar(chave):
    texto_decifrado = ""

    for caractere in texto_certo_contado:

        if caractere == " ":
            texto_decifrado += " "
        else:
            nova_letra = chr(
                ((ord(caractere) - ord('a') - chave) % 26)
                + ord('a')
            )
            texto_decifrado += nova_letra

    return texto_decifrado

for chave in range (26):
    print(f"Chave {chave}:")
    print(decifrar(chave))
    print()