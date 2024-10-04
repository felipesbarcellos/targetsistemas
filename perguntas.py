import re
k = 0


class Pergunta():
    def __init__(self) -> None:
        self.n_questoes: list[int] = []
        self.questoes: list[str] = []
        self.abre_perguntas()
        pass


    def abre_perguntas(self):
        with open('perguntas.txt', encoding="utf-8") as p:
            n_questao: int = 0
            k=0
            lines: list[str] = p.readlines()
            for line in lines:
                line = line.replace("\n","")
                if f"{k+1})" in line:
                    k += 1
                    n_questao = k
                self.questoes.append(line)
                self.n_questoes.append(n_questao)

        ...

    def retorna_pergunta(self, n):
        pergunta = ""
        for index in zip(self.n_questoes, self.questoes):
            if index[0] == n:
                pergunta += index[1]
        return pergunta

if __name__ == "__main__":
    p = Pergunta()
    print(p.retorna_pergunta(2))