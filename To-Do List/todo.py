import os
import ANSI as A

TODO_FILE = "Lista.txt"

def carregar_tarefas():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r", encoding="utf-8") as file:
        tarefas = [linha.strip() for linha in file.readlines()]
    return tarefas

def salvar_tarefas(tarefas):
    with open(TODO_FILE, "w", encoding="utf-8") as file:
        for tarefa in tarefas:
            file.write(tarefa + "\n")

def exibir_tarefas(tarefas):
    if not tarefas:
        print(f"{A.VERMELHO}Nenhuma tarefa na lista!{A.RESET}")
    else:
        print(f"""{A.NEGRITO}{A.SUBLINHADO}\n=== SUAS TAREFAS ==={A.RESET}
                """)
        for i, tarefa in enumerate(tarefas, start=1):
            status = "[X]" if tarefa.startswith("[X]") else "[ ]"
            print(f"{i}. {status} {tarefa[4:]}")  

def adicionar_tarefa(tarefas):
    tarefa = input("Digite a nova tarefa: ").strip()
    if tarefa:
        tarefas.append("[ ] " + tarefa)  
        print(f"{A.FUNDO_AMARELO_BRILHANTE}Tarefa '{tarefa}' adicionada com sucesso!{A.RESET}")

def remover_tarefa(tarefas):
    exibir_tarefas(tarefas)
    try:
        indice = int(input("Digite o número da tarefa que deseja remover: ")) - 1
        if 0 <= indice < len(tarefas):
            removida = tarefas.pop(indice)
            print(f"{A.CIANO_BRILHANTE}Tarefa '{removida[4:]}' removida com sucesso!{A.RESET}")
        else:
            print(f"{A.VERMELHO}Número inválido!{A.RESET}")
    except ValueError:
        print(f"{A.AMARELO}Por favor, insira um número válido!{A.RESET}")

def concluir_tarefa(tarefas):
    exibir_tarefas(tarefas)
    try:
        indice = int(input("Digite o número da tarefa que deseja marcar como concluída: ")) - 1
        if 0 <= indice < len(tarefas):
            if not tarefas[indice].startswith("[X]"):
                tarefas[indice] = "[X]" + tarefas[indice][3:]  
                print(f"{A.VERDE_BRILHANTE}Tarefa '{tarefas[indice][4:]}' marcada como concluída!{A.RESET}")
            else:
                print(f"{A.VERDE}Essa tarefa já está concluída!{A.RESET}")
        else:
            print(f"{A.VERMELHO}Número inválido!{A.RESET}")
    except ValueError:
        print("Por favor, insira um número válido!")

def menu():
    tarefas = carregar_tarefas()
    while True:
        print(f"""{A.NEGRITO}{A.SUBLINHADO}\n=== MENU ==={A.RESET}
                """)
        print("1. Exibir Tarefas")
        print("2. Adicionar Tarefa")
        print("3. Remover Tarefa")
        print("4. Concluir Tarefa")
        print("5. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            exibir_tarefas(tarefas)
        elif opcao == "2":
            adicionar_tarefa(tarefas)
            salvar_tarefas(tarefas)
        elif opcao == "3":
            remover_tarefa(tarefas)
            salvar_tarefas(tarefas)
        elif opcao == "4":
            concluir_tarefa(tarefas)
            salvar_tarefas(tarefas)
        elif opcao == "5":
            salvar_tarefas(tarefas)
            print(f"{A.PRETO}Saindo do programa. Suas tarefas foram salvas!{A.RESET}")
            break
        else:
            print(f"{A.VERMELHO}Opção inválida! Por favor, escolha uma opção válida.{A.RESET}")

if __name__ == "__main__":
    menu()
