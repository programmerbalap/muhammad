from django.contrib import admin
from .models import Kategori, Produk, Slide, Kontak, Profil, Statis, ChatID


class KategoriAdmin(admin.ModelAdmin):
    list_display = ("nama", "aktif", "banner_satu", "banner_dua",)
    prepopulated_fields = {"slug": ("nama",)}


class DataProdukAdmin(admin.ModelAdmin):
    list_display = ("nama_produk", "gambar_satu", "harga", "no_whats_app",)
    prepopulated_fields = {"slug": ("nama_produk",)}


admin.site.register(Produk, DataProdukAdmin)
admin.site.register(Kategori, KategoriAdmin)
admin.site.register(Slide)
admin.site.register(Kontak)
admin.site.register(Profil)
admin.site.register(Statis)
admin.site.register(ChatID)
