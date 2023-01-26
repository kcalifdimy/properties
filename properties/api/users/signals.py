from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save

from rest_framework.authtoken.models import Token

from properties.api.users.models import Profile, User



#def Create_profile(sender, **kwargs):
 #   if kwargs['created']:
  #      user_profile = Profile.objects.create(user=kwargs['instance'])

#post_save.connect(Create_profile, sender=settings.AUTH_USER_MODEL)




