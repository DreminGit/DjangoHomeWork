from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0014_alter_version_version_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="version",
            name="is_current",
            field=models.BooleanField(
                default=True,
                help_text="Установите, если это текущая версия продукта",
                verbose_name="Текущая версия",
            ),
        ),
    ]