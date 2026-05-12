import json
import os
tarefas = []
if os.path.exists("tarefas.json"):

    with open("tarefas.json", "r") as arquivos:
       tarefas = json.load(arquivos)

while True:
    print ("=== Gerenciador de Tarefas ===\n1. Adicionar tarefa\n2. Listar tarefas\n3. Concluir tarefa\n4. Remover tarefa\n5. Sair")
    opçao = input("Escolha uma das opções acima: ")
    if opçao == "5":
        with open("tarefas.json", "w") as arquivos:
            json.dump(tarefas, arquivos)
        break
    elif opçao == "1":
        rpst_tarefa = input("O que deseja adicionar a lista: ")
        tarefas.append(rpst_tarefa)
    elif opçao == "2" :
        for rpst_tarefa in tarefas:
            print(rpst_tarefa)
    elif opçao =="4":
        remover = input("Qual item da lista você quer remover: ")
        if remover in tarefas:
            tarefas.remove(remover)
        else:
            print("Este item não está na lista de tarefas.")
    elif opçao == "3":
        concluir = input("Qual tarefa você deseja concluir: ")
        if concluir in tarefas:       
            posicao = tarefas.index(concluir)
            tarefas[posicao] = concluir + " ✅"   
        else:                          
         print("Este item não está na lista de tarefas.")
