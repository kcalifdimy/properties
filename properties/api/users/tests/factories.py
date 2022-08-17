from django.db.models.signals import post_save
import typing 
#import Any, Sequence

from django.contrib.auth import get_user_model
from factory import Faker, post_generation, Sequence, RelatedFactory, django, SubFactory
from factory.django import DjangoModelFactory



@django.mute_signals(post_save)
class ProfileFactory(django.DjangoModelFactory):
    class Meta:
        model = 'users.Profile'

    bio = Faker('sentence')
    address = Faker('address')
    user = SubFactory('users.test.factories.UserFactory')



@django.mute_signals(post_save)
class UserFactory(DjangoModelFactory):

    #username = Faker("user_name")
    id = Faker('uuid4')
    #email = Faker("email")
    email = Sequence(lambda n: 'person{}@example.com'.format(n))
    first_name = Faker("first_name")
    last_name = Faker("last_name")
    profile = RelatedFactory(ProfileFactory, 'user')

    @post_generation
    def password(self, create: bool, extracted: typing.Sequence[typing.Any], **kwargs):
        password = (
            extracted
            if extracted
            else Faker(
                "password",
                length=42,
                special_chars=True,
                digits=True,
                upper_case=True,
                lower_case=True,
            ).evaluate(None, None, extra={"locale": None})
        )
        self.set_password(password)

    class Meta:
        model = get_user_model()
        django_get_or_create = ["email"]





