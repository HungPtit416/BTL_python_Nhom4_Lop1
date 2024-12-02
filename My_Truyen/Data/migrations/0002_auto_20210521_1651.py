

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaptruyen',
            name='thoigian',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='truyen',
            name='gioithieu',
            field=models.TextField(max_length=5000),
        ),
        migrations.CreateModel(
            name='Theodoi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IDtruyen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Data.truyen')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
