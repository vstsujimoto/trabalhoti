arquivo = input("qual arquivo deseja compactar?")
with open(arquivo, "rb") as f:
    byte = f.read(1)
    while byte:
        # Do stuff with byte.
        byte = f.read(1)
        print(byte)









#tamanho = 1

#with open(arquivo, "rb") as in_file:
    #with open("saida-teste", "wb") as out_file:
#        while True:
#            piece = in_file.read(tamanho)
    #        if piece == "":
        #        break # end of file
            #out_file.write(piece)

#
#from heapq import heappush, heappop, heapify
#from collections import defaultdict
#
#def encode(symb2freq):
#    """Huffman encode the given dict mapping symbols to weights"""
#    heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
#    heapify(heap)
#    while len(heap) > 1:
#        lo = heappop(heap)
#        hi = heappop(heap)
#        for pair in lo[1:]:
#            pair[1] = '0' + pair[1]
#        for pair in hi[1:]:
#            pair[1] = '1' + pair[1]
#        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
#    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
#
##txt = "this is an example for huffman encoding"
#txt = open(arquivo,'r')
#print (txt)
#symb2freq = defaultdict(int)
#for ch in txt:
#    symb2freq[ch] += 1
## in Python 3.1+:
## symb2freq = collections.Counter(txt)
#huff = encode(symb2freq)
#print ("Symbol\tWeight\tHuffman Code")
#for p in huff:
#    print ("%s\t%s\t%s" % (p[0], symb2freq[p[0]], p[1]))
