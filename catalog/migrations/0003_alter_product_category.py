import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_alter_category_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                help_text="введите название категории",
                on_delete=django.db.models.deletion.CASCADE,
                to="catalog.category",
                verbose_name="категория",
            ),
        ),
    ]