from django.db import models
from django.urls import reverse


class Body(models.Model):
    id_body = models.AutoField(primary_key=True)
    id_body_material = models.ForeignKey('BodyMaterial', models.DO_NOTHING, db_column='id_body_material')
    id_body_type = models.ForeignKey('BodyType', models.DO_NOTHING, db_column='id_body_type')

    def __str__(self):
        return '%s %s' % (self.id_body_material, self.id_body_type)


class BodyMaterial(models.Model):
    id_body_material = models.AutoField(primary_key=True)
    body_material = models.CharField(unique=True, max_length=45)

    def __str__(self):
        return '%s' % self.body_material


class BodyType(models.Model):
    id_body_type = models.AutoField(primary_key=True)
    body_type = models.CharField(unique=True, max_length=45)

    def __str__(self):
        return '%s' % self.body_type


class Category(models.Model):
    id_category = models.AutoField(primary_key=True)
    category = models.CharField(max_length=45)

    def __str__(self):
        return '%s' % self.category


class Color(models.Model):
    id_color = models.AutoField(primary_key=True)
    color = models.CharField(unique=True, max_length=45)

    def __str__(self):
        return '%s' % self.color


class Neck(models.Model):
    id_neck = models.AutoField(primary_key=True)
    id_neck_material = models.ForeignKey('NeckMaterial', models.DO_NOTHING, db_column='id_neck_material')
    id_neck_type = models.ForeignKey('NeckType', models.DO_NOTHING, db_column='id_neck_type')
    frets = models.IntegerField()

    def __str__(self):
        return '%s %s frets: %s' % (self.id_neck_material, self.id_neck_type, self.frets)


class NeckMaterial(models.Model):
    id_neck_material = models.AutoField(primary_key=True)
    neck_material = models.CharField(unique=True, max_length=45)

    def __str__(self):
        return '%s' % self.neck_material


class NeckType(models.Model):
    id_neck_type = models.AutoField(primary_key=True)
    neck_type = models.CharField(unique=True, max_length=45)

    def __str__(self):
        return '%s' % self.neck_type


class Producer(models.Model):
    id_producer = models.AutoField(primary_key=True)
    producer = models.CharField(unique=True, max_length=45)
    website = models.CharField(unique=True, max_length=45, blank=True, null=True)

    def __str__(self):
        return '%s' % self.producer


class Product(models.Model):
    id_product = models.AutoField(primary_key=True)
    model = models.CharField(unique=True, max_length=45)
    id_category = models.ForeignKey(Category, models.DO_NOTHING, db_column='id_category')
    id_color = models.ForeignKey(Color, models.DO_NOTHING, db_column='id_color')
    id_neck = models.ForeignKey(Neck, models.DO_NOTHING, db_column='id_neck')
    id_body = models.ForeignKey(Body, models.DO_NOTHING, db_column='id_body')
    price = models.IntegerField()
    id_producer = models.ForeignKey(Producer, models.DO_NOTHING, db_column='id_producer')

    def __str__(self):
        return '%s (%s)' % (self.model, self.id_category)

    def get_absolute_url(self):
        return reverse('product_detail',
                       args=[self.id_product])

    def ge_id(self):
        return self.id_product
