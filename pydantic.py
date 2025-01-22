from pydantic import BaseModel

from rich import traceback

traceback.install()

class Account(BaseModel):
    name: str
    balance: float

if __name__ == "__main__":
    acc = Account(name="John Doe", balance= 1000)
    print(acc.name)
    print(acc.balance)