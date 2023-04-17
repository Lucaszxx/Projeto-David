opcaoSelecionada = int(input("1 - Operações\n2 - Expressão\n0 - Finalizar Programa\n->"))
if opcaoSelecionada != 1 and opcaoSelecionada != 2 and opcaoSelecionada != 0:
    print("Opção inexistente...")

# Menu de Operações
elif opcaoSelecionada == 1:
    funcaoDesejada = int(input("1 - Adicionar Operação na Fila\n2 - Executar Próxima Operação da Fila\n3 - Executar Todas as Operações da Fila\n0 - Voltar para o menu principal\n->"))
    if funcaoDesejada == 1:
        print("Adicionar Operação na Fila")
        print("------------------------------------------------------------------")
        operacao = int(input("1 - Adição(+)\n2 - Subtração (-)\n3 - Multiplicação (*)\n4 - Divisão (/)\n->"))
        
    elif funcaoDesejada == 2:
        print("Executar Próxima Operação da Fila")
    elif funcaoDesejada == 3:
        print("Executar Todas as Operações da Fila")
    elif funcaoDesejada == 0:
        print("Voltando...")

# Expressões (Não tem Menu)
elif opcaoSelecionada == 2:
    print("Não há menu")

# Finalizar o programa
elif opcaoSelecionada == 0:
    print("Finalizando...")
    exit
    