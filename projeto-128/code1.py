from bs4 import BeautifulSoup
import requests
import pandas as pd 
#LINK DA PAGINA DE ESTRELAS ANÃS MARRONS
link = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

#------------------------------------------------#
#---------------      PARTE 1   -----------------#
#---------------   CSV COMPLETO   ---------------#
#------------------------------------------------#

#obter a página
page = requests.get(link)

#obtenha a análise da página em python
soup = BeautifulSoup(page.text, 'html.parser')

#tabela de estrelas <table> com a classe 'wikitable sortable'
table = soup.find('table', {'class':'wikitable sortable'})

#crie a lista de todas as estrelas
listStars = []

#acesse o tbody da tabela de estrelas
table_tbody = table.find('tbody')
#guarde todas as linhas <tr> da tabela 
table_trs = table_tbody.find_all("tr")

#para cada linha, acesse os dados da coluna
for tr in table_trs:
    #guarde os dados da coluna <td>
    columns = tr.find_all("td")
    line = []
    #repete para cada coluna
    for column in columns:
        #guarda o texto com a info daquela coluna
        data = column.text.rstrip()
        #add na linha de dados o dado
        line.append(data)
    #add a lista de dados da estrela na lista de estrelas
    listStars.append(line)
#mostre o resultado
print(listStars)

#defina os nomes das colunas
headers = [
    "Star", "Constellation", "Right Ascension", "Declination",
    "App. Mag.", "Distance", "Spectral Type", "Brown Dwarf", "Mass",
    "Radius", "Orbital Period", "Semimajor axis", "Ecc.", "Discovery Year"
]
#converta a lista de estrelas em um dataframe
dataframe = pd.DataFrame(listStars, columns = headers)
#converta o dataframe em um arquivo csv
dataframe.to_csv("complete.csv")

#------------------------------------------------#
#---------------      PARTE 2   -----------------#
#---------------   CSV RESUMIDO   ---------------#
#------------------------------------------------#

#lista de dados
listaNome = []
listaDistancia = []
listaMassa = []
listaRaio = []

#repete para cada estrela da lista
for i in range(1, len(listStars)):
    #add o nome da estrela na lista
    listaNome.append(listStars[i][0])
    #add a distancia da estrela da Terra na lista
    listaDistancia.append(listStars[i][5])
    #add o peso da estrela na lista de peso
    listaMassa.append(listStars[i][8])
    #add o tamanho da estrela na lista de tamanho
    listaRaio.append(listStars[i][9])

headers = [
    "Star_name", "Distance", "Mass", "Radius"
]

#combinar as listas em uma variável só
final_list = list(zip(listaDistancia, listaNome, listaMassa, listaRaio))

#convertendo a lista final em dataframe
final_dataframe = pd.DataFrame(final_list, columns=headers)

#convertendo o dataframe em arquivo csv com índices
final_dataframe.to_csv("final_data.csv", index=True, index_label='id')