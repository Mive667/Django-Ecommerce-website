from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None):
        if not email:
            raise ValueError('User must have an email address')
        if not username:
            raise ValueError('User must have a username')
        # if not first_name:
        #     raise ValueError('User must have a first name')
        # if not last_name:
        #     raise ValueError('User must have a last name')

        user = self.model(
            # Uppercase -> Lowercase
            email = self.normalize_email(email), 
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self, email, username, first_name, last_name, password):
        user = self.create_user(
            email = email, 
            password = password,
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)


# Create your models here.
class Account(AbstractBaseUser):
    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    # address_line_1 = models.CharField(max_length=150)
    # address_line_2 = models.CharField(max_length=150)
    # profile_picture = models.ImageField(upload_to='media/profile_pictures', blank=True)
    # city = models.CharField(max_length=50)
    # state = models.CharField(max_length=50)
    # country = models.CharField(max_length=50)
    # zip_code = models.CharField(max_length=10)
    # date_joined = models.DateTimeField(auto_now_add=True)
    # last_login = models.DateTimeField(auto_now=True)
    # is_admin = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=True)
    # is_staff = models.BooleanField(default=False)
    # is_superuser = models.BooleanField(default=False)
    # is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
