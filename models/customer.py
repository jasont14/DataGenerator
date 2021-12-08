from dataclasses import dataclass

@dataclass
class Customer:
    id:int
    name:str
    address:str
    city:str
    state:str
    zip:str
    tax_id: str
