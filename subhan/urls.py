from django.urls import path
from .import views
urlpatterns = [
    path('kontak', views.KontakView.as_view(), name='kontak'),
    path('checkout', views.CheckoutView.as_view(), name='checkout'),
    path('produk', views.ProdukView.as_view(), name='produk'),
    path('', views.beranda, name='beranda'),
    path('tentang-kami', views.profil, name='profil'),
    path('<slug:slug>', views.kategori, name='kategori'),
    path('<slug:kategori_slug>/<slug:slug>',
         views.single_produk, name='single_produk'),
]
