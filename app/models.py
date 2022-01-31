from django.db import models

# Create your models here.

# class ElementData(models.Model):
#     label = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.label
class Element(models.Model):

    href = models.CharField(max_length=255)
    parent = models.ForeignKey("self", on_delete=models.PROTECT, null = True, blank= True)
    label = models.CharField(max_length=255)


    def __str__(self):
        return str(self.label)




