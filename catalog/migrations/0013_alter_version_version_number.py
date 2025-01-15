from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0012_alter_version_version_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="version",
            name="version_number",
            field=models.SmallIntegerField(
                help_text="Введите номер версии",
                max_length=20,
                unique=True,
                verbose_name="Номер версии",
            ),
        ),
    ]