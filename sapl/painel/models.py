import reversion
from django.db import models
from django.utils.translation import ugettext_lazy as _
from sapl.utils import YES_NO_CHOICES


@reversion.register()
class Painel(models.Model):
    PAINEL_TYPES = (
        ('C', 'Completo'),
        ('P', 'Parlamentares'),
        ('V', 'Votação'),
        ('M', 'Mensagem'),
    )

    aberto = models.BooleanField(verbose_name=_('Abrir painel'), default=False)
    data_painel = models.DateField(verbose_name=_('Data painel'))
    mostrar = models.CharField(max_length=1,
                               choices=PAINEL_TYPES, default='C')

    def __str__(self):
        return str(self.aberto) + ":" + self.data_painel.strftime("%d/%m/%Y")


@reversion.register()
class Cronometro(models.Model):
    CRONOMETRO_TYPES = (
        ('A', _('Aparte')),
        ('D', _('Discurso')),
        ('O', _('Ordem do dia')),
        ('C', _('Considerações finais'))
    )

    CRONOMETRO_STATUS = (
        ('I', 'Start'),
        ('R', 'Reset'),
        ('S', 'Stop'),
        ('C', 'Increment'),
    )

    status = models.CharField(
        max_length=1,
        verbose_name=_('Status do cronômetro'),
        choices=CRONOMETRO_STATUS,
        default='S')
    duracao_cronometro = models.DurationField(
        verbose_name=_('Duração do cronômetro'))
    tipo = models.CharField(
        max_length=100, 
        verbose_name=_('Tipo Cronômetro'), 
        unique=True)
    ativo = models.BooleanField(
        default=False, 
        choices=YES_NO_CHOICES,
        verbose_name=_('Ativo?'))
    ordenacao = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name=_("Ordenação"))

    class Meta:
        verbose_name = _('Cronômetro')
        verbose_name_plural = _('Cronômetros')
        ordering = ['ordenacao']

    def __str__(self):
        return self.tipo


@reversion.register()
class PainelConfig(models.Model):

    cronometro_ordem = models.BooleanField(
        verbose_name=_('Cronômetro da Questão de Ordem deve travar os demais?'),
        choices=YES_NO_CHOICES, default=True)

    disparo_cronometro = models.BooleanField(
        verbose_name=_('Cronômetros devem disparar com antecedência?'),
        choices=YES_NO_CHOICES, default=True)

    tempo_disparo_antecedencia = models.DurationField(
        verbose_name=_('Cronômetros devem disparar com quanto tempo de antecedência?'),
        default="00:00:30",
        blank=True,
        null=True)

    class Meta:
        verbose_name = _('Configurações do Painel')
        verbose_name_plural = _('Configurações do Painel')
        ordering = ('-id',)

    @classmethod
    def attr(cls, attr):
        config = PainelConfig.objects.first()

        if not config:
            config = PainelConfig()
            config.save()

        return getattr(config, attr)

    def __str__(self):
        return 'Configurações do Painel'
