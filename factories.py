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
        model = 'news_product.Product'

    title = factory.Faker('word')
    price = factory.Faker('pyfloat')
    category = factory.SubFactory(CategoryFactory)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "users.User"

    first_name = factory.Faker("word")
    email = factory.Faker("word")
    age = factory.Faker("pyint")
    password = f"{factory.Faker('pyint')}{factory.Faker('word')}"


class BlogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'comments.Blog'

    title = factory.Faker("word")
    author = factory.SubFactory(CategoryFactory)
    body = factory.Faker('first_name')


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'comments.Comments'

    blog = factory.SubFactory(BlogFactory)
    user = factory.SubFactory(UserFactory)
    body = factory.Faker("word")
