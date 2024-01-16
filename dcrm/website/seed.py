from. models import*
from faker import Faker
fake=Faker()


def seed_db(n):
    for i in range(0, n):
        Sale.objects.create(
            sale_product=fake.product(),
            sale_qty=fake.quantity(),
            subtotal=fake.sub_total(),
            date=fake.created_at(),
            price=fake.product.price(),

            
        )