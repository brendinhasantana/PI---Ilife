import json
import os

# Arquivo onde as consultas serão armazenadas
ARQUIVO_CONSULTAS = 'consultas.json'


def carregar_consultas():
    if os.path.exists(ARQUIVO_CONSULTAS):
        with open(ARQUIVO_CONSULTAS, 'r') as f:
            return json.load(f)
    else:
        return []

# salvar consultas no arquivo JSON
def salvar_consultas(consultas):
    with open(ARQUIVO_CONSULTAS, 'w') as f:
        json.dump(consultas, f, indent=4)

# cadastrar uma nova consulta
def cadastrar_consulta():
    paciente = input("Nome do paciente: ")
    data = input("Data da consulta (dd/mm/aaaa): ")
    hora = input("Hora da consulta (hh:mm): ")
    motivo = input("Motivo da consulta: ")

    consulta = {
        'id': len(consultas) + 1,
        'paciente': paciente,
        'data': data,
        'hora': hora,
        'motivo': motivo
    }

    consultas.append(consulta)
    salvar_consultas(consultas)
    print("\nConsulta cadastrada com sucesso!")

# exibir as consultas cadastradas
def exibir_consultas():
    if consultas:
        print("\nConsultas cadastradas:")
        for consulta in consultas:
            print(f"\nID: {consulta['id']}")
            print(f"Paciente: {consulta['paciente']}")
            print(f"Data: {consulta['data']}")
            print(f"Hora: {consulta['hora']}")
            print(f"Motivo: {consulta['motivo']}")
            print('-' * 30)
    else:
        print("\nNão há consultas cadastradas.")

# excluir uma consulta
def excluir_consulta():
    exibir_consultas()
    try:
        id_consulta = int(input("\nDigite o ID da consulta que deseja excluir: "))
        consulta_encontrada = next((consulta for consulta in consultas if consulta['id'] == id_consulta), None)
        
        if consulta_encontrada:
            consultas.remove(consulta_encontrada)
            salvar_consultas(consultas)
            print(f"\nConsulta com ID {id_consulta} excluída com sucesso!")
        else:
            print("\nConsulta não encontrada.")
    except ValueError:
        print("\nID inválido!")

# editar consulta
def editar_consulta():
    exibir_consultas()
    try:
        id_consulta = int(input("\nDigite o ID da consulta que deseja editar: "))
        consulta_encontrada = next((consulta for consulta in consultas if consulta['id'] == id_consulta), None)
        
        if consulta_encontrada:
            print("\nEditando consulta...")
            paciente = input(f"Nome do paciente ({consulta_encontrada['paciente']}): ") or consulta_encontrada['paciente']
            data = input(f"Data da consulta ({consulta_encontrada['data']}): ") or consulta_encontrada['data']
            hora = input(f"Hora da consulta ({consulta_encontrada['hora']}): ") or consulta_encontrada['hora']
            motivo = input(f"Motivo da consulta ({consulta_encontrada['motivo']}): ") or consulta_encontrada['motivo']

            consulta_encontrada['paciente'] = paciente
            consulta_encontrada['data'] = data
            consulta_encontrada['hora'] = hora
            consulta_encontrada['motivo'] = motivo
            
            salvar_consultas(consultas)
            print(f"\nConsulta com ID {id_consulta} editada com sucesso!")
        else:
            print("\nConsulta não encontrada.")
    except ValueError:
        print("\nID inválido!")

# mostrar o menu e receber a escolha do usuário
def exibir_menu():
    while True:
        print("\n===== Clínica de Nutrição =====")
        print("1. Cadastrar consulta")
        print("2. Exibir todas as consultas")
        print("3. Excluir consulta")
        print("4. Editar consulta")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            cadastrar_consulta()
        elif escolha == '2':
            exibir_consultas()
        elif escolha == '3':
            excluir_consulta()
        elif escolha == '4':
            editar_consulta()
        elif escolha == '5':
            print("\nSaindo...")
            break
        else:
            print("\nOpção inválida, tente novamente.")

# Carregar consultas ao iniciar o programa
consultas = carregar_consultas()

# Executar o menu
exibir_menu()