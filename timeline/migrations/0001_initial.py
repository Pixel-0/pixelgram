# Generated by Django 2.2.5 on 2019-09-02 08:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('caption', models.TextField(max_length=280)),
                ('time_posted', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='default.jpg', upload_to='avatar/')),
                ('bio', models.TextField(blank=True, default='', max_length=140)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timeline.Image')),
                ('liked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timeline.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timeline.Profile'),
        ),
        migrations.CreateModel(
            name='Follows',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('following', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='following', to='timeline.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Followed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followers', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='followed_by', to='timeline.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=140)),
                ('comment_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timeline.Profile')),
                ('commented_on', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timeline.Image')),
            ],
        ),
    ]
