import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='введите наименование категории', max_length=50, verbose_name='наименование')),
                ('description', models.CharField(help_text='введите описание категории', max_length=50, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='введите наименование продукта', max_length=50, verbose_name='наименование продукта')),
                ('description', models.CharField(help_text='опишите продукта', max_length=150, verbose_name='описание')),
                ('image', models.ImageField(blank=True, help_text='загрузите изображение продукта', null=True, upload_to='products/')),
                ('price', models.IntegerField(help_text='стоимость продукта', verbose_name='стоимость')),
                ('created_at', models.DateField(verbose_name='дата создания')),
                ('updated_at', models.DateField(verbose_name='дата редактирования')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ['name', 'category', 'price', 'created_at', 'updated_at'],
            },
        ),
    ]