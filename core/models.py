from django.db import models


class Document(models.Model):
    PP = 'PP'
    ID = 'ID'
    OT = 'OT'
    DOC_TYPES = (
        (PP, 'Passport'),
        (ID, 'Identity card'),
        (OT, 'Others')
    )

    dtype = models.CharField(choices=DOC_TYPES, max_length=2)
    doc_number = models.CharField(max_length=50)

    def __str__(self):
        return self.doc_number


class Costumer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    documents = models.ManyToManyField(Document)

    def __str__(self):
        return self.name

