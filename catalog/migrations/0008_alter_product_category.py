import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0007_alter_product_updated_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                help_text="введите название категории",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="product",
                to="catalog.category",
                verbose_name="категория",
            ),
        ),
    ]