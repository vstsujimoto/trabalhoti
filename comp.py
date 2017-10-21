# modo compactador

#criar um vetor com tamanho de um byte = 256 com valores zero
freq = []
for i in range(0,256):
	freq[i]=0

print(freq)
	
file = open("teste.txt", "rb")
byte = file.read(1)
print(byte)
#faz a contagem de quantos bytes tem no arquivo
freq[byte]=freq[byte]+1 
file.close()
input()