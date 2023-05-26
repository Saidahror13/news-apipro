from django.core.management.base import BaseCommand
from faker import Faker
from factories import ParentCategoryFactory, CategoryFactory

faker = Faker()


class Command(BaseCommand):
    help = 'generate.Categories'

    def handle(self, *args, **options):
        ParentCategoryFactory.create_batch(size=10)
        CategoryFactory.create_batch(size=20)

        self.stdout.write(self.style.SUCCESS('Successfully generated (parent) categories'))
