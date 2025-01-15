import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0010_subject"),
    ]

    operations = [
        migrations.CreateModel(
            name="Version",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "version_number",
                    models.CharField(
                        help_text="Введите номер версии",
                        max_length=20,
                        verbose_name="Номер версии",
                    ),
                ),
                (
                    "version_name",
                    models.CharField(
                        help_text="Введите название версии",
                        max_length=100,
                        verbose_name="Название версии",
                    ),
                ),
                (
                    "is_current",
                    models.BooleanField(
                        default=False,
                        help_text="Установите, если это текущая версия продукта",
                        verbose_name="Текущая версия",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        help_text="Выберите продукт, к которому относится версия",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="versions",
                        to="catalog.product",
                        verbose_name="Продукт",
                    ),
                ),
            ],
            options={
                "verbose_name": "Версия",
                "verbose_name_plural": "Версии",
                "ordering": ["-is_current", "version_number"],
            },
        ),
        migrations.DeleteModel(
            name="Subject",
        ),
    ]