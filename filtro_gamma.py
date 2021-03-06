import sys
import numpy as np

if __name__ == "__main__":
    print(f'Quantos argumentos: {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i}: {arg}")

entrada = open(sys.argv[1], "r+")
saida = open(sys.argv[2], "w+")

linha = entrada.readline()  # P2
linha = entrada.readline()  # comentário
linha = entrada.readline()  # Dimensões
dimensoes = linha.split()
largura = dimensoes[0]
altura = dimensoes[1]
print(largura, altura)
linha = entrada.readline()  # Valor fixo

linha = entrada.readlines()  # ler o restante do arquivo e grava como lista

# converter de lista para array
imagem = np.asarray(linha, dtype=int)
print(imagem)

# escrevendo a imagem cópia
saida.write("P2\n")
saida.write("#Criado por Gildo\n")
saida.write(largura)
saida.write(" ")
saida.write(altura)
saida.write("\n")
saida.write("255\n")
# fator gama
gama = 10

# fazer a transformação de intesidade (negativo)
for i in range((len(imagem))):
   # n = 255 - imagem[i] #negativo
    n = int(((imagem[i]/255)**gama)*255)
    n = str(n)
    # este comando write só aceita string, por isso foi preciso converter
    saida.write(n)
    saida.write("\n")
    # estamos jogando em uma array, se fosse utilizarmos a distância euclidiana precisamos de matriz


print(type(linha))  # do tipo lista <class 'list'>
print(len(linha))  # tamanho 373700


# fechar os dois arquivos
entrada.close()
saida.close()
