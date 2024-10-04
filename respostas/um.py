from perguntas import Pergunta

#Exercício em classe para facilitar a representação
class ExercicioUm():

    def __init__(self) -> None:
        #Passando os dados da questão como atributos da classe
        self.indice = 13
        self.soma = 0
        self.k = 0

        #Executando a soma da sequência até o índice
        self.soma_sequencia_ate_indice()
        pass

    #Definindo lógica de cálculo 
    def soma_sequencia_ate_indice(self) -> int:
        while self.k < self.indice:
            self.k += 1
            self.soma += self.k
        return self.soma
    
    #Definindo representação do objeto
    def __repr__(self) -> str:
        questao = Pergunta().retorna_pergunta(1)
        string = ("-"*20)+"\n"
        string += questao
        string += f"\n\nValor da variável SOMA: {self.soma}"
        return string


if __name__ == "__main__":
    #Exemplo de uso
    primeiro = ExercicioUm()
    ...