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
            print("ficçao cientifica")
            filmes = ["O Homem do Futuro (2011) - Dirigido por Cláudio Torres",
                "A Máquina (2012) - Dirigido por João Falcão",
                "Os Trapalhões na Guerra dos Planetas (1978) - Dirigido por Alberto Renato e J.B. Tanko",
                "O Candidato (2019) - Dirigido por Zé Pedro Goulart",
                "O Contador de Histórias (2009) - Dirigido por Luiz Villaça",
                "A Morte Negra (2022) - Dirigido por Otávio Juliano",
                "A Lenda do Caboclo (2014) - Dirigido por Roberta Marques",
                "A Terra de Ninguém (2009) - Dirigido por Fernando Coimbra",
                "São Jorge (2016) - Dirigido por Marco Dutra",
                "O Invasor (2001) - Dirigido por Beto Brant e Renato Ciasca"]
            
            for filme in filmes:
                print(filme)
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
