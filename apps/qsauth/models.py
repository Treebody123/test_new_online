from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def _create_user(self,username,password,**kwargs):
        user = self.model(username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self,telephone,username,password,**kwargs):
        kwargs['is_superuser'] = False
        return self._create_user(username,password,**kwargs)

    def create_superuser(self,username,password,**kwargs):
        kwargs['is_superuser'] = True
        return self._create_user(username,password,**kwargs)

class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=12,unique=True)
    email = models.EmailField(unique=True,null=True)
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=12)
    is_active = models.BooleanField(default=True)
    gender = models.IntegerField(default=0) # 0:代表未知，1：男，2：女
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)

    # USERNAME_FIELD：这个属性是以后在使用authenticate
    # 进行验证的时候的字段
    USERNAME_FIELD = 'username'
    # 这个属性是用来，以后在命令行中使用createsuperuser命令
    # 的时候，会让你输入的字段，那么这里我们只要写一个username
    # 以后在创建超级管理员的时候，就会让你输入USERNAME_FIELD指定的字段
    # 现在USERNAME_FIELD指定的字段是telephone，以及password（这个字段你不写也会让你输入）
    REQUIRED_FIELDS = ['password']
    # 以后给某个用户发送邮箱的时候，就会使用这个属性指定的字段的值来发送
    EMAIL_FIELD = 'email'

    objects = UserManager()

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.username