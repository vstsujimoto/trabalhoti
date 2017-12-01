Trabalho de TI -compactador e descompactador huffman-
Ricardo Castro 	11/0151884
Victor Tsujimoto 	09/0134885

#este trabalho foi feito em python ver3.6

README

O programa contém duas funções principais, comp() para gerar o arquivo comprimido e descom() para descompactar o arquivo comprimido.
A função comp() utiliza 3 funções:
Conta(): 
Recebe o arquivo a ser codificado e retorna uma matriz contendo o par numero de repetições/byte.
Tree():
 Recebe a matriz de conta(), e monta a arvore de elementos/ códigos através do heap, retornando-o ao final.
Codifica():
 Recebe o heap da função tree(), escreve o arquivo codificado e retorna o tamanho (numero total de bytes do arquivo codificado).
Antes de escrever o arquivo compactavo, foram escritos cada byte seguido pela sequencia de bits do código correspondente.
Para a escrita do arquivo codificado, é interessante notar que python só faz escrita byte a byte, e para isso foi necessário construir esses bytes concatenando os códigos dos elementos na sequencia até que tivessem 8bits.
Comp(): 
Por fim, utilizando essas 3 funções,  a função comp() calcula a comprimento médio do código huffman, a entropia, e a taxa de compressão e as mostra na tela.

Função descom():
	Como o heap é uma lista, e a heappop() retira o elemento de menor peso, seria inviável utiliza-lo para descompactar nosso arquivo. Para isso foram construídas duas classes, no() e arvore() para construir uma arvore binaria de busca.
Primeiro é lido o cabeçalho, o primeiro byte indica quantos elementos possuirá a arvore. Sabemos que como o arquivo foi escrito byte a byte, o numero máximo de elementos possíveis é 256, então um byte é capaz de indicar qualquer valor até ate esse limite.
Em seguida com o método insere(),  mapeamos os elementos na árvore percorrendo-a de acordo com o vetor código dos elementos. Os bytes encontram se nas folhas da árvore e os demais nós contem valores None.
Tendo a árvore construída lemos o arquivo compactado bit a bit, para cada bit é verificado se o nó da arvore é uma folha (não tem filhos). Se for uma folha o byte da sequência percorrida até o momento é gravado no arquivo descompactado e o cursor volta para a raiz da árvore.
Observações:
O arquivo descompactado contem um ‘d’ antes de seu nome, enquanto o compactado contem a extensão .huff no final de seu nome.
	A função nativa bin quando recebe um inteiro retorna uma string com a sequencia de bits correspondente.
	se utilizarmos [0] seguido de um elemento do tipo byte, teremos seu numero inteiro correspondente.
O Código contem vários comentários, explicando as partes mais importantes

