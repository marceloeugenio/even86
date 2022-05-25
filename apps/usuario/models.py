from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UsuarioManager(BaseUserManager):
    def create_user(self, username, nome, email, fk_usuario_inclusao, password=None):
        if not email:
            raise ValueError("Email obrigatório")
        if not username:
            raise ValueError("Nome de Usuário obrigatório")

        user = self.model(
            username=username,
            nome=nome,
            fk_usuario_inclusao=fk_usuario_inclusao,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, nome=None, fk_usuario_inclusao=None):
        user = self.create_user(
            password=password,
            username=username,
            nome=nome,
            fk_usuario_inclusao=fk_usuario_inclusao,
            email=self.normalize_email(email),
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Usuario(PermissionsMixin, AbstractBaseUser):
    username = models.CharField(default='', max_length=30, null=False, blank=False, db_column='username', verbose_name='Nome Usuário')
    nome = models.CharField(default='', max_length=150, null=True, blank=True,db_column='nome', verbose_name='Nome Completo')
    email = models.EmailField(default='', max_length=100, null=True, blank=True, db_column='email', unique=True, verbose_name='Email')
    qtd_acesso = models.IntegerField(default=0,null=True, blank=True, db_column='qtd_acesso', verbose_name='Qtd. Acesso')
    is_admin = models.BooleanField(default='False', db_column='is_admin', verbose_name='Admin')
    is_active = models.BooleanField(default='True', db_column='is_active', verbose_name='Disponível')
    is_staff = models.BooleanField(default='False', db_column='is_staff', verbose_name='Staff')
    is_superuser = models.BooleanField(default='False', db_column='is_superuser', verbose_name='Super Usuário')
    date_joined = models.DateTimeField(max_length=250, null=True, blank=True, db_column='date_joined', auto_now_add=True, verbose_name='Data/Hora Inclusão')
    last_login = models.DateTimeField(max_length=250, null=True, blank=True, db_column='last_login', auto_now=True, verbose_name='Data/Hora Login')

    fk_usuario_inclusao = models.ForeignKey('usuario.Usuario', default='', related_name='usuario_rel_usuario_inclusao', on_delete=models.DO_NOTHING, null=True, blank=True, db_column='fk_usuario_inclusao', verbose_name='Usuário Inclusão')
    fk_usuario_alteracao = models.ForeignKey('usuario.Usuario', default='', related_name='usuario_rel_usuario_alteracao', on_delete=models.DO_NOTHING, null=True, blank=True, db_column='fk_usuario_alteracao', verbose_name='Usuário Alteração')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UsuarioManager()

    # class Meta(AbstractBaseUser.Meta):
    class Meta:
        db_table = 'usuario'
        verbose_name = "usuário"
        verbose_name_plural = 'usuários'
        permissions = (
            ('list_usuario', 'Listar Usuários'),
        )

    def __str__(self):
        return self.email+' - '+self.nome

    def get_nome(self):
        return self.nome

    # def has_perm(self, perm, obj=None):
    #     return True
    
    # def has_module_perms(self, app_label):
    #     return True

    # @property
    # def is_staff(self):
    #     return self.is_admin

    # @property
    # def is_admin(self):
    #     "Is the user a admin member?"
    #     return self.admin

    # @property
    # def is_active(self):
    #     "Is the user active?"
    #     return self.active

    # def get_full_name(self):
    #     # The user is identified by their email address
    #     return self.email

    # def get_short_name(self):
    #     # The user is identified by their email address
    #     return self.email

