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
#se a tabela não exite, o primeiro par num/byte é adicionado
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
heapify(freq)
#a árvore de codificação será montada em uma lista, utilizando o conceito de heap
#ao final, o último elemento da lista será o nó raiz com a soma total dos elementos, assim não haverá mais iterações necessárias
while len(freq) > 1:
#menor elemento é mapeado à esquerta
        lef = heappop(freq)
#segundo menor é mapeado à direita
        rig = heappop(freq)
#atribui codigo aos elementos removidos
        for par in lef[1:]:
            par[1] = '0' + par[1]
        for par in rig[1:]:
            par[1] = '1' + par[1]
#coloca um novo elemento na arvore correspondente à soma dos elementos removidos
        heappush(freq, [lef[0] + rig[0]] + lef[1:] + rig[1:])

totalbits = 8*freq[0][0]
print ("total bits =",totalbits)
print()
for item in freq:
    for sub in item:
        print(sub)
        
#input()
