#contador de frequencias

from operator import itemgetter

#cria uma lista sem elementos para mapear os bytes e suas frequencias
freq = []	
with open("teste.txt", "rb") as file:
#le um byte de cada vez
    byte = file.read(1)
    num = 1
    #print(byte)
    while byte:
        par=[byte,num]   
#se a tabela não exite, o primeiro par byte/freq é adicionado
        if not freq:
            freq.append(par)
        else:
            pos=0
            flag=0 #indica se byte foi encontrado
#procura byte na lista, caso seja encontrado sua freq é atualizada
            for line in freq:
                if line[0]==byte:
                    freq[pos][1]+=1
                    flag=1 #byte encontrado
                    break
                else:
                    pos+=1
#se o byte não está na lista, então é adicionado com freq=1
            if flag==0:
                freq.append(par)
        byte = file.read(1)
        #print(byte)
#faz a contagem de quantos bytes tem no arquivo 
file.close()
#ordena lista pela ordem 
freq.sort(key=itemgetter(1))
#conta total de bytes
total =0 
for par in freq:
    total += par[1]
pos = 0
#transforma ocorrencias em percentual
for par in freq:
    freq[pos][1]=round(freq[pos][1]/total,3)
    pos+=1
#mostra matriz    
print(freq)

#input()