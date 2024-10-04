from perguntas import Pergunta

#Exercício em classe para facilitar a representação
class ExercicioCinco():
    def __init__(self, string) -> None:
        self.string: str = string
        self.string_invertida: str
        pass

    #Carregando os dados que serão consumidos
    def inverte_string(self):
        ...
        
    #Definindo representação do objeto
    def __repr__(self) -> str:
        questao = Pergunta().retorna_pergunta(4)
        string = ("-"*20)+"\n"
        string += questao+"\n"
        string += f"\String: {self.string}:\n"
        string += f"\String Invertida: {self.string_invertida}:\n"
        return string
    
if __name__ == "__main__":
    print(ExercicioCinco())