# fake sellers, orders, customers, and product data that are linked to each other ( with relation )

from faker import Faker
import random
import pandas as pd

# create fake data using Faker library
fake = Faker()

# generate 100 fake sellers
sellers = []
for i in range(100):
    seller = {
        'id': i+1,
        'name': fake.company(),
        'address': fake.address()
    }
    sellers.append(seller)

# generate 1000 fake products
products = []
for i in range(1000):
    product = {
        'id': i+1,
        'name': fake.word(),
        'description': fake.sentence(),
        'price': random.randint(10, 100),
        'seller_id': random.randint(1, 100)
    }
    products.append(product)

# generate 10000 fake customers
customers = []
for i in range(10000):
    customer = {
        'id': i+1,
        'name': fake.name(),
        'address': fake.address(),
        'email': fake.email()
    }
    customers.append(customer)

# generate 100000 fake orders
orders = []
for i in range(100000):
    order = {
        'id': i+1,
        'product_id': random.randint(1, 1000),
        'customer_id': random.randint(1, 10000),
        'quantity': random.randint(1, 10),
        'order_date': fake.date_this_century()
    }
    orders.append(order)

# convert the data to pandas dataframes
sellers_df = pd.DataFrame(sellers)
products_df = pd.DataFrame(products)
customers_df = pd.DataFrame(customers)
orders_df = pd.DataFrame(orders)

# merge the dataframes together based on the relationships between the data
result = pd.merge(orders_df, products_df, on='product_id', how='left')
result = pd.merge(result, sellers_df, left_on='seller_id', right_on='id', how='left')
result = pd.merge(result, customers_df, on='customer_id', how='left')

# save the data to a CSV file
result.to_csv('fake_data.csv', index=False)
