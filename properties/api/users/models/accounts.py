import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from properties.api.users.managers import CustomUserManager


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    class Types(models.TextChoices):
        CLIENT = "CLIENT", "CLIENT"
        AGENT = "AGENT", "AGENT"
        REALTOR = "REALTOR", "REALTOR"
        LANDLORD = " LANDLORD", " LANDLORD"

    base_type = Types.CLIENT

    # What type of user are we?
    type = models.CharField(_("Type"), max_length=50, choices=Types.choices, default=base_type)

    # First Name and Last Name Do Not Cover Name Patterns
    # Around the Globe.
    username = None
    email = models.EmailField( unique=True)
    first_name = models.CharField(_("Last Name of User"), blank=True, max_length=255)
    last_name = models.CharField(_("First Name of User"), blank=True, max_length=255)
    #last_login = models.DateTimeField(_("last login"), blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    phone_number = models.CharField(null=True,max_length=214, blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

   

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.base_type
        return super().save(*args, **kwargs)


class ClientManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.CLIENT)


class AgentManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.AGENT)


class RealtorManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.REALTOR)


class LandlordManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.LANDLORD)



class Client(User):
    base_type = User.Types.CLIENT
    objects = ClientManager()

    class Meta:
        proxy = True


class Agent(User):
    base_type = User.Types.AGENT
    objects = AgentManager()

    class Meta:
        proxy = True

   
class Landlord(User):
    base_type = User.Types.LANDLORD
    objects = LandlordManager()

    class Meta:
        proxy = True

class Realtor(User):
    base_type = User.Types.REALTOR
    objects = RealtorManager()

    class Meta:
        proxy = True