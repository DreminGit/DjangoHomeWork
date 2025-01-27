import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_alter_product_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                help_text="введите название категории",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product",
                to="catalog.category",
                verbose_name="категория",
            ),
        ),
    ]