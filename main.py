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
            print()
            print("Batman: O Cavaleiro das Trevas (2008)")
            print("A Origem (2010)")
            print("Matrix (1999)")
            print("O Senhor dos Anéis: O Retorno do Rei (2003)")
            print("Gladiador (2000)")
            print("Duro de Matar (1988)")
            print("Mad Max: Estrada da Fúria (2015)")
            print("Os Vingadores (2012)")
            print("John Wick: De Volta ao Jogo (2014)")
            print("O Exterminador do Futuro 2: O Julgamento Final (1991)")
            print()
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
            pass
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
            # Lista de 10 filmes musicais
            musical_films = [
                "The Sound of Music",
                "Singin' in the Rain",
                "Grease",
                "West Side Story",
                "Chicago",
                "La La Land",
                "Mamma Mia!",
                "Les Misérables",
                "The Rocky Horror Picture Show",
                "Hairspray"
            ]

            for film in musical_films:
                print(f"- {film}")
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
