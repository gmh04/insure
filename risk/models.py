from django.db import models

# core risk entity, e.g automobiles, houses, prizes
class RiskEntity(models.Model):
    name = models.CharField(max_length=10)

# supported form data type, e.g text, number, date or enum
class RiskAttribute(models.Model):
    attr_type = models.CharField(max_length=30)

# entity/attribute mapping with any value
class RiskValue(models.Model):
    label = models.CharField(max_length=10)
    entity = models.ForeignKey(RiskEntity, on_delete=models.CASCADE)
    attr = models.ForeignKey(RiskAttribute, on_delete=models.CASCADE)
    value = models.TextField()
