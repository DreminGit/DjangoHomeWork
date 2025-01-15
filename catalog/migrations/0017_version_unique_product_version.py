from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0016_alter_version_version_number"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="version",
            constraint=models.UniqueConstraint(
                fields=("product", "version_number"), name="unique_product_version"
            ),
        ),
    ]