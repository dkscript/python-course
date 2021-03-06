import json,os,re

def lista_arquivos(diretorio,extensao='mxf'):
    pattern = '.*'
    pasta = diretorio# diretorio onde localiza os arquivos .extensao
    caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
    arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
    lista_arquivos_extensao = [re.findall(pattern,arq) for arq in arquivos if arq.lower().endswith(extensao.lower())]  # lista com todos os arquivos .extensao no diretorio
    return lista_arquivos_extensao



def temCloseCaption(arquivo_json):
    with open(arquivo_json) as file_data:
        data = file_data.readlines()

    arquivo_json = ''
    for item in (data):
        arquivo_json += item
    extraido_json = json.loads(arquivo_json)
    temcc = False

    for item in range(len(extraido_json['media']['track'])):
        if extraido_json['media']['track'][item]['@type'] == 'Text':
            temcc = True
    return temcc

#path_api = 'C:\\Users\\projetos\\PycharmProjects\\python-course\\Comerciais_Api_globo\\arquivos_json\\'
path_api = 'C:\\Users\\projetos\\PycharmProjects\\python-course\\Comerciais_Api_globo\\AMOSTRA_PCM_BIG_LITTLE\\'

print(lista_arquivos(path_api,'json'))
for arquivos in lista_arquivos(path_api,'json'):
    print(arquivos[0].replace(path_api,'') + ' Possui CC ? ' + str(temCloseCaption(arquivos[0])))