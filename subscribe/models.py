# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime


class TransactionBase(models.Model):
    STATUS_CHOICES = (
        (0, u'en cours'),
        (1, u'confirmé')
    )

    COUNTRY_CHOICES = (
        ('BE', u'Belgique'),
        ('FR', u'France'),
        ('LU', u'Luxembourg')
    )

    TITLE_CHOICES = (
        (False, u'Madame'),
        (True, u'Monsieur')
    )

    title = models.BooleanField('civilité', default=False, choices=TITLE_CHOICES)
    first_name = models.CharField('prénom', max_length=30)
    last_name = models.CharField('nom de famille', max_length=30)
    email = models.EmailField('courriel')
    street = models.CharField('rue', max_length=30)
    number = models.CharField('numéro', max_length=10) # 27 bis
    letterbox = models.PositiveSmallIntegerField('boîte postale', max_length=30, null=True, blank=True)
    city = models.CharField('ville', max_length=30)
    zip_code = models.PositiveSmallIntegerField('code postal', max_length=5)
    country = models.CharField('pays', max_length=2, choices=COUNTRY_CHOICES, default="BE")
    creation_date = models.DateTimeField(auto_now_add=True)
    status = models.PositiveSmallIntegerField('statut', choices=STATUS_CHOICES, default=0)
    invoice_reference = models.PositiveIntegerField('référence facture', max_length=10, unique=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        now = datetime.now()
        count = self.__class__.objects.filter(creation_date__year=now.year, creation_date__month=now.month).count() + 1
        invoice_reference = u"{}{}{:04d}".format(now.strftime("%y%m"), self.__class__.transaction_type, count)
        self.invoice_reference = int(invoice_reference)
        super(TransactionBase, self).save(*args, **kwargs)

    def structured_communication(self):
        ref = self.invoice_reference
        nbr = "{}{:02d}".format(ref, ref % 97)
        return "+++{}/{}/{}+++".format(nbr[:3], nbr[3:6], nbr[6:])


class Subscription(TransactionBase):
    """ Describes a cooperation"""
    transaction_type = '01'


class Cooperation(TransactionBase):
    """ Describes a cooperation"""
    transaction_type = '02'

    SHARE_CHOICES = (
        (1, u'1 (€ 20)'),
        (2, u'2 (€ 40)'),
        (3, u'3 (€ 60)'),
        (4, u'4 (€ 80)'),
        (5, u'5 (€ 100)'),
        (6, u'6 (€ 120)')
    )

    share_number = models.PositiveSmallIntegerField('nombre de parts', choices=SHARE_CHOICES, default="1")
