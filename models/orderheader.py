from dataclasses import dataclass

@dataclass
class OrderHeader:
    id:int
    customer_id:int
    order_date:str = "2000,1,1"
    ship_date:str = "2000,1,1"