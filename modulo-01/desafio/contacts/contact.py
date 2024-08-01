from typing import Dict

class Contact():
    def __init__(self, name, phone, email, favorite = False) -> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.favorite = favorite

    def update_contact(self, data: Dict) -> None:
        try:
            self.name = data["name"]
            self.phone = data["phone"]
            self.email = data["email"]
            print("Contato atualizado com sucesso!")
        except Exception:
            print("Houve um problema ao atualizar o contato, tente de novo mais tarde...")

    def turn_in_turn_off_favorite(self) -> None:
        try: self.favorite = not self.favorite
        except Exception:
            print("Houve um problema ao favoritar o contato, tente de novo mais tarde...")

    def __str__(self) -> str:
        if (self.favorite): return self.name + ": " + self.email + " | " + self.phone + " ★"
        return self.name + ": " + self.email + " | " + self.phone