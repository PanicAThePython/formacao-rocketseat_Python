from contactBook.contactBook import ContactBook
from contacts.contact import Contact

if __name__=="__main__":
    my_contact_book = ContactBook()
    while True:
        print("---------------------------")
        print("Menu de Gerencimanto da agenda:")
        print("1 - adicionar novo contato")
        print("2 - listar contatos da agenda")
        print("3 - atualizar contato")
        print("4 - des/favoritar contato")
        print("5 - remover contato da agenda")
        print("6 - listar todos os contatos favoritos")
        print("7 - sair")

        user_action = input("Entre com o número da ação que deseja... ")

        if (user_action == "1"):
            contact_name = input("Ensira o nome do contato: ")
            contact_phone = input("Ensira o telefone do contato: ")
            contact_email = input("Ensira o email do contato: ")

            new_contact = Contact(contact_name, contact_phone, contact_email)
            my_contact_book.add_contact_to_contact_book(new_contact)

        elif (user_action == "2"):
            my_contact_book.get_all_contacts()

        elif (user_action == "3"):
            contact_index = int(input("Ensira o número do contato... "))
            contact_name = input("Ensira o novo nome do contato: ")
            contact_phone = input("Ensira o novo telefone do contato: ")
            contact_email = input("Ensira o novo email do contato: ")

            contact_data = {
                "name": contact_name,
                "phone": contact_phone,
                "email": contact_email
            }

            my_contact_book.update_contact(contact_index - 1, contact_data)

        elif (user_action == "4"):
            contact_index = int(input("Ensira o número do contato... "))
            my_contact_book.make_favorite_or_not(contact_index - 1)

        elif (user_action == "5"):
            contact_index = int(input("Ensira o número do contato... "))
            my_contact_book.delete_contact_from_contact_book(contact_index - 1)

        elif (user_action == "6"):
            my_contact_book.get_all_favorite_contacts()

        elif (user_action == "7"): break

        else:
            print("Valor de entrada inválido...")

