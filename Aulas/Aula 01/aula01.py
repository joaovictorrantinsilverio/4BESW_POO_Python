# Declaração de Variáveis
idade = 10
print('Idade:', idade)

nome = 'Alice'
print('Nome:', nome)

valor_de_pi = 3.14
print('Valor de π:', valor_de_pi)

print() # Pulando uma linha

# Operadores Aritméticos
num1 = 5
num2 = 3

soma = num1 + num2
print(f'Soma dos números {num1} e {num2} é.........: {soma}')

multiplicacao = num1 * num2
print(f'Multiplicação dos números {num1} e {num2} é: {multiplicacao}')

subtracao = num1 - num2
print(f'Subtração dos números {num1} e {num2} é....: {subtracao}')

divisao = num1 / num2
print(f'Divisão dos números {num1} e {num2} é......: {divisao}')

print() # Pulando uma linha

# Operadores de Atribuição
x = 5
print('Valor inicial de x:', x)

x += 2
print('Valor de x após x += 2:', x)

x -= 3
print('Valor de x após x -= 3:', x)

x *= 4
print('Valor de x após x *= 4:', x)

x /= 2
print('Valor de x após x /= 2:', x)

# Operadores de Comparação
if soma > 10:
    print('A soma é maior que 10')
else:
    print('A soma não é maior que 10')

if soma < 10:
    print('A soma é menor que 10')
else:
    print('A soma não é menor que 10')

# Podemos utilizar também:
# == (igual)
# != (diferente)
# <= (menor ou igual)
# >= (maior ou igual)

# Operadores Lógicos
idade_tioPaulo = 69
idade_Maria = 15

print() # Pulando uma linha

# Operador 'OR'
if idade_tioPaulo >= 18 or idade_Maria >= 18:       # Retorna True se todas as condições forem verdadeiras; caso contrário, retorna False
    print('Pelo menos uma das pessoas é maior de idade')
else:
    print('Nenhuma das pessoas é maior de idade')

# Operador 'AND'
if idade_tioPaulo >= 18 and idade_Maria >= 18:      # Retorna True se pelo menos uma das condições for verdadeira; casocontrário, retorna False. 
    print('Ambas as pessoas são maiores de idade')
else:
    print('Pelo menos uma das pessoas não é maior de idade')

# Operador 'NOT' (inverte o sinal lógico)
if not (idade_Maria >= 18):                 # Inverte o resultado lógico: se a expressão for True, retorna False; se forFalse, retorna True.
    print('Maria é menor de idade')

print() # Pulando uma linha

# Operadores de identidade
time_alunos = 'Vasco'
time_professor = 'Corinthians'

# Demonstração do operador 'is'
if time_alunos is time_professor:               # Operador 'is' retorna true caso ambas as variáveis apontam o mesmo objeto na memória.
    print('time_alunos e time_professor são o mesmo objeto.')
else:
    print('time_alunos e time_professor são objetos diferentes.')

# Demonstração do operador 'is not'
if time_alunos is not time_professor:          # Operador 'is not' retorna true caso ambas as variáveis apoontem para objetos diferentes na memória.
    print('time_alunos NÃO é o mesmo que time_professor')

print() # Pulando uma linha

# Operadores de Associação
frutas = ['maçã', 'banana', 'pera', 'uva', 'goiaba', 'abacaxi']

fruta1 = 'goiaba'
fruta2 = 'kiwi'

# Retorna True caso o valor seja encontrado na sequência; casocontrário, retorna False.
print('Tem essa fruta?....:', fruta1 in frutas)
print('Tem essa fruta?....:', fruta2 in frutas)

# Retorna True caso o valor não seja encontrado na sequência; casocontrário, retorna False.
print('Não tem essa fruta?:', fruta2 not in frutas)