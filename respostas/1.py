# 1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
# Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
# Imprimir(SOMA);
# Ao final do processamento, qual será o valor da variável SOMA?

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
        string = f"Valor da variável SOMA: {self.soma}"
        return string


if __name__ == "__main__":
    #Exemplo de uso
    primeiro = ExercicioUm()
    print(primeiro)
    ...