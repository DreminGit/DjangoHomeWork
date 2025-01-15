from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0008_alter_product_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="views_counter",
            field=models.PositiveIntegerField(default=0, verbose_name="просмотры"),
        ),
    ]