import random
import string
import ANSI as A
from armazenar import salvar_senha, excluir_senha_id  

def gerar_senha(tamanho, incluir_maiusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_especiais=True):
    caracteres = ""
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_especiais:
        caracteres += string.punctuation
    
    if not caracteres:
        print('É necessário selecionar pelo menos um tipo de caracter!')
        return None
    
    senha = "".join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    print(f"""
          {A.SUBLINHADO}{A.NEGRITO}GERENCIADOR DE SENHAS ALEATÓRIAS{A.RESET}
            """)
    
    while True:
        print("\n1. Gerar nova senha")
        print("2. Excluir senha")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            try:
                tamanho = int(input("Digite o tamanho da senha: "))
            except ValueError:
                print("Entrada Inválida. Insira o tamanho em números!")
                continue

            incluir_maiusculas = input("Inserir letras maiúsculas? (s/n): ").strip().lower() == 's'
            incluir_minusculas = input("Inserir letras minúsculas? (s/n): ").strip().lower() == 's'
            incluir_numeros = input("Inserir números? (s/n): ").strip().lower() == 's'
            incluir_especiais = input("Inserir caracteres especiais? (s/n): ").strip().lower() == 's'
            
            senha = gerar_senha(tamanho, incluir_maiusculas, incluir_minusculas, incluir_numeros, incluir_especiais)
            
            if senha:
                print("\nSenha gerada: ", senha)
                salvar_senha(senha)
        
        elif opcao == '2':
            try:
                id_senha = int(input("Digite o ID da senha a ser excluída: "))
                excluir_senha_id(id_senha)
            except ValueError:
                print("Entrada inválida. Insira o ID como um número.")
        
        elif opcao == '3':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()
