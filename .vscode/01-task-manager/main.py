# print() é usado para exibir informações na tela
# Exibe o nome do nosso programa
tarefas = []  # Lista vazia para armazenar as tarefas

while True: # Enquanto a condição for verdadeira, o código dentro do while será executado.
        print("Task Manager")
    # Exibe uma linha para separar o título do restante do conteúdo
        print("--------------------")
    # Exibe as opções disponíveis para o usuário no menu
        print("1- Ver Tarefas") # ver as tarefas cadastradas
        print("2- Adicionar Tarefa") # Adiciona uma nova tarefa 
        print("3- Concluir Tarefa") # Conclui uma tarefa cadastrada
        print("4- Sair") # Sai do programa
        print("--------------------")

        opcao = input("Digite a Opção desejada:") # Solicita que o usuário digite a opção desejada
        # = Serve para guardar o valor (informação) digitado 


        if opcao == "1": 
            print("Ver Tarefas") 
        for tarefa in tarefas: # passa pelas tarefas que estão cadastradas.
            print(tarefa)
        if opcao == "2": 
            print("Adicionar Tarefa") 
            tarefa = input("Digite a tarefa que deseja adicionar: ")
            tarefas.append(tarefa) # Adiciona a tarefa digitada na lista de tarefas
        if opcao == "3": 
            print("Concluir Tarefa") 
        if opcao == "4": 
            print("Sair") 
            break

