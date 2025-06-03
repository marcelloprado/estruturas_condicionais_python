from verificar_idade import verificar_idade
from calcular_peso import calcular_imc
from verificar_estacao import verificar_estacao

def exibir_menu():
    print("\n=== Menu Principal ===")
    print("1. Verificar idade")
    print("2. Calcular Peso")
    print("3. Verificar estação do ano")
    print("4. Sair")
    return input("\n Escolha uma opção (1-4): ")

def main():
    while True:
        opcao = exibir_menu()
        
        match opcao:
            case '1':
                print("\n=== Verificar Idade ===")
                resultado = verificar_idade()
                print(f"\n Resultado: {resultado}")
            case '2':
                print("\n=== Calcular IMC ===")
                resultado = calcular_imc()
                print(f"\n Resultado: {resultado}")
                
            case '3':
                print("\n=== Verificar Estação do Ano ===")
                resultado = verificar_estacao()
                print(f"\n Resultado: {resultado}")
                
            case '4':
                print("\n=== Programa Finalizado! ===")
                break
            case _:
                print("\n Opção inválida! Tente novamente.")
                
        input("\n Pressione Enter para continuar...")
        
if __name__ == "__main__":
    main() 