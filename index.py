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
    total = 1
    for numero in numeros:
        total = total * numero
    print(total)


def divisao(numeros):
    total = numeros[0]
    for numero in numeros[1:]:
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
contador = 0


def menuOperacoes():
    funcaoDesejada = int(input(
        "1 - Adicionar Operação na Fila\n2 - Executar Próxima Operação da Fila\n3 - Executar Todas as Operações da Fila\n0 - Voltar para o menu principal\n->"))

    # Função que adiciona uma operação a fila de operações
    if funcaoDesejada == 1:
        print("Adicionar Operação na Fila")
        print("------------------------------------------------------------------")
        operacao = int(input(
            "1 - Adição(+)\n2 - Subtração (-)\n3 - Multiplicação (*)\n4 - Divisão (/)\n->"))
        colherNumeros(operacao)

    # FAZENDO AGORA!!!!!!!!!
    elif funcaoDesejada == 2:
        print("Executar Próxima Operação da Fila")
        tipo = filaDeOperacoes[contador][contador]
        valores = filaDeOperacoes[contador][1]

        if tipo == 'somar':
            print("---------------------------------------------")
            print(f"Tipo de operação: {tipo}")
            print("---------------------------------------------")
            print("Os valores são:")
            # remove os colchetes das listas
            print('%s' % ' + '.join(map(str, valores)))
            print("---------------------------------------------")
            print("O resultado da soma é:")
            operacoes["somar"](valores)
            print("---------------------------------------------")
            return menuOperacoes()

        elif tipo == 'subtrair':
            print("---------------------------------------------")
            print(f"Tipo de operação: {tipo}")
            print("---------------------------------------------")
            print("Os valores são:")
            # remove os colchetes das listas
            print('%s' % ' - '.join(map(str, valores)))
            print("---------------------------------------------")
            print("O resultado da subtração é:")
            operacoes["subtrair"](valores)
            print("---------------------------------------------")
            return menuOperacoes()

        elif tipo == 'multiplicar':
            print("---------------------------------------------")
            print(f"Tipo de operação: {tipo}")
            print("---------------------------------------------")
            # remove os colchetes das listas
            print("Os valores são:")
            print('%s' % ' x '.join(map(str, valores)))
            print("---------------------------------------------")
            print("O resultado da multiplicação é:")
            operacoes["multiplicar"](valores)
            print("---------------------------------------------")
            return menuOperacoes()

        elif tipo == 'dividir':
            print("---------------------------------------------")
            print(f"Tipo de operação: {tipo}")
            print("---------------------------------------------")
            print("Os valores são:")
            # remove os colchetes das listas
            print('%s' % ' / '.join(map(str, valores)))
            print("---------------------------------------------")
            print("O resultado da divisão é:")
            operacoes["dividir"](valores)
            print("---------------------------------------------")
            return menuOperacoes()
            
    # Executa todas as operações dentro da fila de operações
    elif funcaoDesejada == 3:
        if len(filaDeOperacoes) == 0:
            print("A fila de operações está vazia!")
        else:
            print("Executar Todas as Operações da Fila")
            for tipoOperacao, numeros in filaDeOperacoes:
                if tipoOperacao == 'somar':
                    print("---------------------------------------------")
                    print(f"Tipo de operação: {tipoOperacao}")
                    print("---------------------------------------------")
                    print("Os valores são:")
                    # remove os colchetes das listas
                    print('%s' % ' + '.join(map(str, numeros)))
                    print("---------------------------------------------")
                    print("O resultado da soma é:")
                    operacoes["somar"](numeros)
                    print("---------------------------------------------")

                elif tipoOperacao == 'subtrair':
                    print("---------------------------------------------")
                    print(f"Tipo de operação: {tipoOperacao}")
                    print("---------------------------------------------")
                    print("Os valores são:")
                    # remove os colchetes das listas
                    print('%s' % ' - '.join(map(str, numeros)))
                    print("---------------------------------------------")
                    print("O resultado da subtração é:")
                    operacoes["subtrair"](numeros)
                    print("---------------------------------------------")

                elif tipoOperacao == 'multiplicar':
                    print("---------------------------------------------")
                    print(f"Tipo de operação: {tipoOperacao}")
                    print("---------------------------------------------")
                    # remove os colchetes das listas
                    print("Os valores são:")
                    print('%s' % ' x '.join(map(str, numeros)))
                    print("---------------------------------------------")
                    print("O resultado da multiplicação é:")
                    operacoes["multiplicar"](numeros)
                    print("---------------------------------------------")

                elif tipoOperacao == 'dividir':
                    print("---------------------------------------------")
                    print(f"Tipo de operação: {tipoOperacao}")
                    print("---------------------------------------------")
                    print("Os valores são:")
                    # remove os colchetes das listas
                    print('%s' % ' / '.join(map(str, numeros)))
                    print("---------------------------------------------")
                    print("O resultado da divisão é:")
                    operacoes["dividir"](numeros)
                    print("---------------------------------------------")

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
                print(
                    "-----------------------------------------------------------------------")
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
