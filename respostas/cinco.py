from perguntas import Pergunta

#Exercício em classe para facilitar a representação
class ExercicioCinco():
    def __init__(self, string = "Teste Maluco") -> None:
        self.string: str = string
        self.string_invertida = self.inverte_string(self.string)
        pass

    #Carregando os dados que serão consumidos
    def inverte_string(self, string):
        invertida = ""
        for i in range(len(string) -1, -1, -1):
            invertida += string[i]
        return invertida
        
    #Definindo representação do objeto
    def __repr__(self) -> str:
        questao = Pergunta().retorna_pergunta(5)
        string = ("-"*20)+"\n"
        string += questao+"\n"
        string += f"String: {self.string}:\n"
        string += f"String Invertida: {self.string_invertida}\n"
        return string
    
if __name__ == "__main__":
    print(ExercicioCinco())