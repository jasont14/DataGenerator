from dataclasses import dataclass
from faker import Faker
from faker.providers import DynamicProvider

from models.customer import Customer
from models.orderdetail import OrderDetail
from models.orderheader import OrderHeader
from models.product import Product
from app.generatorinfo import GeneratorInfo
from app.writetojson import WriteToJson

import datetime
import itertools
import json

class Generator:
    def __init__(self, gen_info: GeneratorInfo, fake: Faker):
        self.gen_info = gen_info
        self.fake = fake
        self.products = []

    def generate_customers(self):       

        product_provider = DynamicProvider(
            provider_name="product",
            elements=self.gen_info.product_list,
        )
        self.fake.add_provider(product_provider)

        #write out 10 customers
        customers = []
        customer_id_iter = itertools.count()
        for _ in range(self.gen_info.number_of_customers):
            customers.append( Customer(next(customer_id_iter)
                                    , self.fake.name()
                                    , self.fake.street_address()
                                    , self.fake.city()
                                    , self.fake.state_abbr()
                                    , self.fake.postcode()
                                    , self.fake.ssn()
                            ).__dict__                              #to dictionary to enable print to json
                    )        
        #print(json.dumps(customers))
        file_name = datetime.datetime.now().strftime("%Y-%m-%d") + 'customer.json'

        #write to file
        WriteToJson(file_name, customers)

    def generator_products(self):
        #write out products
        
        product_id_iter = itertools.count()
        for x in self.gen_info.product_list:
            self.products.append( Product (next(product_id_iter)
                                    ,x
                                    ,self.fake.pyfloat(2,2,True,1,20)                            
                                    ).__dict__
                            )

        #print(json.dumps(self.products)) # ToDo: need to move this out to external for query for large product sets.
        file_name = datetime.datetime.now().strftime("%Y-%m-%d") + 'products.json'

        WriteToJson(file_name, self.products)        

    def generate_order_headers(self):

        order_headers = []
        order_header_id_iter = itertools.count()

        for _ in range(self.gen_info.number_of_orders):
            order_headers.append ( OrderHeader ( next(order_header_id_iter)
                                    ,self.fake.random_int(min=0,max=self.gen_info.number_of_customers)
                                    ,self.fake.date_between(self.gen_info.order_date_order, datetime.datetime.now()).strftime("%Y-%m-%d")
                                    ,self.fake.date_between(self.gen_info.order_date_ship, datetime.datetime.now()).strftime("%Y-%m-%d")
                                    ).__dict__
            )

        #print(json.dumps(order_headers))
        file_name = datetime.datetime.now().strftime("%Y-%m-%d") + 'order_headers.json'

        WriteToJson(file_name,order_headers)  
  
    
    def get_order_details(self, order_header_id: int, order_detail_id: int) -> OrderDetail:

        od_id = order_detail_id
        od_header_id = order_header_id
        od_product_id = self.fake.random_int(min = 0, max=len(self.gen_info.product_list)-1)
        od_quantity =   self.fake.random_int(min=0, max = 5)
        od_price =      self.products[od_product_id].get("unit_price")
        od_tax = od_quantity * od_price * self.gen_info.tax_rate
        od_extended_price = od_quantity * od_price + od_tax

        return OrderDetail( od_id
                ,od_header_id
                ,od_product_id
                ,od_quantity
                ,od_price
                ,od_tax
                ,od_extended_price
         )

    def generate_order_details(self):
        
        order_details = []
        
        order_header_cnt = 0

        while order_header_cnt <= self.gen_info.number_of_orders:

            lines = self.fake.random_int(min=1,max=4)
            cntr = 1
            while cntr <= lines:  
                    
                order_details.append(self.get_order_details(order_header_cnt,cntr).__dict__)
                cntr = cntr + 1
            
            order_header_cnt = order_header_cnt + 1

        #print(json.dumps(order_details))
        file_name = datetime.datetime.now().strftime("%Y-%m-%d") + 'order_details.json'
        WriteToJson(file_name,order_details)
     
     