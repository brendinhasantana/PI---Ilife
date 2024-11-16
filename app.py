import os
import datetime

# exibir o menu
def exibir_menu():
    print("\n---- Menu de Cadastro de Consultas ----")
    print("1. Cadastrar nova consulta")
    print("2. Mostrar todas as consultas cadastradas")
    print("3. Sair")

# cadastrar uma nova consulta
def cadastrar_consulta():
    print("\nDigite os dados da nova consulta:")

    # dados do paciente
    nome_paciente = input("Nome do paciente: ")
    data_consulta = input("Data da consulta (dd/mm/aaaa): ")
    horario_consulta = input("Horário da consulta (hh:mm): ")
    observacoes = input("Observações (opcional): ")

    try:
        data_consulta_formatada = datetime.datetime.strptime(data_consulta, "%d/%m/%Y")
    except ValueError:
        print("Erro: Data inválida! Use o formato dd/mm/aaaa.")
        return

    try:
        horario_consulta_formatado = datetime.datetime.strptime(horario_consulta, "%H:%M")
    except ValueError:
        print("Erro: Horário inválido! Use o formato hh:mm.")
        return

    # Salva os dados em um arquivo de texto
    consulta = {
        'nome': nome_paciente,
        'data': data_consulta_formatada.strftime("%d/%m/%Y"),
        'horario': horario_consulta_formatado.strftime("%H:%M"),
        'observacoes': observacoes if observacoes else "Nenhuma observação."
    }

    salvar_consulta(consulta)

    print(f"\nConsulta cadastrada com sucesso para {nome_paciente}!")

# salvar a consulta no arquivo
def salvar_consulta(consulta):
    arquivo = "consultas.txt"

    with open(arquivo, "a") as f:
        f.write(f"Paciente: {consulta['nome']}\n")
        f.write(f"Data: {consulta['data']}\n")
        f.write(f"Horário: {consulta['horario']}\n")
        f.write(f"Observações: {consulta['observacoes']}\n")
        f.write("-" * 40 + "\n")

# exibir todas as consultas cadastradas
def exibir_consultas():
    arquivo = "consultas.txt"

    if not os.path.exists(arquivo):
        print("\nAinda não há consultas cadastradas.")
        return
    
    with open(arquivo, "r") as f:
        consultas = f.read()

    if consultas:
        print("\n---- Consultas Cadastradas ----")
        print(consultas)
    else:
        print("\nNão há consultas registradas.")

# Função principal
def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_consulta()
        elif opcao == "2":
            exibir_consultas()
        elif opcao == "3":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
