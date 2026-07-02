from analise1 import texto_certo_contado
import pandas as pd
import matplotlib.pyplot as plt

#Aqui através de um loop, vamos percorrer o texto contabilizando a quantidade de cada letra.
frequencia = {}

for caractere in texto_certo_contado:
    if caractere == ' ':
        continue
    
    if caractere in frequencia:
        frequencia[caractere] += 1
    else:
        frequencia[caractere] = 1
print(frequencia)



#Vai criar um dataframe com as colunas de caractere e frequencia dele
df = pd.DataFrame(list(frequencia.items()), columns=['caracteres', 'frequencia'])
df = df.sort_values(by = "frequencia", ascending=False)

#Vai criar um gráfico de barras que permite visualizar a frequência de cada letra
plt.bar(df['caracteres'], df['frequencia'])
plt.xlabel('Caracteres')
plt.ylabel('Frequência')
plt.title('Distribuição de Caracteres')
plt.show()
