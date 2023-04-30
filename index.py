import sys


# Funções de operações mátematicas
def soma(numeros):
    total = 0
    for numero in numeros:
        total = total + numero
    print(total)


def subtracao(numeros):
    total = numeros[0]
    for numero in numeros[1:]:
        total = total - numero
    print(total)


def multiplicacao(numeros):
    total = 0
    for numero in numeros:
        total = total * numero
    print(total)


def divisao(numeros):
    total = 0
    for numero in numeros:
        total = total / numero  
    print(total)

# Array de operações matemáticas
operacoes = {
    'somar': soma,
    'subtrair': subtracao,
    'multiplicar': multiplicacao,
    'dividir': divisao
}


# Menu de operaçoes matématicas e fila
filaDeOperacoes = []
def menuOperacoes():
    funcaoDesejada = int(input(
        "1 - Adicionar Operação na Fila\n2 - Executar Próxima Operação da Fila\n3 - Executar Todas as Operações da Fila\n0 - Voltar para o menu principal\n->"))
    
    # Função que adiciona uma operação a fila de operações
    if funcaoDesejada == 1:
        print("Adicionar Operação na Fila")
        print(
            "------------------------------------------------------------------")
        operacao = int(input(
            "1 - Adição(+)\n2 - Subtração (-)\n3 - Multiplicação (*)\n4 - Divisão (/)\n->"))
        colherNumeros(operacao)
    
    elif funcaoDesejada == 2:
        print("Executar Próxima Operação da Fila")
    
    # Executa todas as operações dentro da fila de operações    
    elif funcaoDesejada == 3:
        print("Executar Todas as Operações da Fila")
        for tipoOperacao, numeros in filaDeOperacoes:
            if tipoOperacao == 'somar':
                operacoes["somar"](numeros)
                
            elif tipoOperacao == 'subtrair':
                operacoes["subtrair"](numeros)
                
            elif tipoOperacao == 'multiplicar':
                operacoes["multiplicar"](numeros)

            elif tipoOperacao == 'dividir':
                operacoes["dividir"](numeros)
            
    elif funcaoDesejada == 0:
        print("Voltando...")


# Menu principal.
def menu():
    opcaoSelecionada = int(
        input("1 - Operações\n2 - Expressão\n0 - Finalizar Programa\n->"))

    if opcaoSelecionada != 1 and opcaoSelecionada != 2 and opcaoSelecionada != 0:
        print("Opção inexistente...")
    if opcaoSelecionada == 1:
        menuOperacoes()

    # Expressões (Não tem Menu).
    elif opcaoSelecionada == 2:
        print("Não há menu")

    # Finalizar o programa.
    elif opcaoSelecionada == 0:
        print("Finalizando...")
        exit

# Colhedor de números.
def colherNumeros(operacao):
    numeros = []
    numero = 0
    validador = True

    while validador == True:
        numero = input(
            "Digite um número: | caso não queria mais digitar, digite: '*'\n->")
        if numero.isdigit():
            numero = int(numero)
            numeros.append(numero)

        # Caso não queira digitar mais nenhum valor.
        elif numero == '*':
            # Caso não digite nenhum número no programa.
            if len(numeros) < 2:
                print(
                    "-----------------------------------------------------------------------")
                print("É necessário pelo menos 2 números para fazer qualquer cálculo...")
                print("-----------------------------------------------------------------------")
                colherNumeros()
            else:
                validador = False
                if operacao == 1:
                    filaDeOperacoes.append(['somar', numeros])
                    print("Fila de operações", filaDeOperacoes)
                    menuOperacoes()

                elif operacao == 2:
                    filaDeOperacoes.append(['subtrair', numeros])
                    print("Fila de operações", filaDeOperacoes)
                    menuOperacoes()
                    
                # Corrigir a função pois está retornando o valor 0
                elif operacao == 3:
                    filaDeOperacoes.append(['multiplicar', numeros])
                    print("Fila de operações", filaDeOperacoes)
                    menuOperacoes()
                
                # Corrigir a função pois está retornando o valor 0
                elif operacao == 4:
                    filaDeOperacoes.append(['dividir', numeros])
                    print("Fila de operações", filaDeOperacoes)
                    menuOperacoes()

        # Caso digite algo que não seja um número, o usuário receberá essa mensagem e poderá digitar novamente.
        else:
            print("Digite somente números!")
            
# Iniciar programa
menu()
