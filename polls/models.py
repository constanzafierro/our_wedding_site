from django.db import models
from django.conf import settings


class Comment(models.Model):
    name = models.CharField(max_length=200)
    text = models.CharField(max_length=500)


class PlusOneGuest(models.Model):
    name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    drink_check = models.BooleanField(default=True)
    is_veggie = models.BooleanField(default=False)


class Guest(models.Model):
    guest_user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                      on_delete=models.CASCADE,
                                      primary_key=True)
    confirmation_status = models.BooleanField(default=False)
    drink_check = models.BooleanField(default=True)
    just_party = models.BooleanField(default=False)
    is_veggie = models.BooleanField(default=False)
    has_plus_one = models.BooleanField(default=False)
    plus_one = models.ForeignKey(PlusOneGuest, null=True, blank=True,
                                 on_delete=models.CASCADE)

    def __str__(self):
        return "{}, confirmed:{}".format(self.guest_user, self.confirmation_status)

