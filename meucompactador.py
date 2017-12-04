#Trabalho de TI -compactador e descompactador huffman-
#Ricardo Castro 	11/0151884
#Victor Tsujimoto 	09/0134885
#este trabalho foi feito em python ver3.6


from heapq import heapify, heappush, heappop
import math

#classe cria objeto nó
class no(object):

    def __init__(self):
        self.valor = None
        self.esquerda = None
        self.direita = None
        
    def atribui(self, valor):
        self.valor=valor

#classe que cria o objeto arvore
class arvore(object):

    def __init__(self):
        self.raiz = no()

#insere nó na arvore de huffman, recebe o byte o e o vetor do com os bits do codigo
    def insere(self, noatual, byte, cod):
        for i in cod:
            if i=='0':
                if (noatual.esquerda):
                    noatual=noatual.esquerda
                else:
                    noatual.esquerda=no()
                    noatual=noatual.esquerda
                    
            if i=='1':
                if (noatual.direita):
                    noatual=noatual.direita
                else:
                    noatual.direita=no()
                    noatual=noatual.direita
        noatual.valor=byte
#verifica se determinado nó tem filhos
    def temfilho(self,noatual, c):
        if (c=='0'):
            if (noatual.esquerda):
                return True
        elif (c=='1'):
            if (noatual.direita):
                return True
        else:
            return False


#contador de frequencias

def conta(arquivo):
#cria uma lista sem elementos para mapear os bytes e suas frequencias
    freq = []
    with open(arquivo, "rb") as file:
#le um byte de cada vez
        byte = file.read(1)
        num = 1
        cod =''
        while byte:
            par=[num,[byte,cod]]
#se a tabela não existe, o primeiro par num/byte é adicionado
            if not freq:
                freq.append(par)
            else:
                pos=0
                flag=0 #indica se byte foi encontrado
#procura byte na lista, caso seja encontrado sua freq é atualizada
                for line in freq:
                    if line[1][0]==byte:
                        freq[pos][0]+=1
                        flag=1 #byte encontrado
                        break
                    else:
                        pos+=1
#se o byte não está na lista, então é adicionado com freq=1
                if flag==0:
                    freq.append(par)
            byte = file.read(1)
    file.close()
    return freq
#fim do contador de freq



#árvore de codificação, recebe matriz de frequencias da função conta()
def tree(freq):
#a árvore de codificação será montada em uma lista, utilizando o conceito de heap
    heapify(freq)
#ao final, o último elemento da lista será o nó raiz com a soma total dos elementos, assim não haverá mais iterações necessárias
    while len(freq) > 1:
#menor elemento é mapeado à esquerda
        lef = heappop(freq)
#segundo menor é mapeado à direita
        rig = heappop(freq)
#atribui codigo aos elementos removidos
        for par in lef[1:]:
            par[1] = '0' + par[1]
        for par in rig[1:]:
            par[1] = '1' + par[1]
#adiciona um novo elemento à arvore com peso correspondente à soma dos pesos dos elementos removidos
#os elementos removidos são concatenados à esse novo elemento
        heappush(freq, [lef[0] + rig[0]] + lef[1:] + rig[1:])
    return freq
#fim da função que monta a arvore de codigos



#codifica
#recebe arvore e codifica o arquivo a ser compactado
def codifica(arvore,novo,arquivo):
    del (arvore[0][0])
    tamanho=0
#abre arquivo a ser escrito e arquivo a ser lido
    with open(novo,"wb") as codificado, open (arquivo, "rb") as file:
        #escreve cabeçalho contendo a arvore
        #escreve numero de pares byte/codigo
        codificado.write(bytes([len(arvore[0])-1]))
        tamanho+=1
        for par in arvore[0]:
            codificado.write(par[0])
            tamanho+=1
            for i in par[1]:
                codificado.write(bytes([ord(i)]))
                tamanho+=1
            codificado.write(bytes([ord(' ')]))
            tamanho+=1
#le byte
        byte = file.read(1)
        array=''
        escreve=''
        while byte:
#procura na matriz pelo byte
            for item in arvore[0]:
                if item[0]==byte:
