import sys
import numpy as np

if __name__ == "__main__":
    print(f'Quantos argumentos: {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i}: {arg}")


# Abrindo os arquivos de entrada e saida
entrada = open(sys.argv[1], "r+")
saida = open(sys.argv[2], "w+")

linha = entrada.readline()  # P2
linha = entrada.readline()  # Comentário
linha = entrada.readline()  # Dimensões
dimensoes = linha.split()
largura = dimensoes[0]
altura = dimensoes[1]
linha = entrada.readline()  # Valor fixo

linha = entrada.readlines()  # Ler o restante do arquivo e grava como lista

# converter e grava como lista

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

for i in range(len(imagem)):
    n = 255 - imagem[i]
    n = str(n)
    saida.write(n)
    saida.write("\n")


# sempre fechar os dois arquivos
entrada.close()
saida.close()
