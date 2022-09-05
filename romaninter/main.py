class aplicacao():
    def __init__(self):
        self.numeral = input("Entrada: ")
    def verifica(self):
        self.fatiamento = []
        for x in range(0, len(self.numeral)):
            self.fatiamento.append(self.numeral[x])
    def romanint(self):
        for x in range(len(self.fatiamento), 0):
            self.fatiamento[x] 