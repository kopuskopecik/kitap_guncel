# Generated by Django 2.0 on 2019-07-13 22:19

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_student', models.BooleanField(default=False)),
                ('is_teacher', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Etkinlik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(choices=[('k', 'Kitap Okuma Turnuvası'), ('p', 'Kitap Okuma Etkinlikleri'), ('a', 'Anlamayı Geliştirme Turnuvası'), ('b', 'Birinci Sınıf Okuma Etkinliği'), ('o', 'Okul Öncesi Masal Etkinliği'), ('l', 'Lise "Kitap Koçum" Etkinliği')], max_length=1)),
                ('sinif_adi', models.CharField(max_length=30)),
                ('hedef', models.PositiveIntegerField()),
                ('startting_date', models.DateTimeField(auto_now_add=True, max_length=30)),
                ('finishing_date', models.DateTimeField(auto_now=True, max_length=30)),
                ('odul', models.CharField(blank=True, choices=[('b', 'Birinci Ödül'), ('i', 'İkinci Ödül'), ('ü', 'Üçüncü Ödül'), ('d', 'Dördüncü Ödül')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Kitap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(blank=True, max_length=30)),
                ('sayfa', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('takim', models.CharField(blank=True, choices=[('t', 'Turuncu'), ('m', 'Mavi'), ('k', 'Kırmızı'), ('s', 'Sarı'), ('y', 'Yeşil')], max_length=1)),
                ('bireysel_odulu', models.CharField(blank=True, max_length=30)),
                ('takim_odulu', models.CharField(blank=True, max_length=30)),
                ('sayfa', models.PositiveIntegerField(default=0)),
                ('no', models.PositiveIntegerField(default=0)),
                ('kitap', models.ManyToManyField(blank=True, related_name='kitaplar', to='accounts.Kitap')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('okul_adi', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='student',
            name='ogretmen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Teacher'),
        ),
        migrations.AddField(
            model_name='etkinlik',
            name='asistan',
            field=models.ManyToManyField(related_name='asistanlar', to='accounts.Student'),
        ),
        migrations.AddField(
            model_name='etkinlik',
            name='ogrenci',
            field=models.ManyToManyField(related_name='ogrenciler', to='accounts.Student'),
        ),
        migrations.AddField(
            model_name='etkinlik',
            name='ogretmen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Teacher'),
        ),
    ]
