import json

from perguntas import Pergunta

#Exercício em classe para facilitar a representação
class ExercicioTres():
    def __init__(self) -> None:
        #Construção das listas
        self.dias: list[int] = []
        self.valores: list[float] = []

        #Variáveis de resposta
        self.menor_valor: float
        self.maior_valor: float
        self.acima_media_mensal: int
        
        #Execução dos métodos
        self.carrega_dados()
        self.media_mensal = self.calcula_media_mensal()
        self.get_numeros_maiores_que_a_media()
        pass

    #Definindo representação do objeto
    def __repr__(self) -> str:
        questao = Pergunta().retorna_pergunta(3)
        string = ("-"*20)+"\n"
        string += questao+"\n\n"
        string += f"O MENOR valor de faturamento ocorrido em um dia do mês: {self.get_menor_valor()}\n"
        string += f"O MAIOR valor de faturamento ocorrido em um dia do mês: {self.get_maior_valor()}\n"
        string += f"Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.: {self.acima_media_mensal}"
        return string

    #Lendo o arquivo json
    def carrega_dados(self) -> None:
        with open("dados.json", "r", encoding="utf-8") as f:
            dados = json.load(f)
            for n in range(len(dados)):
                dia = dados[n]['dia']
                valor = dados[n]['valor']
                #Verificando se o valor é maior que 0
                if valor >= 0:
                    self.dias.append(dia)
                    self.valores.append(valor)
        return
    
    def calcula_media_mensal(self):
        total = 0
        tamanho_lista_valores = len(self.valores)
        for n in self.valores:
            total += n
        media = total/tamanho_lista_valores
        return media
    
    def get_numeros_maiores_que_a_media(self):
        acima_media_mensal = []
        for n in range(len(self.valores)):
            if self.valores[n] > self.media_mensal:
                par = {'dia':self.dias[n], 'valor':self.valores[n]}
                acima_media_mensal.append(par)
        self.acima_media_mensal = len(acima_media_mensal)

    def get_menor_valor(self):
        return min([i for i in self.valores if i != 0])

    def get_maior_valor(self):
        return max([i for i in self.valores if i != 0])

if __name__ == "__main__":
    print(ExercicioTres().get_maior_valor())