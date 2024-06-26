# Generated by Django 4.1.5 on 2023-02-01 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='AttributeName',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('nazev', models.CharField(blank=True, default='', max_length=15)),
                ('kod', models.CharField(blank=True, default='', max_length=15)),
                ('zobrazit', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AttributeValue',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('hodnota', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('nazev', models.CharField(blank=True, max_length=63)),
                ('obrazek', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('nazev', models.CharField(blank=True, max_length=63)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('cena', models.DecimalField(decimal_places=2, max_digits=12)),
                ('mena', models.CharField(blank=True, max_length=3)),
                ('published_on', models.DateTimeField(blank=True, null=True)),
                ('is_published', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('nazev', models.CharField(max_length=63)),
                ('obrazek_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data_api.image')),
                ('product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data_api.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductAttributes',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('attribute_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data_api.attribute')),
                ('product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data_api.product')),
            ],
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('nazev', models.CharField(blank=True, default='', max_length=63)),
                ('attributes_ids', models.ManyToManyField(blank=True, to='data_api.attribute')),
                ('obrazek_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data_api.image')),
                ('products_ids', models.ManyToManyField(blank=True, to='data_api.product')),
            ],
        ),
        migrations.AddField(
            model_name='attribute',
            name='hodnota_atributu_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data_api.attributevalue'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='nazev_atributu_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data_api.attributename'),
        ),
    ]
