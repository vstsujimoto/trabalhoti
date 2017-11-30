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
        
#descompacta

with open("teste.txt.huff", "rb") as desc:
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
    byte=desc.read(1)
    while byte:
        vetor = bin(byte[0])
        
    
desc.close()

for i in vetor:
    print(i[0])
    print(i[1])
