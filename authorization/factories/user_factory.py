import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "authorization.User"
        django_get_or_create = ("username",)

    username = factory.Faker("username")
    email = factory.Faker("email")
    password = factory.PostGenerationMethodCall("set_password", "password")

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    is_active = True
    is_superuser = False
    is_staff = False
