from django.db import models

class PatreonModel(models.Model): 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        abstract = True

class Person(PatreonModel): 
    pass 

class Page(PatreonModel): 
    owners = models.ManyToManyField(Person) 

class Update(PatreonModel): 
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    content = models.TextField()

class Attachments(PatreonModel): 
    uploaded = models.FileField() 
    update = models.ForeignKey(Update, on_delete=models.CASCADE)
