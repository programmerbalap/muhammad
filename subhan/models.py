from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from django_resized import ResizedImageField


# Create your models here.


class Kategori(models.Model):
    nama = models.CharField(max_length=200, blank=True, null=True)
    aktif = models.BooleanField(default=True)
    banner_satu = ResizedImageField(size=[575, 200], quality=80, crop=['middle', 'center'],
                                    upload_to='gambar/banner', blank=True, null=True, verbose_name="Gambar (575 x 200 pixel)")
    banner_dua = models.ImageField(
        upload_to='gambar/banner', blank=False, null=True, verbose_name="Gambar (575 x 200 pixel)")
    slug = models.SlugField(max_length=200, null=True, blank=True, unique=True)

    class Meta:
        verbose_name_plural = "Kategori"

    # def save(self, *args, **kwargs):  # new
    #     if not self.slug:
    #         self.slug = slugify(self.nama)
    #         return super().save(*args, **kwargs)

    # def __str__(self):
    #     return f"Kategori: {self.nama}, aktif: {self.aktif}"

    def __str__(self):
        return '%s, %s' % (self.nama, self.aktif)

    @property
    def get_produk(self):
        return Produk.objects.filter(kategori__nama=self.nama)


class Produk(models.Model):
    KETERANGAN = (
        ('Baru', 'Baru'),
        ('Lama', 'Lama'),
    )
    kategori = models.ForeignKey(Kategori, null=True, blank=True,
                                 related_name="produks", on_delete=models.SET_NULL)
    nama_produk = models.CharField(max_length=200, blank=True, null=True)
    gambar_satu = models.ImageField(
        upload_to='gambar/banner', blank=False, null=True, verbose_name="Gambar 1 (270 x 250pixel)")
    gambar_dua = models.ImageField(
        upload_to='gambar/banner', blank=False, null=True,  verbose_name="Gambar 2 (270 x 250pixel)")
    gambar_tiga = models.ImageField(
        upload_to='gambar/banner', blank=False, null=True,  verbose_name="Gambar 3 (270 x 250pixel)")
    gambar_empat = models.ImageField(
        upload_to='gambar/banner', blank=False, null=True,  verbose_name="Gambar 4 (270 x 250pixel)")
    gambar_lima = models.ImageField(
        upload_to='gambar/banner', blank=False, null=True,  verbose_name="Gambar 5 (270 x 250pixel)")
    slug = models.SlugField(max_length=200, unique=True,  verbose_name="Slug")
    # keterangan = models.TextField(max_length=200, blank=True, null=True,  verbose_name="Keterangan")
    keterangan = RichTextField(blank=True, null=True)
    harga = models.PositiveIntegerField(
        blank=True, null=True,  verbose_name="Harga Rp.")
    no_whats_app = models.PositiveBigIntegerField(
        blank=True, null=True,  verbose_name="No WhatsApp")
    tanggal_upload = models.DateTimeField(
        auto_now_add=True, null=True,  verbose_name="Tanggal Upload")
    diskon = models.IntegerField(
        default=0, blank=True, null=True,  verbose_name="Diskon %")
    dibeli = models.IntegerField(
        default=0, blank=True, null=True,  verbose_name="Dibeli")
    keterangan_barang = models.CharField(
        max_length=200, null=True, choices=KETERANGAN,  verbose_name="Ket. Barang")

    class Meta:
        verbose_name_plural = "Produk"

    @property
    def setelah_diskon(self):
        if self.diskon == 0:
            nilai_diskon = self.harga
        else:
            jml = self.diskon / 100
            nilai_diskon = self.harga - (jml * self.harga)
        return nilai_diskon

    def __str__(self):
        return self.nama_produk


class Slide(models.Model):
    teks_satu = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="Teks Satu")
    teks_dua = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="Teks Dua")
    teks_tiga = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="Teks Tiga")
    gambar_slide = models.ImageField(
        upload_to='gambar/slide', blank=False, null=True, verbose_name="Gambar Slide (270 x 250pixel)")
    aktif = models.BooleanField(default=True, verbose_name="Status")

    class Meta:
        verbose_name_plural = "Slide"


class Kontak(models.Model):
    nama = models.CharField(max_length=200, blank=False,
                            null=True, verbose_name="Nama")
    no_whats_app = models.PositiveBigIntegerField(
        blank=True, null=True, verbose_name="No WhatsApp")
    email = models.EmailField(
        max_length=200, blank=False, null=True, verbose_name="Email")
    subject = models.CharField(
        max_length=200, blank=False, null=True, verbose_name="Subject")
    isi = models.TextField(max_length=200, blank=False,
                           null=True, verbose_name="Isi")

    class Meta:
        verbose_name_plural = "Kontak"


class Profil(models.Model):
    nama = models.CharField(max_length=200, blank=False,
                            null=True, verbose_name="Nama")
    # keterangan = models.TextField(max_length=200, blank=True, null=True, verbose_name="Keterangan")
    keterangan = RichTextField(blank=True, null=True)
    gambar = models.ImageField(upload_to='gambar/profil', blank=False,
                               null=True, verbose_name="Gambar (1920 x 1200 pixel)")
    tanggal_upload = models.DateTimeField(
        auto_now_add=True, null=True, verbose_name="Tanggal Upload")

    class Meta:
        verbose_name_plural = "Profil"


class Statis(models.Model):
    alamat_kami = models.TextField(
        max_length=200, blank=False, null=True, verbose_name="Alamat")
    telpon = models.CharField(
        max_length=200, blank=False, null=True, verbose_name="No Telepon")
    email = models.EmailField(
        max_length=200, blank=False, null=True, verbose_name="Email")

    class Meta:
        verbose_name_plural = "Statis"


class ChatID(models.Model):
    chatid = models.CharField(max_length=200, blank=False, null=True)
    nama = models.CharField(max_length=200, blank=False, null=True)
    aktif = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Data Chat ID"
