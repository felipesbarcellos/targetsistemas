from perguntas import Pergunta

#Exercício em classe para facilitar a representação
class ExercicioDois():
    def __init__(self, repeticoes: int = 2) -> None:
        self.repeticoes = repeticoes
        self.resultado = self.fibonacci(self.repeticoes)
        pass

    #Definindo função recursiva do fibonacci
    def fibonacci(self, n):
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
        else:
            sequencia = self.fibonacci(n - 1)
            prox_num = sequencia[-1] + sequencia[-2]
            sequencia.append(prox_num)
            return sequencia
        
    #Definindo representação do objeto
    def __repr__(self) -> str:
        questao = Pergunta().retorna_pergunta(2)
        string = ("-"*20)+"\n"
        string += questao
        string += f"\n\nA sequência fibonacci com {self.repeticoes} elementos é: {self.resultado}"
        return string
    
if __name__ == "__main__":
    print(ExercicioDois(7))