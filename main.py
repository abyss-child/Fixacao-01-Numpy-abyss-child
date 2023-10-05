import numpy as np

# Criar um array bidimensional com dados diferentes dos utilizados em sala

matr = np.genfromtxt('matr.txt', delimiter=' ', dtype=int)
print(f'Matriz\n{matr}\n')

# Obter dados estatísticos diferentes (pelo menos 3, uma com axis=1, a outra com axis = 0 e a última sem axis)
soma_lin = matr.sum(axis=1)
print(f'Soma das linhas\n{soma_lin}\n')

media_col = matr.mean(axis=0)
print(f'Média das colunas\n{media_col}\n')

max_matr = matr.max()
print(f'Valor máximo da matriz\n{max_matr}\n')

# Obter a transposta da matriz e realizar uma operação com ela
transposta = matr.T
print(f'Transposta\n{transposta}\n')

# Realizar um produto escalar entre duas matrizes ou de um array com uma matriz
matr2 = np.genfromtxt('matr2.txt', delimiter=' ', dtype=int)
prod_esc = np.dot(matr, matr2)
print(f'Produto escalar\n{prod_esc}\n')

# Criar um filtro para a sua matriz
filtro = np.genfromtxt('filtro.txt', delimiter=' ', dtype=bool)
print(f'Filtro\n{filtro}\n')
print(f'Matriz filtrada\n{matr[filtro]}\n')

# Realizar alguma operação aritmética (número com matriz, array com matriz, etc.)
soma = matr + matr2[0, :]
print(f'Soma das matrizes\n{soma}')

# Vincular com o github (código deve estar no repositório sem o venv ou outros arquivos de configuração)

# EXTRA (200XP): Os dados devem vir de algum arquivo externo
