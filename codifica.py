#contador de frequencias
from heapq import heapify, heappush, heappop

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

#árvore de codificação
freq = conta("teste.txt")
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

totalbits = 8*freq[0][0]

print ("total bits =",totalbits)
print()
del (freq[0][0])

#codifica

#abre arquivo a ser escrito
with open("codificado.txt","w") as codificado:
#abre arquivo a ser lido
    with open ("teste.txt", "rb") as file:
#le byte
        byte = file.read(1)
        while byte:
#procura na matriz pelo byte
            for item in freq[0]:
                if item[0] == byte:
#escreve codigo no novo arquivo
                    codificado.write(item[1])
                    break
            byte=file.read(1)
    file.close()
codificado.close()
