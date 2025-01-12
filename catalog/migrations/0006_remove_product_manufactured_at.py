from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0005_product_manufactured_at_alter_product_created_at"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="manufactured_at",
        ),
    ]