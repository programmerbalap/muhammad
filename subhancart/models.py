from django.db import models

# Create your models here.
from django.db import models
from subhan.models import Produk
# Create your models here.


class Transaksi(models.Model):
    Status = (
        ('Baru', 'Baru'),
        ('Lunas', 'Lunas'),
    )
    no_transaksi = models.CharField(
        max_length=200, blank=False, null=True, verbose_name="No Transaksi")
    nama_depan = models.CharField(
        max_length=200, blank=False, null=True, verbose_name="Nama Depan")
    nama_belakang = models.CharField(
        max_length=200, blank=False, null=True, verbose_name="Nama Belakang")
    alamat = models.TextField(
        max_length=200, blank=False, null=True, verbose_name="Alamat")
    provinsi = models.CharField(
        max_length=200, blank=False, null=True, verbose_name="Provinsi")
    kabupaten = models.CharField(
        max_length=200, blank=False, null=True, verbose_name="Kabupaten")
    kecamatan = models.CharField(
        max_length=200, blank=False, null=True, verbose_name="Kecamatan")
    kode_post = models.CharField(
        max_length=200, blank=False, null=True, verbose_name="Kode Pos")
    email = models.CharField(max_length=200, blank=False,
                             null=True, verbose_name="Email")
    whatsapp = models.CharField(
        max_length=200, blank=False, null=True, verbose_name="No WhatsApp")
    total_transaksi = models.BigIntegerField(
        blank=True, null=True, verbose_name="Total Transaksi")
    status = models.CharField(max_length=200, default="Baru",
                              blank=True, null=True, choices=Status, verbose_name="Status")
    date_created = models.DateTimeField(
        auto_now_add=True, null=True, blank=True, verbose_name="Tanggal Dibuat")
    tanggal_kirim = models.DateTimeField(
        auto_now_add=False, null=True, blank=False, verbose_name="Tanggal Kirim")

    class Meta:
        verbose_name_plural = "Transaksi"


class DetailTransaksi(models.Model):
    no_transaksi = models.CharField(
        max_length=200, blank=False, null=True, verbose_name="No Transaksi")
    produk = models.ForeignKey(Produk, null=True, on_delete=models.SET_NULL)
    jumlah = models.IntegerField(blank=True, null=True, verbose_name="Jumlah")

    class Meta:
        verbose_name_plural = "Detail Transaksi"
