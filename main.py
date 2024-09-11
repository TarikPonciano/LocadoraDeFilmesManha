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
            
            filmes_aventura = [
    "Indiana Jones e os Caçadores da Arca Perdida",
    "O Senhor dos Anéis: A Sociedade do Anel",
    "Jurassic Park",
    "Piratas do Caribe: A Maldição do Pérola Negra",
    "Harry Potter e a Pedra Filosofal",
    "A Jornada de Chihiro",
    "As Aventuras de Tintim",
    "O Hobbit: Uma Jornada Inesperada",
    "Star Wars: Episódio IV - Uma Nova Esperança",
    "Jumanji"
            ]

            contador = 1
            print("--- Filmes de Aventura ---\n")
            for filme in filmes_aventura:
                print(f"{contador}.",filme)
                contador += 1

        elif escolha == 3:
            print("A Grande Família (2006)")
            print("Os Caça-Fantasmas (1984)")
            print("Superbad - É Hoje (2007)")
            print("Se Beber, Não Case! (2009)")
            print("O Ânimos do Pai (2003)")
            print("O Ditador (2012)")
            print("As Branquelas (2004)")
            print("A Ressaca (2011)")
            print("O Virgem de 40 Anos (2005)")
            print("A Noite do Jogo (2018)")
            pass
        elif escolha == 4:
            pass
        elif escolha == 5:
            pass
        elif escolha == 6:
            print("O Senhor dos Anéis: A Sociedade do Anel (2001)")
            print("Harry Potter e a Pedra Filosofal (2001)")
            print("O Hobbit: Uma Jornada Inesperada (2012)")
            print("A Princesa Prometida (1987)")
            print("Pan's Labyrinth (2006)")
            print("As Crônicas de Nárnia: O Leão, a Feiticeira e o Guarda-Roupa (2005)")
            print("O Labirinto do Fauno (2006)")
            print("Star Wars: Episódio IV - Uma Nova Esperança (1977)")
            print("A História Sem Fim (1984)")
            print("Avatar (2009)")
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
            print(f'''01 > Seven: Os Sete Crimes Capitais (1995)
                  02 > Ilha do Medo (2010)
                  03 > Cisne Negro (2010)
                  04 > O Silêncio dos Inocentes (1991)
                  05 > A Origem (2010)
                  06 > O Sexto Sentido (1999)
                  07 > Garota Exemplar (2014)
                  08 > Corra! (2017)
                  09 > Oldboy (2003)
                  10 > Prisioners (2013)''')
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
