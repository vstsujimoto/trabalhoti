#contador de frequencias
    
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
print(freq)
#input()
