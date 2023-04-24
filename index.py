import sys

# Funções de operações mátematicas
def soma(numeros):
    total = 0
    for numero in numeros:
        total = total + numero
    print(total)

def subtracao(numeros):
    total = 0
    for numero in numeros:
        total =  total - numero
    print(total)

def multiplicacao(numeros):
    total = 0
    for numero in numeros:
        total =  total * numero
    print(total)

def divisao(numeros):
    total = 0
    for numero in numeros:
        total =  total / numero
    print(total)


# Colhedor de números da fila.
def colherNumeros(operacao):
    numeros = []
    numero = 0
    validador = True

    while validador == True:
        numero = input("Digite um número: | caso não queria mais digitar, digite: '*'\n->")
        if numero.isdigit():
            numero = int(numero)
            numeros.append(numero)

        # Caso não queira digitar mais nenhum valor.
        elif numero == '*':
            # Caso não digite nenhum número no programa.
            if len(numeros) < 2:
                print("-----------------------------------------------------------------------")
                print("É necessário pelo menos 2 números para fazer qualquer cálculo...")
                print("-----------------------------------------------------------------------")
                colherNumeros()
            else:
                validador = False
                if operacao == 1:
                    soma(numeros)
                elif operacao == 2:
                    subtracao(numeros)
            
        # Caso digite algo que não seja um número, o usuário receberá essa mensagem e poderá digitar novamente.
        else:
            print("Digite somente números!")

opcaoSelecionada = int(input("1 - Operações\n2 - Expressão\n0 - Finalizar Programa\n->"))
if opcaoSelecionada != 1 and opcaoSelecionada != 2 and opcaoSelecionada != 0:
    print("Opção inexistente...")

# Menu de Operações.
elif opcaoSelecionada == 1:
    funcaoDesejada = int(input("1 - Adicionar Operação na Fila\n2 - Executar Próxima Operação da Fila\n3 - Executar Todas as Operações da Fila\n0 - Voltar para o menu principal\n->"))
    if funcaoDesejada == 1:
        print("Adicionar Operação na Fila")
        print("------------------------------------------------------------------")
        operacao = int(input("1 - Adição(+)\n2 - Subtração (-)\n3 - Multiplicação (*)\n4 - Divisão (/)\n->"))
        colherNumeros(operacao)
        
    elif funcaoDesejada == 2:
        print("Executar Próxima Operação da Fila")
    elif funcaoDesejada == 3:
        print("Executar Todas as Operações da Fila")
    elif funcaoDesejada == 0:
        print("Voltando...")

# Expressões (Não tem Menu).
elif opcaoSelecionada == 2:
    print("Não há menu")

# Finalizar o programa.
elif opcaoSelecionada == 0:
    print("Finalizando...")
    exit