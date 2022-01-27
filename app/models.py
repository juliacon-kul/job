from django.db import models

# Create your models here.

# class ElementData(models.Model):
#     label = models.CharField(max_length=255)

    # def __str__(self):
    #     return self.label
class Element(models.Model):

    href = models.CharField(max_length=255)
    parent = models.ForeignKey("self", on_delete=models.PROTECT, null = True, blank= True)
    # data = models.OneToOneField(ElementData, on_delete=models.CASCADE)
    label = models.CharField(max_length=255)
    # connection = models.ForeignKey('self', on_delete=models.SET_NULL, null = True, blank= True ) - это нужно для добавления дополнительной связи, пока не работает
    # hierarchical_level = () - нужен метод для рассчета уровня иерархии

    def __str__(self):
        return self.label




