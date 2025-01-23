from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.hashers import make_password

class CustomUserManager(BaseUserManager):
    def create_user(self, email, x_handle, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        if not x_handle:
            raise ValueError("The X account handle must be set")
        
        email = self.normalize_email(email)
        user = self.model(email=email, x_handle=x_handle, **extra_fields)

        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user
   
    def create_superuser(self, email, x_handle, password=None, **extra_fields):
        user = self.create_user(
            email=email,
            x_handle=x_handle,
            password=password,
            is_staff=True,
            **extra_fields
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    x_handle = models.CharField(max_length=50, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['x_handle']

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Add this line

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    # python manage.py migrate --run-syncdb