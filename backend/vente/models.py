from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# customize my own usermanger
class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name, password, **extra_fields):
        """
        Creates and saves a User with the given email, registration and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        if not password:
            raise ValueError('Users password is required')

        user = self.model(
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, password=None):

        user = self.create_user(
            email,
            first_name,
            password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save()
        print(user.email)
        return user

# customize my own user
class Utilisateur(AbstractBaseUser, PermissionsMixin):


    class Meta:
        verbose_name = "User"
    email = models.EmailField("Email adress", max_length=200, unique=True)
    first_name = models.CharField(max_length=10, null=True)
    last_name = models.CharField(max_length=10, null=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name',]

    def __str__(self):
        return self.email



	

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
	image = models.ImageField(upload_to='image/fruit_pic/', default='default.jpeg', blank=True)

	user = models.ManyToManyField(Utilisateur)

	def __str__(self):
		return f'fruit-{self.name}'