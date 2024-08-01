from contacts.contact import Contact
from typing import List, Dict

class ContactBook():
    def __init__(self) -> None:
        self.contacts: List[Contact] = []

    def add_contact_to_contact_book(self, contact: Contact) -> None:
        try:
            self.contacts.append(contact)
            print("Contato adicionado com sucesso!!")
        except Exception:
            print("Houve um problema ao adicionar o contato da agenda, tente de novo mais tarde...")

    def get_all_contacts(self) -> List[Contact]:
        try:
            cont = 1
            for contact in self.contacts:
                print(cont, ".", contact.__str__())
                cont+=1
            if (self.contacts.__len__() == 0): print("A Agenda está vazia!")
        except Exception:
            print("Houve um problema ao listar os contatos da agenda, tente de novo mais tarde...")

    def update_contact(self, index: int, data: Dict) -> None:
        self.contacts[index].update_contact(data)

    def make_favorite_or_not(self, index: int) -> None:
        self.contacts[index].turn_in_turn_off_favorite()

    def get_all_favorite_contacts(self) -> List[Contact]:
        try:
            count_favs = 0
            for contact in self.contacts:
                if (contact.favorite): 
                    print(contact.__str__())
                    count_favs+=1
            if (count_favs == 0): print("Você ainda não favoritou ninguém...")
        except Exception:
            print("Houve um problema ao listar os contatos favoritos da agenda, tente de novo mais tarde...")

    def delete_contact_from_contact_book(self, index: int) -> None:
        try:
            for i in range(len(self.contacts)):
                if i == index:
                    contact = self.contacts[i]
                    self.contacts.remove(contact)
        except Exception:
            print("Houve um problema ao deletar o contato da agenda, tente de novo mais tarde...")