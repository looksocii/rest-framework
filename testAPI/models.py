from django.db import models

# Create your models here.
class Useraccount(models.Model):
    id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    imguserurl = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'useraccount'


class Booklist(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    short_title = models.TextField(blank=True, null=True)
    img_book = models.CharField(max_length=255, blank=True, null=True)
    price_rent = models.FloatField(blank=True, null=True)
    category = models.ForeignKey('Category', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booklist'


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    content = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'


class Payment(models.Model):
    id = models.IntegerField(primary_key=True)
    date_time = models.DateField(blank=True, null=True)
    exp_date = models.DateField(blank=True, null=True)
    total_price = models.FloatField(blank=True, null=True)
    useraccount_id = models.IntegerField(blank=True, null=True)
    booklist_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment'
