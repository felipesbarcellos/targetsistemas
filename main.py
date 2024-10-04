import respostas.um
import respostas.dois
import respostas.tres
import respostas.quatro
import respostas.cinco

if __name__ == "__main__":
    while True:
        print("Selecione uma questão para visualizar:\n")
        print("1: Sequência numérica")
        print("2: Fibonacci")
        print("3: Análise Json")
        print("4: Percentual de representação")
        print("5: Inverter")
        print("\n9: Fechar")
        print("0: Todas\n")
        opt = input("Digite o número da opção desejada: ")
        try:
            match int(opt):
                case 0:
                    print(respostas.um.ExercicioUm())
                    print(respostas.dois.ExercicioDois())
                    print(respostas.tres.ExercicioTres())
                case 1:
                    print(respostas.um.ExercicioUm())
                case 2:
                    n_elementos = input("Quantos elementos você quer retornar no conjunto fibonacci: ")
                    print(respostas.dois.ExercicioDois(int(n_elementos)))
                case 3:
                    print(respostas.tres.ExercicioTres())
                case 4:
                    print(respostas.quatro.ExercicioQuatro())
                case 5:
                    palavra = input("Digite a palavra que você deseja inverter: ")
                    print(respostas.cinco.ExercicioCinco(palavra))
                case 9:
                    break
                case _:
                    print("Entrada inválida. Digite apenas um dos números disponíveis")

        except ValueError as e:
            print("Entrada inválida. Digite apenas o número...")
            
        input("-- Aperte ENTER para continuar --")