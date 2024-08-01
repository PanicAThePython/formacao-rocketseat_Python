from pydantic import BaseModel

class TarefaTest(BaseModel):
    nome: str
    completa: bool
 
data = [
    {
        "nome": "teste",
        "completa": False,
    },
]

t = TarefaTest(**data[0])
print(t)