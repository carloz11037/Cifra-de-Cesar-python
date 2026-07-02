#Aqui vamos pegar o texto e tratar para que ele fique fácil de vasculhar

try:
    with open("dados/texto.py", "r") as arquivo:
        conteudo = arquivo.read()

except FileNotFoundError:
    print("O seu arquivo não foi encontrado")

texto_certo =""

for caractere in conteudo:
    if caractere.isalpha() or caractere == " ":
        texto_certo += caractere
        texto_certo_contado = texto_certo.lower()
print(texto_certo_contado)