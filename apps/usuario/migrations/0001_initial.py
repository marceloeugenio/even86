# Generated by Django 3.2.5 on 2022-04-25 04:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(db_column='username', default='', max_length=30, verbose_name='Nome Usuário')),
                ('nome', models.CharField(blank=True, db_column='nome', default='', max_length=150, null=True, verbose_name='Nome Completo')),
                ('email', models.EmailField(blank=True, db_column='email', default='', max_length=100, null=True, unique=True, verbose_name='Email')),
                ('qtd_acesso', models.IntegerField(blank=True, db_column='qtd_acesso', default=0, null=True, verbose_name='Qtd. Acesso')),
                ('is_admin', models.BooleanField(db_column='is_admin', default='False', verbose_name='Admin')),
                ('is_active', models.BooleanField(db_column='is_active', default='True', verbose_name='Disponível')),
                ('is_staff', models.BooleanField(db_column='is_staff', default='False', verbose_name='Staff')),
                ('is_superuser', models.BooleanField(db_column='is_superuser', default='False', verbose_name='Super Usuário')),
                ('date_joined', models.DateTimeField(auto_now_add=True, db_column='date_joined', max_length=250, null=True, verbose_name='Data/Hora Inclusão')),
                ('last_login', models.DateTimeField(auto_now=True, db_column='last_login', max_length=250, null=True, verbose_name='Data/Hora Login')),
                ('fk_usuario_alteracao', models.ForeignKey(blank=True, db_column='fk_usuario_alteracao', default='', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='usuario_rel_usuario_alteracao', to=settings.AUTH_USER_MODEL, verbose_name='Usuário Alteração')),
                ('fk_usuario_inclusao', models.ForeignKey(blank=True, db_column='fk_usuario_inclusao', default='', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='usuario_rel_usuario_inclusao', to=settings.AUTH_USER_MODEL, verbose_name='Usuário Inclusão')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'usuário',
                'verbose_name_plural': 'usuários',
                'db_table': 'usuario',
                'permissions': (('list_usuario', 'Listar Usuários'),),
            },
        ),
    ]
