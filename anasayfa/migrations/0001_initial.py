# Generated by Django 2.0 on 2019-07-13 22:19

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dokuman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=50, verbose_name='Doküman Adı:')),
                ('slug', models.SlugField(max_length=130, unique=True)),
                ('dokuman_ekle', models.FileField(upload_to='', verbose_name='doküman yükle')),
            ],
            options={
                'verbose_name': 'Doküman',
                'verbose_name_plural': 'Dokümanlar',
            },
        ),
        migrations.CreateModel(
            name='Genel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('başlık', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=130, unique=True)),
                ('kısa_içerik', ckeditor.fields.RichTextField()),
                ('uzun_içerik', ckeditor.fields.RichTextField()),
                ('resim_grubu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resim_grubu', to='shop.Resim', verbose_name='Resim grubu')),
            ],
            options={
                'verbose_name': 'Genel-Konu',
                'verbose_name_plural': 'Genel-Konular',
            },
        ),
        migrations.CreateModel(
            name='RenkFont',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(blank=True, choices=[('bg-primary', 'mavi'), ('bg-secondary', 'gri'), ('bg-success', 'yeşil'), ('bg-danger', 'kırmızı'), ('bg-warning', 'turuncu'), ('bg-info', 'açık mavi'), ('bg-light', 'ince beyaz'), ('bg-dark', 'koyu siyah'), ('bg-white', 'kalın beyaz'), ('bg-transparent', 'ince siyah')], max_length=30, verbose_name='komple sayfanın arka plan rengi')),
                ('kategorilerim_yazı_rengi', models.CharField(blank=True, choices=[('text-primary', 'mavi'), ('text-secondary', 'gri'), ('text-success', 'yeşil'), ('text-danger', 'kırmızı'), ('text-warning', 'turuncu'), ('text-info', 'açık mavi'), ('text-light', 'ince beyaz'), ('text-dark', 'koyu siyah'), ('text-body', 'az koyu siyah'), ('text-muted', 'sönük gri'), ('text-white', 'kalın beyaz'), ('text-black-50', 'ince siyah'), ('text-white-50', 'kalın gri')], max_length=30, verbose_name='KATEGORİLERİM başlığının yazı rengi')),
                ('kategorilerim_yazısı_arka_plan_rengi', models.CharField(blank=True, choices=[('bg-primary', 'mavi'), ('bg-secondary', 'gri'), ('bg-success', 'yeşil'), ('bg-danger', 'kırmızı'), ('bg-warning', 'turuncu'), ('bg-info', 'açık mavi'), ('bg-light', 'ince beyaz'), ('bg-dark', 'koyu siyah'), ('bg-white', 'kalın beyaz'), ('bg-transparent', 'ince siyah')], max_length=30, verbose_name='KATEGORİLERİM başlığının arka plan rengi')),
                ('kategorilerim_arka_plan_rengi', models.CharField(blank=True, choices=[('bg-primary', 'mavi'), ('bg-secondary', 'gri'), ('bg-success', 'yeşil'), ('bg-danger', 'kırmızı'), ('bg-warning', 'turuncu'), ('bg-info', 'açık mavi'), ('bg-light', 'ince beyaz'), ('bg-dark', 'koyu siyah'), ('bg-white', 'kalın beyaz'), ('bg-transparent', 'ince siyah')], max_length=30, verbose_name='KATEGORİLERİM bölümünün arka plan rengi')),
                ('kategorilerim_yazı_boyutu', models.CharField(blank=True, choices=[('8', 8), ('10', 10), ('12', 12), ('14', 14), ('16', 16), ('18', 18), ('20', 20), ('22', 22), ('24', 24)], max_length=30, verbose_name='KATEGORİLERİM başlığının yazı büyüklğü')),
                ('urunler_yazı_boyutu', models.CharField(blank=True, choices=[('8', 8), ('10', 10), ('12', 12), ('14', 14), ('16', 16), ('18', 18), ('20', 20), ('22', 22), ('24', 24)], max_length=30, verbose_name='Ürünler başlığının yazı büyüklğü')),
                ('urunler_arka_plan_rengi', models.CharField(blank=True, choices=[('bg-primary', 'mavi'), ('bg-secondary', 'gri'), ('bg-success', 'yeşil'), ('bg-danger', 'kırmızı'), ('bg-warning', 'turuncu'), ('bg-info', 'açık mavi'), ('bg-light', 'ince beyaz'), ('bg-dark', 'koyu siyah'), ('bg-white', 'kalın beyaz'), ('bg-transparent', 'ince siyah')], max_length=30, verbose_name='Ürünler başlığının arka plan rengi')),
                ('urunler_yazı_büyüklüğü', models.CharField(blank=True, choices=[('8', 8), ('10', 10), ('12', 12), ('14', 14), ('16', 16), ('18', 18), ('20', 20), ('22', 22), ('24', 24)], max_length=30, verbose_name='Ürün isimlerinin yazı büyüklğü')),
                ('ilk_üç_button', models.CharField(blank=True, choices=[('btn-primary', 'mavi'), ('btn-secondary', 'gri'), ('btn-success', 'yeşil'), ('btn-danger', 'kırmızı'), ('btn-warning', 'turuncu'), ('btn-info', 'açık mavi'), ('btn-light', 'ince beyaz'), ('btn-dark', 'koyu siyah'), ('btn-white', 'kalın beyaz'), ('btn-link', 'sadece mavi link')], max_length=30, verbose_name="ürün kategorilerindeki ilk üç button'un rengi")),
                ('dördüncü_button', models.CharField(blank=True, choices=[('btn-primary', 'mavi'), ('btn-secondary', 'gri'), ('btn-success', 'yeşil'), ('btn-danger', 'kırmızı'), ('btn-warning', 'turuncu'), ('btn-info', 'açık mavi'), ('btn-light', 'ince beyaz'), ('btn-dark', 'koyu siyah'), ('btn-white', 'kalın beyaz'), ('btn-link', 'sadece mavi link')], max_length=30, verbose_name="ürün kategorilerindeki dördüncü button'un rengi")),
                ('beşinci_button', models.CharField(blank=True, choices=[('btn-primary', 'mavi'), ('btn-secondary', 'gri'), ('btn-success', 'yeşil'), ('btn-danger', 'kırmızı'), ('btn-warning', 'turuncu'), ('btn-info', 'açık mavi'), ('btn-light', 'ince beyaz'), ('btn-dark', 'koyu siyah'), ('btn-white', 'kalın beyaz'), ('btn-link', 'sadece mavi link')], max_length=30, verbose_name="ürün kategorilerindeki beşinci button'un rengi")),
                ('altıncı_button', models.CharField(blank=True, choices=[('btn-primary', 'mavi'), ('btn-secondary', 'gri'), ('btn-success', 'yeşil'), ('btn-danger', 'kırmızı'), ('btn-warning', 'turuncu'), ('btn-info', 'açık mavi'), ('btn-light', 'ince beyaz'), ('btn-dark', 'koyu siyah'), ('btn-white', 'kalın beyaz'), ('btn-link', 'sadece mavi link')], max_length=30, verbose_name="ürün kategorilerindeki altıncı button'un rengi")),
                ('yedinci_button', models.CharField(blank=True, choices=[('btn-primary', 'mavi'), ('btn-secondary', 'gri'), ('btn-success', 'yeşil'), ('btn-danger', 'kırmızı'), ('btn-warning', 'turuncu'), ('btn-info', 'açık mavi'), ('btn-light', 'ince beyaz'), ('btn-dark', 'koyu siyah'), ('btn-white', 'kalın beyaz'), ('btn-link', 'sadece mavi link')], max_length=30, verbose_name="ürün kategorilerindeki yedinci button'un rengi")),
                ('sekizinci_button', models.CharField(blank=True, choices=[('btn-primary', 'mavi'), ('btn-secondary', 'gri'), ('btn-success', 'yeşil'), ('btn-danger', 'kırmızı'), ('btn-warning', 'turuncu'), ('btn-info', 'açık mavi'), ('btn-light', 'ince beyaz'), ('btn-dark', 'koyu siyah'), ('btn-white', 'kalın beyaz'), ('btn-link', 'sadece mavi link')], max_length=30, verbose_name="ürün kategorilerindeki sekizinci button'un rengi")),
                ('buttonlar_yazı_büyüklüğü', models.CharField(blank=True, choices=[('8', 8), ('10', 10), ('12', 12), ('14', 14), ('16', 16), ('18', 18), ('20', 20), ('22', 22), ('24', 24)], max_length=30, verbose_name='Kategori isimlerinin yazı büyüklğü')),
                ('isim', models.CharField(default='Site Geneli Özellikler', max_length=50)),
                ('navbardaki_yazı', models.CharField(default='KİTAP OKUMA HEDEFİNİZE PLANLI ÇÖZÜM', max_length=250, verbose_name='Navbardaki yazı')),
                ('site_adı', models.CharField(default='Kitap Turnuvası', max_length=250, verbose_name='Sitenin Adı')),
                ('cep_telefonu', models.CharField(default='0505 763 63 81', max_length=50, verbose_name='Sitenin Adı')),
            ],
            options={
                'verbose_name': 'Renk-ve-Yazı',
                'verbose_name_plural': 'Renk-ve-Yazılar',
            },
        ),
        migrations.CreateModel(
            name='Slayt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=50, verbose_name='Başlık')),
                ('yazı', models.CharField(max_length=200, verbose_name='Yazı')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='resim')),
                ('aktif', models.BooleanField(default=False, help_text='Sitede görünmesini istiyorsanız işaretleyiniz!!!', verbose_name='Aktif mi?')),
                ('sıralama_sayısı', models.PositiveIntegerField(default=0, verbose_name='Anasayfa Sıralama Sayısı')),
            ],
            options={
                'verbose_name': 'Slayt-Resmi',
                'verbose_name_plural': 'Slayt-Resimleri',
                'ordering': ['sıralama_sayısı'],
            },
        ),
        migrations.CreateModel(
            name='Yorum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=50, verbose_name='Kullanıcı Adı:')),
                ('okul', models.CharField(choices=[('İlkokul', 'İlkokul'), ('Ortaokul', 'Ortaokul')], max_length=30, verbose_name='Okulunuz:')),
                ('content', models.TextField(verbose_name='Yorum:')),
                ('aktif', models.BooleanField(default=False, help_text='Sitede görünmesini istiyorsanız işaretleyiniz!!!', verbose_name='Aktif mi?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma tarihi')),
            ],
            options={
                'verbose_name': 'Yorum',
                'verbose_name_plural': 'Yorumlar',
                'ordering': ['-created_at'],
            },
        ),
    ]
