# Generated by Django 4.2.6 on 2023-12-13 16:31

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(blank=True, max_length=200, null=True)),
                ('aktif', models.BooleanField(default=True)),
                ('banner_satu', django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=80, scale=None, size=[575, 200], upload_to='gambar/banner', verbose_name='Gambar (575 x 200 pixel)')),
                ('banner_dua', models.ImageField(null=True, upload_to='gambar/banner', verbose_name='Gambar (575 x 200 pixel)')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Kategori',
            },
        ),
        migrations.CreateModel(
            name='Kontak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200, null=True, verbose_name='Nama')),
                ('no_whats_app', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='No WhatsApp')),
                ('email', models.EmailField(max_length=200, null=True, verbose_name='Email')),
                ('subject', models.CharField(max_length=200, null=True, verbose_name='Subject')),
                ('isi', models.TextField(max_length=200, null=True, verbose_name='Isi')),
            ],
            options={
                'verbose_name_plural': 'Kontak',
            },
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200, null=True, verbose_name='Nama')),
                ('keterangan', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('gambar', models.ImageField(null=True, upload_to='gambar/profil', verbose_name='Gambar (1920 x 1200 pixel)')),
                ('tanggal_upload', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Tanggal Upload')),
            ],
            options={
                'verbose_name_plural': 'Profil',
            },
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teks_satu', models.CharField(blank=True, max_length=200, null=True, verbose_name='Teks Satu')),
                ('teks_dua', models.CharField(blank=True, max_length=200, null=True, verbose_name='Teks Dua')),
                ('teks_tiga', models.CharField(blank=True, max_length=200, null=True, verbose_name='Teks Tiga')),
                ('gambar_slide', models.ImageField(null=True, upload_to='gambar/slide', verbose_name='Gambar Slide (270 x 250pixel)')),
                ('aktif', models.BooleanField(default=True, verbose_name='Status')),
            ],
            options={
                'verbose_name_plural': 'Slide',
            },
        ),
        migrations.CreateModel(
            name='Statis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alamat_kami', models.TextField(max_length=200, null=True, verbose_name='Alamat')),
                ('telpon', models.CharField(max_length=200, null=True, verbose_name='No Telepon')),
                ('email', models.EmailField(max_length=200, null=True, verbose_name='Email')),
            ],
            options={
                'verbose_name_plural': 'Statis',
            },
        ),
        migrations.CreateModel(
            name='Produk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_produk', models.CharField(blank=True, max_length=200, null=True)),
                ('gambar_satu', models.ImageField(null=True, upload_to='gambar/banner', verbose_name='Gambar 1 (270 x 250pixel)')),
                ('gambar_dua', models.ImageField(null=True, upload_to='gambar/banner', verbose_name='Gambar 2 (270 x 250pixel)')),
                ('gambar_tiga', models.ImageField(null=True, upload_to='gambar/banner', verbose_name='Gambar 3 (270 x 250pixel)')),
                ('gambar_empat', models.ImageField(null=True, upload_to='gambar/banner', verbose_name='Gambar 4 (270 x 250pixel)')),
                ('gambar_lima', models.ImageField(null=True, upload_to='gambar/banner', verbose_name='Gambar 5 (270 x 250pixel)')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='Slug')),
                ('keterangan', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('harga', models.PositiveIntegerField(blank=True, null=True, verbose_name='Harga Rp.')),
                ('no_whats_app', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='No WhatsApp')),
                ('tanggal_upload', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Tanggal Upload')),
                ('diskon', models.IntegerField(blank=True, default=0, null=True, verbose_name='Diskon %')),
                ('dibeli', models.IntegerField(blank=True, default=0, null=True, verbose_name='Dibeli')),
                ('keterangan_barang', models.CharField(choices=[('Baru', 'Baru'), ('Lama', 'Lama')], max_length=200, null=True, verbose_name='Ket. Barang')),
                ('kategori', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='produks', to='subhan.kategori')),
            ],
            options={
                'verbose_name_plural': 'Produk',
            },
        ),
    ]