from django.db import models
from django import forms

class Pessoas(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    pess_nome = models.TextField(default='', null=True, blank=True, db_column='pess_nome', verbose_name='Nome')
    pess_is_disponivel = models.BooleanField(default='True', db_column='pess_is_disponivel', verbose_name='Disponível')
    pess_datetime_inclusao = models.DateTimeField(max_length=250, null=True, blank=True, db_column='pess_datetime_inclusao',auto_now_add=True, verbose_name='Data/Hora Inclusão')
    pess_datetime_alteracao = models.DateTimeField(max_length=250, null=True, blank=True, db_column='pess_datetime_alteracao',auto_now=True, verbose_name='Data/Hora Alteração')
    pess_fk_usuario_inclusao = models.ForeignKey('usuario.Usuario', default='', related_name='pessoas_rel_usuario_inclusao', on_delete=models.DO_NOTHING, null=True, blank=True, db_column='pess_fk_usuario_inclusao', verbose_name='Usuário Inclusão')
    pess_fk_usuario_alteracao = models.ForeignKey('usuario.Usuario', default='', related_name='pessoas_rel_usuario_alteracao', on_delete=models.DO_NOTHING, null=True, blank=True, db_column='pess_fk_usuario_alteracao', verbose_name='Usuário Alteração')

    class Meta:
        db_table = 'pessoas'
        verbose_name = "pessoa"
        verbose_name_plural = 'pessoas'
        permissions = (
            ('list_pess', 'Listar Pessoas'),
        )

    def __str__(self):
        return self.pess_nome