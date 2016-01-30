from django.db import models
# a function whcih replaces whitespaces with hyphens
from django.template.defaultfilters import slugify

class Category(models.Model):
    name = models.CharField(max_length= 128, unique= True)
    likes = models.IntegerField(default = 0)
    views = models.IntegerField(default= 0)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        # Uncomment if you don't want the slug to change every time the name changes
        #if self.id is None:
        #slug = slugify(self.name)
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Page(models.Model):
    #category is the foreign key
    category = models.ForeignKey(Category)
    title = models.CharField(max_length= 128)
    url = models.URLField()
    views = models.IntegerField(default = 0)

    def __unicode__(self):
        return self.title
