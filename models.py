from django.contrib.auth.models import User
from django.db import models


class Body(models.Model):
    id_body = models.AutoField(primary_key=True)
    id_body_material = models.ForeignKey('BodyMaterial', models.DO_NOTHING, db_column='id_body_material')
    id_body_type = models.ForeignKey('BodyType', models.DO_NOTHING, db_column='id_body_type')

    class Meta:
        db_table = 'body'


class BodyMaterial(models.Model):
    id_body_material = models.AutoField(primary_key=True)
    body_material = models.CharField(unique=True, max_length=45)

    class Meta:
        db_table = 'body_material'


class BodyType(models.Model):
    id_body_type = models.AutoField(primary_key=True)
    body_type = models.CharField(unique=True, max_length=45)

    class Meta:
        db_table = 'body_type'


class Category(models.Model):
    id_category = models.AutoField(primary_key=True)
    category = models.CharField(max_length=45)

    class Meta:
        db_table = 'category'


class Color(models.Model):
    id_color = models.AutoField(primary_key=True)
    color = models.CharField(unique=True, max_length=45)

    class Meta:
        db_table = 'color'


class Neck(models.Model):
    id_neck = models.AutoField(primary_key=True)
    id_neck_material = models.ForeignKey('NeckMaterial', models.DO_NOTHING, db_column='id_neck_material')
    id_neck_type = models.ForeignKey('NeckType', models.DO_NOTHING, db_column='id_neck_type')
    frets = models.IntegerField()

    class Meta:
        db_table = 'neck'


class NeckMaterial(models.Model):
    id_neck_material = models.AutoField(primary_key=True)
    neck_material = models.CharField(unique=True, max_length=45)

    class Meta:
        db_table = 'neck_material'


class NeckType(models.Model):
    id_neck_type = models.AutoField(primary_key=True)
    neck_type = models.CharField(unique=True, max_length=45)

    class Meta:
        db_table = 'neck_type'


class Producer(models.Model):
    id_producer = models.AutoField(primary_key=True)
    producer = models.CharField(unique=True, max_length=45)
    website = models.CharField(unique=True, max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'producer'


class Product(models.Model):
    id_product = models.AutoField(primary_key=True)
    model = models.CharField(unique=True, max_length=45)
    id_category = models.ForeignKey(Category, models.DO_NOTHING, db_column='id_category')
    id_color = models.ForeignKey(Color, models.DO_NOTHING, db_column='id_color')
    id_neck = models.ForeignKey(Neck, models.DO_NOTHING, db_column='id_neck')
    id_body = models.ForeignKey(Body, models.DO_NOTHING, db_column='id_body')
    price = models.IntegerField()
    id_producer = models.ForeignKey(Producer, models.DO_NOTHING, db_column='id_producer')

    class Meta:
        db_table = 'product'
