import factory


class ParentCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'category.Category'

    title = factory.Faker('word')


class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('word')
    parent = factory.SubFactory(ParentCategoryFactory)

    class Meta:
        model = 'category.Category'


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'products.Product'

    title = factory.Faker('word')
    price = factory.Faker('pyfloat')
    category = factory.SubFactory(CategoryFactory)
