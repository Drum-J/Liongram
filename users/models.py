from pickletools import read_uint1
from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager as DjangoUserManager

class UserManager(DjangoUserManager):
    # 함수명 앞에 _가 붙은 이유는 외부에 유출하지 않고 숨기기위해, 내부에서만 쓰기 위해서.
    def _create_user(self, username, email, password, **extra_fields):
        if not email :
            raise ValueError('이메일은 필수 값입니다.')

        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password) #암호를 해싱처리 해준다. 암호화.
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(username, email, password, **extra_fields)



class User(AbstractUser):
    phone = models.CharField(verbose_name='전화번호',max_length=11)

    object = UserManager() #유저와 유저매니저를 연결시켜준다, 클래스만 만들어놓으면 전혀 다른애가 되기 때문이다.




# # 확장모델, 부가적인 내용을 넣고싶을때
# class UserInfo(models.Model):
#     phone_sub = models.CharField(verbose_name='보조 전화번호',max_length=11)
#     user = models.ForeignKey(to='User',on_delete=models.CASCADE)