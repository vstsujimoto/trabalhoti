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



#função para compactar
def comp(arquivo):
	print("modo compactação")
	qtdBytes = 1
	with open(arquivo, 'rb') as arq:
	    byte = arq.read(qtdBytes)
	    while byte:
	        byte = arq.read(qtdBytes)
	        print(byte)



#função para descompactar
def descomp(arquivo):
	print("modo descompactação")

# Entrada
print("bem vindo ao C-D huffman!")
modo = input("Em que modo deseja operar?\n(pressione -c para modo compactação e -d para descompactação)")

if(modo=='c' or modo=='-c' or modo=='C' or modo=='-C'):
	arquivo = input("qual arquivo deseja compactar?")




	comp(arquivo)
elif (modo=='d' or modo=='-d' or modo=='D' or modo=='-D'):
	arquivo = input("qual arquivo deseja descompactar?")
	descomp(arquivo)
else:
	print("Opção Inválida. Exit!")
# Saida
saida()
