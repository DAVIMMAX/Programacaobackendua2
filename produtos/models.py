from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    preco =models.DecimalField(max_digits=10, decimal_places=2)
    validade = models.DateField(null=True, blank= True)

    def __str__(self):
        return self.nome