from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="description",
            field=models.CharField(
                help_text="введите описание категории",
                max_length=200,
                verbose_name="описание",
            ),
        ),
    ]