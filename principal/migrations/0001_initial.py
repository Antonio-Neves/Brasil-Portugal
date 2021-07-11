# Generated by Django 3.2.4 on 2021-07-11 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='principal.basemodel')),
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=100, unique=True, verbose_name='Category')),
                ('category_slug', models.SlugField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['category_name'],
            },
            bases=('principal.basemodel',),
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='principal.basemodel')),
                ('sub_category_id', models.AutoField(primary_key=True, serialize=False)),
                ('sub_category_name', models.CharField(max_length=100, unique=True, verbose_name='Sub Category')),
                ('sub_category_slug', models.SlugField(max_length=150, unique=True)),
                ('sub_category_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategorycategory', to='principal.category')),
            ],
            options={
                'verbose_name': 'Subcategory',
                'verbose_name_plural': 'Subcategories',
                'ordering': ['sub_category_name'],
            },
            bases=('principal.basemodel',),
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='principal.basemodel')),
                ('article_id', models.AutoField(primary_key=True, serialize=False)),
                ('article_name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('article_slug', models.SlugField(max_length=150, unique=True)),
                ('article_content', models.TextField()),
                ('article_status', models.CharField(choices=[('0', 'Draft'), ('1', 'Publish')], default=0, max_length=1)),
                ('article_cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articlesubcategory', to='principal.subcategory')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
                'ordering': ['article_name'],
            },
            bases=('principal.basemodel',),
        ),
    ]
