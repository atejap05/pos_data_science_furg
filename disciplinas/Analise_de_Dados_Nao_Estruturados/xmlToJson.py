import xmltodict
import json

with open("SEU_XML_AQUI.xml") as xmlFile:
    data_dict = xmltodict.parse(xmlFile.read())

json_data = json.dumps(data_dict)

with open("disciplinas/Analise_de_Dados_Nao_Estruturados/json_file.json", 'w') as jsonFile:
    jsonFile.write(json_data)

