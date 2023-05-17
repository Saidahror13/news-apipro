from django.core.management.base import BaseCommand, CommandError
from news_category import models as category_models


class Command(BaseCommand):
    help = 'Migrate categories from products app to category apps'

    def handle(self, *args, **options):
        old_cats = category_models.Category.objects.all()
        for cat in old_cats:
            category_models.Category.objects.create(title=cat.title)
        self.stdout.write(self.style.SUCCESS('Successfully migrated %s categories.' % old_cats.count())


