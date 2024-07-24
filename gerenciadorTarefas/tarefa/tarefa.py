class Tarefa():
    def __init__(self, nome) -> None:
        self.nome = nome
        self.completa = False

    def get_nome(self):
        return self.nome
    
    def get_completa(self):
        return self.completa
    
    def set_completa(self, valor):
        self.completa = valor

    def set_nome(self, novoNome):
        self.nome = novoNome

    def __str__(self):
        if (self.completa):
            return "[X] - %s" % self.nome
        else:
            return "[ ] - %s" % self.nome