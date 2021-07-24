from pyUFbr.baseuf import ufbr
from pprint import pprint

#print(help(ufbr))
ufs = ufbr.dict_uf

sigla = input("digite a sigla do estado brasileiro: ")

print(f"O estado é: {(ufs.get(sigla.upper())).get('nome')}")