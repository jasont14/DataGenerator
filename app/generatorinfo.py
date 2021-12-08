from dataclasses import dataclass
from datetime import datetime

class GeneratorInfo:
    def __init__(self
                    ,order_date_order: datetime.date = datetime.now()
                    ,order_date_ship: datetime.date = datetime.now()
                    ,number_of_orders: int = 1000
                    ,number_of_customers: int = 10
                    ,product_list = []
                    ,tax_rate: float = 0.06
                ):
        self.order_date_order = order_date_order
        self.order_date_ship = order_date_ship
        self.number_of_orders = number_of_orders
        self.number_of_customers = number_of_customers
        self.product_list = product_list
        self.tax_rate = tax_rate
