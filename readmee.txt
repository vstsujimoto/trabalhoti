Trabalho de TI -compactador e descompactador huffman-
Ricardo Castro 	11/0151884
Victor Tsujimoto 	09/0134885

#este trabalho foi feito em python ver3.6

README

O programa cont�m duas fun��es principais, comp() para gerar o arquivo comprimido e descom() para descompactar o arquivo comprimido.
A fun��o comp() utiliza 3 fun��es:
Conta(): 
Recebe o arquivo a ser codificado e retorna uma matriz contendo o par numero de repeti��es/byte.
Tree():
 Recebe a matriz de conta(), e monta a arvore de elementos/ c�digos atrav�s do heap, retornando-o ao final.
Codifica():
 Recebe o heap da fun��o tree(), escreve o arquivo codificado e retorna o tamanho (numero total de bytes do arquivo codificado).
Antes de escrever o arquivo compactavo, foram escritos cada byte seguido pela sequencia de bits do c�digo correspondente.
Para a escrita do arquivo codificado, � interessante notar que python s� faz escrita byte a byte, e para isso foi necess�rio construir esses bytes concatenando os c�digos dos elementos na sequencia at� que tivessem 8bits.
Comp(): 
Por fim, utilizando essas 3 fun��es,  a fun��o comp() calcula a comprimento m�dio do c�digo huffman, a entropia, e a taxa de compress�o e as mostra na tela.

Fun��o descom():
	Como o heap � uma lista, e a heappop() retira o elemento de menor peso, seria invi�vel utiliza-lo para descompactar nosso arquivo. Para isso foram constru�das duas classes, no() e arvore() para construir uma arvore binaria de busca.
Primeiro � lido o cabe�alho, o primeiro byte indica quantos elementos possuir� a arvore. Sabemos que como o arquivo foi escrito byte a byte, o numero m�ximo de elementos poss�veis � 256, ent�o um byte � capaz de indicar qualquer valor at� ate esse limite.
Em seguida com o m�todo insere(),  mapeamos os elementos na �rvore percorrendo-a de acordo com o vetor c�digo dos elementos. Os bytes encontram se nas folhas da �rvore e os demais n�s contem valores None.
Tendo a �rvore constru�da lemos o arquivo compactado bit a bit, para cada bit � verificado se o n� da arvore � uma folha (n�o tem filhos). Se for uma folha o byte da sequ�ncia percorrida at� o momento � gravado no arquivo descompactado e o cursor volta para a raiz da �rvore.
Observa��es:
O arquivo descompactado contem um �d� antes de seu nome, enquanto o compactado contem a extens�o .huff no final de seu nome.
	A fun��o nativa bin quando recebe um inteiro retorna uma string com a sequencia de bits correspondente.
	se utilizarmos [0] seguido de um elemento do tipo byte, teremos seu numero inteiro correspondente.
O C�digo contem v�rios coment�rios, explicando as partes mais importantes

