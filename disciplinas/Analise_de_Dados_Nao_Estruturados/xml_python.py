import os
import xml.etree.ElementTree as ET

locadora = ET.Element("locadora")

albuns = ET.SubElement(locadora, "albuns")

cd_I = ET.SubElement(albuns, "CD_I")

ET.SubElement(cd_I, "field1", name="gravadora").text = "A Melhor Gravadora"
ET.SubElement(cd_I, "field2", name="numMusicas").text = '20'
ET.SubElement(cd_I, "field3", name="artista").text = 'joelzinho dos teclados'
ET.SubElement(cd_I, "field4", name="titulo").text = 'Forro na Veia'
ET.SubElement(cd_I, "field5", name="genero").text = 'Pizadinha do Forro'
ET.SubElement(cd_I, "field6", name="ano").text = '2035'

musicas1 = ET.SubElement(cd_I, "Musicas")
ET.SubElement(musicas1, "field1", name="musica01").text = 'Arrocha que ela gosta'
ET.SubElement(musicas1, "field2", name="musica02").text = 'Arrocha que ela gosta 2'

cd_II = ET.SubElement(albuns, "CD_II")
ET.SubElement(cd_II, "field1", name="gravadora").text = "Melhor Que a Outra"
ET.SubElement(cd_II, "field2", name="numMusicas").text = '25'
ET.SubElement(cd_II, "field3", name="artista").text = 'joelzinho dos teclados'
ET.SubElement(cd_II, "field4", name="titulo").text = 'Forro da Peste'
ET.SubElement(cd_II, "field5", name="genero").text = 'Pizadinha do Forro'
ET.SubElement(cd_II, "field6", name="ano").text = '2055'

musicas2 = ET.SubElement(cd_II, "Musicas")
ET.SubElement(musicas2, "field1", name="musica01").text = 'Na Casa da Dinda Eu Fui Feliz'
ET.SubElement(musicas2, "field2", name="musica02").text = 'Apaga a Luz e Vem Rebolar'

tree = ET.ElementTree(locadora)
tree.write(os.path.join('disciplinas/Analise_de_Dados_Nao_Estruturados', "Locadoura_que_sobrou.xml"))
