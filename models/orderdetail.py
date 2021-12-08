from dataclasses import dataclass

@dataclass
class OrderDetail:
    id:int
    header_id:int
    product_id:int
    quantity:int = 0
    price:float = 0.0
    tax:float = 0.0
    extended_price:float = 0.0