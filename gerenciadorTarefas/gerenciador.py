from tarefa.tarefa import Tarefa

class Gerenciador():
    def __init__(self) -> None:
        self.lista = []

    def adicionar_tarefa(self, nome):
        tarefa = Tarefa(nome)
        self.lista.append(tarefa)
        print("Tarefa %s adicionada com sucesso!" % nome)

    def listar_tarefa(self):
        for index, tarefa in enumerate(self.lista):
            print(str(index + 1), tarefa.__str__())
        if (len(self.lista) == 0): 
            print("Lista vazia!!")

    def atualizar_tarefa(self, novoNome):
        enter = int(input("Entre com o número da tarefa..."))
        if (enter > 0):
            self.lista[enter-1].set_nome(novoNome)
        print("Tarefa %s atualizada com sucessor!" % novoNome)
        
    def completar_tarefa(self):
        enter = int(input("Entre com o número da tarefa..."))
        if (enter > 0):
            self.lista[enter-1].set_completa(True)
        print("Tarefa %s completada com sucessor!" % self.lista[enter-1].nome)
    
    def remover_completas(self):
        for tarefa in self.lista:
            if (tarefa.completa):
                self.lista.remove(tarefa)
        print("Tarefas completadas foram removidas!")

if __name__ == "__main__":
    grc = Gerenciador()
    while True:
        print("---------------------------")
        print("Menu de Gerencimanto de tarefas:")
        print("1 - adicionar")
        print("2 - listar")
        print("3 - atualizar")
        print("4 - completar")
        print("5 - remover completas")
        print("6 - sair")

        inp = input("Entre com o valor... ")

        if inp == "1":
            nova_tarefa = input("Entre com o nome da tarefa... ")
            grc.adicionar_tarefa(nova_tarefa)
        elif inp == "2":
            grc.listar_tarefa()
        elif inp == "3":
            novo_nome_tarefa = input("Entre com o novo nome da tarefa... ")
            grc.atualizar_tarefa(novo_nome_tarefa)
        elif inp == "4":
            grc.completar_tarefa()
        elif inp == "5":
            grc.remover_completas()
        elif inp == "6":
            break
        else:
            print("Valor inválido, tente outro")