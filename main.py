from dataclasses import dataclass
from faker import Faker
from faker.providers import DynamicProvider

from models.customer import Customer
from models.orderdetail import OrderDetail
from models.orderheader import OrderHeader
from models.product import Product
from app.generatorinfo import GeneratorInfo
from app.generator import Generator

import datetime
import itertools

def main(): 
    fake = Faker()
    gen = Generator(get_generator_info(),fake)
    gen.generate_customers()
    gen.generator_products()
    gen.generate_order_headers()
    gen.generate_order_details()

#ToDo: gen info could be set as config file ....refactor... 
#ToDo: product_list list of str.....move external to config or pass in as list... refactor
def get_generator_info() -> GeneratorInfo:
    gen_info = GeneratorInfo(
        order_date_order = datetime.date(2021,1,1)
        ,order_date_ship = datetime.date(2021,1,1)
        ,number_of_orders = 1000
        ,number_of_customers = 10
        ,product_list = ["Spoon", "Fork", "Knife", "Plate", "Bowl", "Spork", "Cup", "Glass", "Guzzler", "Straw"] # for use with Faker Provider
        ,tax_rate = 0.06    
    )

    return gen_info

if __name__ == "__main__":
    main()











