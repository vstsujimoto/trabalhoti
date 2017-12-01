from heapq import heapify, heappush, heappop
import math

class no(object):

    def __init__(self):
        self.valor = None
        self.esquerda = None
        self.direita = None
        
    def atribui(self, valor):
        self.valor=valor

class arvore(object):

    def __init__(self):
        self.raiz = no()

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

    def temfilho(self,noatual, c):
        if (c=='0'):
            if (noatual.esquerda):
                return True
        elif (c=='1'):
            if (noatual.direita):
                return True
        else:
            return False
        
#descompacta

with open("teste.txt.huff", "rb")as desc, open("descompactado.txt", "wb")as novo :
    cab = desc.read(1)
    tamanho = cab[0] +1
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

    arvore = arvore()
#insere todos os valores na arvore
    for i in vetor:
        arvore.insere(arvore.raiz,i[0],i[1])

#converte o arquivo para forma legivel
    #byte=desc.read(1)
    #print(byte)
    array=[]
    root=arvore.raiz
    while byte:
        if len(array)==0:
            byte=desc.read(1)
            #print(byte)
            vetor = bin(byte[0])
            vetor = vetor[2:]
            #print(vetor)
            vetorr=[]
            for i in vetor:
                vetorr.append(i)
            while len(vetorr)<8:
                vetorr.insert(0,'0')
            array+=vetorr
            vetor=[]
#se vetor nao esta vazio
        elif len(array)>0:
            #print(array)
            c=array.pop(0)
            #print(c)
#se no tem filhos
            if arvore.temfilho(root,c)==True:
                #print("true")
                if c=='0':
                    root=root.esquerda
                elif c=='1':
                    root=root.direita
#se nao tiver filhos
            else:
                #print("false")
                novo.write(root.valor)
                array.insert(0,c)
                #print(root.valor)
                root=arvore.raiz
        
        
    
desc.close()
novo.close()
