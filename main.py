def exibir_menu():
    print("Escolha um gênero de filme:")
    print("1. Ação")
    print("2. Aventura")
    print("3. Comédia")
    print("4. Drama")
    print("5. Ficção Científica")
    print("6. Fantasia")
    print("7. Romance")
    print("8. Terror")
    print("9. Suspense")
    print("10. Mistério")
    print("11. Documentário")
    print("12. Animação")
    print("13. Musical")
    print("14. Policial")
    print("15. Guerra")
    print("16. Histórico")

def main():
    exibir_menu()
    
    try:
        escolha = int(input("Digite o número do gênero escolhido: "))
        
        #Faça modificações apenas na seção do seu número
        #Faça o print de 10 filmes do gênero selecionado
        if escolha == 1:
            pass
        elif escolha == 2:
            pass
        elif escolha == 3:
            pass
        elif escolha == 4:
            pass
        elif escolha == 5:
            pass
        elif escolha == 6:
            pass
        elif escolha == 7:
            # Lista de filmes de romance
            filmes_de_romance = [
                "A Culpa é das Estrelas",
                "P.S. Eu Te Amo",
                "Como Eu Era Antes de Você",
                "Diário de uma Paixão",
                "A Bella e a Fera",
                "O Lado Bom da Vida",
                "La La Land",
                "Orgulho e Preconceito",
                "500 Dias com Ela",
                "Amor e Outras Drogas"
            ]

            # Imprimir os filmes de romance
            for filme in filmes_de_romance:
                print(f"- {filme}")
        elif escolha == 8:
            pass
        elif escolha == 9:
            pass
        elif escolha == 10:
            pass
        elif escolha == 11:
            pass
        elif escolha == 12:
            pass
        elif escolha == 13:
            pass
        elif escolha == 14:
            pass
        elif escolha == 15:
            pass
        elif escolha == 16:
            pass
        else:
            print("Gênero inválido!")
        
        
    
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

if __name__ == "__main__":
    main()
