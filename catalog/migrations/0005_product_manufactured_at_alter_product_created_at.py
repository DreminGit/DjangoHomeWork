import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0004_alter_product_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="manufactured_at",
            field=models.DateField(
                blank=True, null=True, verbose_name="дата производства продукта"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="created_at",
            field=models.DateField(
                default=datetime.datetime.now, verbose_name="дата создания"
            ),
        ),
    ]