#escreve byte a byte os codigos no novo arquivo
                    for i in item[1]:
                        array+=i
                    if len(array)>=8:
                        escreve=int(array[:8],2)
                        escreve=bytes([escreve])
                        codificado.write(escreve)
                        tamanho+=1
                        array=array[8:]
                    break
            byte=file.read(1)
#completa com 1s o ultimo byte a ser escrito
        if len(array)<8:
            escreve=array
            restam=8-len(array)
            while restam>0:
                escreve+='1'
                restam-=1
            escreve=bytes([int(escreve,2)])
            codificado.write(escreve)
            tamanho+=1
    file.close()
    codificado.close()
    return tamanho
#fim codifica

#compactador
def comp(arquivo):
    freq = conta(arquivo)
    arvore = tree(conta(arquivo))
    totalbytes = arvore[0][0]
    tamanho=codifica(arvore,arquivo+".huff",arquivo)

#comprimento medio
    l=0
#entropia
    h=0
#calcula L e H(x)
    for par in freq:
        for item in arvore[0]:
            if item[0]==par[1][0]:
#par[1]/totalbytes=frequencia em percentual, item[1]=n de bits
                p=par[0]/totalbytes
                l=l+ p*len(item[1])
                h=h-p*math.log(p,2)
                break

    print("Lav =",round(l,2))
    print("H(x) =",round(h,2))
    print("taxa de compressão =", round(totalbytes/tamanho,2))
#fim compactador

#função para descompactar
def descom(comprimido):
#abre arquivo comprimido e cria o arquivo descompactado
    with open(comprimido, "rb")as desc, open('d'+comprimido[:len(comprimido)-5], "wb")as novo :
#o primeiro byte é referente ao numero de palavras que foram codificadas
        cab = desc.read(1)
        tamanho = cab[0] +1
#vetor que armazenará os pares byte/codigo
        vetor=[]
        while tamanho>0:
#byte
            byte= desc.read(1)
            tamanho-=1
#codigo huffman do byte
            cod=[]
            bit = desc.read(1)
            while bit !=b' ':
                cod+=chr(bit[0])
                bit = desc.read(1)
#monta vetor com pares byte/codigo
            vetor+=[[byte,cod]]
#termina de ler o cabeçalho
#cria arvore
        arvoree = arvore()
#insere todos os valores na arvore
        for i in vetor:
            arvoree.insere(arvoree.raiz,i[0],i[1])

#converte o arquivo para forma legivel

        array=[]
        root=arvoree.raiz
        while byte:
            if len(array)==0:
                byte=desc.read(1)
#transforma byte em uma sring de bits
                if byte:
                    vetor = bin(byte[0])
                else:
                    break
#remove "0b" de cada byte lido
                vetor = vetor[2:]
#vetor na forma ['0', '0', '0', ...] por exemplo
                vetorr=[]
                for i in vetor:
                    vetorr.append(i)
#se o valor do byte nao tiver 8 bits, completa com zeros no inicio
                while len(vetorr)<8:
                    vetorr.insert(0,'0')
                array+=vetorr
                vetor=[]
#se array nao esta vazio
            elif len(array)>0:
                c=array.pop(0)
#se no tem filhos percorre a arvore
                if arvoree.temfilho(root,c)==True:
                    if c=='0':
                        root=root.esquerda
                    elif c=='1':
                        root=root.direita
#se nao tiver filhos é um byte de codigo, pois estes são folhas
                else:
                    novo.write(root.valor)
                    array.insert(0,c)
                    root=arvoree.raiz
        
        
#fecha arquivos
    desc.close()
    novo.close()
    print("descompactado!")
    
# Entrada
print("bem vindo ao C-D huffman!")
modo = input("Em que modo deseja operar?\n(pressione -c para modo compactação e -d para descompactação)\n")

if(modo=='c' or modo=='-c' or modo=='C' or modo=='-C'):
	arquivo = input("qual arquivo deseja compactar?\n")
	print()
	comp(arquivo)
elif (modo=='d' or modo=='-d' or modo=='D' or modo=='-D'):
	arquivo = input("qual arquivo deseja descompactar?\n")
	descom(arquivo)
else:
	print("Opção Inválida. Exit!")
print("pressione qualquer tecla para sair")
input()

