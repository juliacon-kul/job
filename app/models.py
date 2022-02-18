from django.db import models
import nums_from_string

# Create your models here.

class ElementManager(models.Manager):
    def create_element(self, href, parent_id, label, children):
        element = self.create(href = href, parent_id = parent_id, label = label, children = children)
        element.children_list()
        return element

class Element(models.Model):

    href = models.CharField(max_length=255)
    parent_id = models.ForeignKey("self", on_delete=models.PROTECT, null = True, blank= True)
    label = models.CharField(max_length=255)
    children = models.CharField(max_length=255, default= 0, blank = True)

    def __str__(self):
        return self.label

    objects = ElementManager()

    def children_list(self, *args,**kwargs):
        el = self.parent_id
        child = nums_from_string.get_nums(el.children)
        if (len(child) == 1 and child[0] == 0):
            child = []
            child.append(self.id)
        else: child.append(self.id)
        el.children = child
        el.save()

    def children_list_delete(self, *args,**kwargs):
        el = self.parent_id
        child = nums_from_string.get_nums(el.children)
        child.remove(self.id)
        el.children = child
        el.save()



















