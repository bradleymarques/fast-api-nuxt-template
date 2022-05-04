import factory
from authorization.factories import UserFactory


class AdminFactory(UserFactory):
    is_superuser = True
    is_staff = True
