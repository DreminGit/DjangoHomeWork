from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0011_version_delete_subject"),
    ]

    operations = [
        migrations.AlterField(
            model_name="version",
            name="version_number",
            field=models.SmallIntegerField(
                help_text="Введите номер версии",
                max_length=20,
                verbose_name="Номер версии",
            ),
        ),
    ]