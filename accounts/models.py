from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _


class TaiKhoanManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError(_('Tên đăng nhập phải được cung cấp'))

        # Normalize username
        username = self.model.normalize_username(username)

        # Extract email from extra_fields, or use default if not provided
        email = extra_fields.pop('email', '')
        if email:
            email = self.normalize_email(email)

        # Create the user instance with email as a field, and other extra_fields
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('loai_tk', 'admin')

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser phải có is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser phải có is_superuser=True.'))

        return self.create_user(username, password, **extra_fields)


class TaiKhoan(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name=_('Tên đăng nhập'),
        error_messages={
            'unique': _("Tên đăng nhập đã tồn tại."),
        },
    )
    email = models.EmailField(
        verbose_name=_('Địa chỉ email'),
        max_length=255,
        unique=True,
        blank=True,
        null=True,
        error_messages={
            'unique': _("Email đã được sử dụng."),
        },
    )
    sdt = models.CharField(
        max_length=15,
        verbose_name=_('Số điện thoại'),
        blank=True,
        null=True,
    )
    dia_chi = models.TextField(
        verbose_name=_('Địa chỉ'),
        blank=True,
        null=True,
    )
    loai_tk = models.CharField(
        max_length=20,
        choices=[
            ('khach_hang', 'Khách hàng'),
            ('nhan_vien', 'Nhân viên'),
            ('admin', 'Quản lý'),
        ],
        default='khach_hang',
        verbose_name=_('Loại tài khoản'),
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name=_('Truy cập quản trị'),
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('Kích hoạt'),
    )

    objects = TaiKhoanManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('Tài khoản')
        verbose_name_plural = _('Tài khoản')

    def __str__(self):
        return self.username