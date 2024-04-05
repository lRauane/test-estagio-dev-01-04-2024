from django.db import models


class Consumer(models.Model):
    name = models.CharField("Nome do Consumidor", max_length=128)
    document = models.CharField("Documento(CPF/CNPJ)", max_length=14, unique=True)
    zip_code = models.CharField("CEP", max_length=8, null=True, blank=True)
    city = models.CharField("Cidade", max_length=128)
    state = models.CharField("Estado", max_length=128)
    consumption = models.IntegerField("Consumo(kWh)", blank=True, null=True)
    distributor_tax = models.FloatField(
        "Tarifa da Distribuidora", blank=True, null=True
    )
    discount_rule = models.ForeignKey('DiscountRule', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class DiscountRule(models.Model):
    # Tipo de consumo
    CONSUMER_TYPES = (
        ('Residencial', 'Residencial'),
        ('Comercial', 'Comercial'),
        ('Industrial', 'Industrial'),
    )

    # Opções de faixa de consumo
    CONSUMPTION_RANGE_CHOICES = (
        ('< 10.000 kWh', '< 10.000 kWh'),
        ('>= 10.000 kWh e <= 20.000 kWh', '>= 10.000 kWh e <= 20.000 kWh'),
        ('> 20.000 kWh', '> 20.000 kWh'),
    )

    consumption_range = models.CharField("Consumption Range", max_length=50, choices=CONSUMPTION_RANGE_CHOICES)
    consumer_type = models.CharField("Consumer Type", max_length=20, choices=CONSUMER_TYPES)
    cover_value = models.FloatField("Cover Value")
    discount_value = models.FloatField("Discount Value")

    def __str__(self):
        return f"{self.consumer_type} - {self.consumption_range}"
