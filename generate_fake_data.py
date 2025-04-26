import random
from faker import Faker
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from yourapp.models import Product, Order  # Replace with your actual models

fake = Faker()

class Command(BaseCommand):
    help = "Generates fake users, products, and orders for testing."

    def add_arguments(self, parser):
        parser.add_argument('--users', type=int, default=10, help="Number of users to create")
        parser.add_argument('--products', type=int, default=20, help="Number of products to create")
        parser.add_argument('--orders', type=int, default=30, help="Number of orders to create")

    def handle(self, *args, **options):
        self.create_users(options['users'])
        self.create_products(options['products'])
        self.create_orders(options['orders'])

        self.stdout.write(self.style.SUCCESS("Fake data generation complete."))

    def create_users(self, count):
        User = get_user_model()
        self.stdout.write(self.style.NOTICE(f"Creating {count} users..."))
        for _ in range(count):
            User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password='password1234'
            )

    def create_products(self, count):
        self.stdout.write(self.style.NOTICE(f"Creating {count} products..."))
        for _ in range(count):
            Product.objects.create(
                name=fake.word().capitalize(),
                description=fake.text(max_nb_chars=200),
                price=random.uniform(10.0, 500.0),
                stock=random.randint(1, 100)
            )

    def create_orders(self, count):
        self.stdout.write(self.style.NOTICE(f"Creating {count} orders..."))
        User = get_user_model()
        users = list(User.objects.all())
        products = list(Product.objects.all())

        for _ in range(count):
            user = random.choice(users)
            product = random.choice(products)
            quantity = random.randint(1, 5)

            Order.objects.create(
                user=user,
                product=product,
                quantity=quantity,
                total_price=quantity * product.price
            )


#How to use it
# python manage.py generate_fake_data --users 50 --products 100 --orders 200
