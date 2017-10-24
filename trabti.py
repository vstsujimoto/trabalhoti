#Trabalho de TI -compactador e descompactador huffman-
#Ricardo Castro 	11/0151884
#Victor Tsujimoto 	09/0134885
#este trabalho foi feito em python ver3.6


# Entrada
def saida():
	print('==========================================');
	print('\nEntropia:');
	print('\nComprimento médio:');
	print('\nTaxa de compressão:');

# Saida


#função para compactar
def comp(arquivo):
	arq = open(arquivo,'r+')
	print("modo compactação")

#função para descompactar
def descomp(arquivo):
	print("modo descompactação")

# Entrada
print("bem vindo ao C-D huffman!")
modo = input("Em que modo deseja operar?\n(pressione -c para modo compactação e -d para descompactação)")

if(modo=='c'):
	arquivo = input("qual arquivo deseja compactar?")
	comp(arquivo)
elif (modo=='d'):
	arquivo = input("qual arquivo deseja descompactar?")
	descomp(arquivo)
else:
	print("Opção Inválida. Exit!")
# Saida
saida()
