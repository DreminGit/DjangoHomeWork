from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0018_product_owner"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["name", "category", "price", "created_at", "updated_at"],
                "permissions": [
                    ("can_edit_description", "Can edit description"),
                    ("can_edit_category", "Can edit category"),
                ],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
    ]