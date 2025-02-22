

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Theloai',
            fields=[
                ('IDtheloai', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('tentheloai', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Truyen',
            fields=[
                ('IDtruyen', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('tentruyen', models.CharField(max_length=100)),
                ('tacgia', models.CharField(max_length=100)),
                ('nguon', models.CharField(max_length=100)),
                ('trangthai', models.BooleanField(default=False)),
                ('yeuthich', models.IntegerField(default=0)),
                ('luotxem', models.IntegerField(default=0)),
                ('gioithieu', models.CharField(max_length=5000)),
                ('anh', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Checktheloai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IDtheloai', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Data.theloai')),
                ('IDtruyen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Data.truyen')),
            ],
        ),
        migrations.CreateModel(
            name='Chaptruyen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chap', models.IntegerField(default=0)),
                ('tenchap', models.CharField(max_length=100)),
                ('noidung', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('IDtruyen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Data.truyen')),
            ],
        ),
    ]
