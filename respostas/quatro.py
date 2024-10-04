from perguntas import Pergunta

#Exercício em classe para facilitar a representação
class ExercicioQuatro():
    def __init__(self) -> None:
        self.dados_brutos: list[dict] = []
        self.dados_tratados: list[dict] = []
        self.consome_dados()
        self.soma_estados = self.get_soma_estados()
        self.representacao_estados()
        pass

    #Carregando os dados que serão consumidos
    def consome_dados(self):
        sp = {'estado':'SP', 'valor':67836.43}
        rj = {'estado':'RJ', 'valor':36678.66}
        mg = {'estado':'MG', 'valor':29229.88}
        es = {'estado':'ES', 'valor':27265.48}
        outros = {'estado':'Outros', 'valor':19849.53}

        self.dados_brutos.append(sp)
        self.dados_brutos.append(rj)
        self.dados_brutos.append(mg)
        self.dados_brutos.append(es)
        self.dados_brutos.append(outros)

    #Retornando a soma de todos os valores
    def get_soma_estados(self) -> float:
        total = 0
        for i in self.dados_brutos:
            total += i['valor']
        return total
    
    #Criando vetor com estado e porcentagem
    def representacao_estados(self):
        for estado in self.dados_brutos:
            porcentagem = estado['valor']/self.soma_estados*100
            nome_estado = estado['estado']
            output = {'estado':nome_estado, 'porcentagem':porcentagem}
            self.dados_tratados.append(output)
        
    #Definindo representação do objeto
    def __repr__(self) -> str:
        questao = Pergunta().retorna_pergunta(4)
        string = ("-"*20)+"\n"
        string += questao+"\n"
        string += f"\nPercentual de representação de cada estado:\n"
        for n in range(len(self.dados_tratados)):
            string += f"Estado: {self.dados_tratados[n]['estado']}" + " | Porcentagem: {:.2f}%\n".format(self.dados_tratados[n]['porcentagem'])
        return string
    
if __name__ == "__main__":
    print(ExercicioQuatro())