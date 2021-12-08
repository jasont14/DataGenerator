from dataclasses import dataclass

@dataclass
class Product:
    id:int
    name:str
    unit_price: float = 0.0