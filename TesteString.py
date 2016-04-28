
#class testePalavra
#    def __init__(self)
 
def TestePalavra():
    valoresExtenso = {'real':0 , 'um': 1, 'dois':2, 'tres':3 }
    retorno = ""
    palavras = "um dois tres real"
    palavra = palavras.split()
    for valor in palavra:
        #print(valor)
        print(valoresExtenso[valor])
        
    #print(palavras)

if __name__ == '__main__':
    #unittest.main()
    TestePalavra()