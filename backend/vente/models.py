from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Utilisateur(User):

	USERNAME_FIELD = "email"

	def __str__(self):
		return this.email

# creation du model fruit
class Fruit(models.Model):

	QUALITY = [
		('Frais', 'Frais'),
		('Humide', 'Humide'),
		('Sec', 'Sec')
	]

	name = models.CharField(max_length=50)
	price = models.IntegerField()
	quality = models.CharField(choices=QUALITY, max_length=20)

	user = models.ManyToManyField(User)
