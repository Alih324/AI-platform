import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(
                decimal_places=2,
                max_digits=10,
                validators=[django.core.validators.MinValueValidator(0)],
            ),
        ),
        migrations.AlterField(
            model_name='product_review',
            name='author',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='product_reviews',
                to='auth.user',
            ),
        ),
        migrations.AlterField(
            model_name='product_review',
            name='rating',
            field=models.PositiveSmallIntegerField(
                default=5,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(5),
                ],
            ),
        ),
        migrations.AlterModelOptions(
            name='product_review',
            options={
                'ordering': ['-created_at'],
                'verbose_name': 'Product review',
                'verbose_name_plural': 'Product reviews',
            },
        ),
    ]
