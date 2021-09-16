from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator

class UserManager(BaseUserManager):
    def create_user(self, email, phone_number,
                          username=None, password=None,
                          is_active=True, is_staff=False,
                          is_admin=False):
        user_obj = self.model(
            email = self.normalize_email(email),
            username=username,
            phone_number=phone_number
        )
        user_obj.set_password(password) # change user password
        user_obj.staff = True
        user_obj.admin = not is_staff
        user_obj.is_active = True
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, phone_number,
                                username=None, password=None):
        user = self.create_user(
                email,
                username=username,
                password=password,
                phone_number=phone_number,
                staff=True
        )
        return user

    def create_superuser(self, email, phone_number, username=None,
                                password=None):
        user = self.create_user(
                email,
                username=username,
                password=password,
                phone_number=phone_number,
                staff=True,
                admin=True
        )
        return user


class User(AbstractBaseUser):
    email       = models.EmailField(max_length=255, unique=True)
    username    = models.CharField(max_length=255, blank=True, null=True, unique=True)
    #address     = models.ForeignKey(Address, null=True, blank=True, on_delete=models.DO_NOTHING) 
    is_active   = models.BooleanField(default=True, blank=True) # can login 
    staff       = models.BooleanField(default=True, blank=True) # staff user non superuser
    admin       = models.BooleanField(default=False, blank=True) # superuser 
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+919876543210'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True) # validators should be a list
    created_timestamp = models.DateTimeField(auto_now=True)
    updated_timestamp = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = "username" #'username' #
    # USERNAME_FIELD and password are required by default
    REQUIRED_FIELDS = ["phone_number"] #['full_name'] #python manage.py createsuperuser

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_username(self):
        if self.username:
            return self.username
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        if self.is_admin:
            return False
        return self.staff

    @property
    def is_admin(self):
        return self.admin


    class Meta:
        db_table = "account_user"
    
    

