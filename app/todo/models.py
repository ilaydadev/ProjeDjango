from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import User
from django.contrib import admin

class Todo(models.Model):
    # Durum seçenekleri
    STATUS_CHOICES = [
        ('pending', 'Bekliyor'),
        ('completed', 'Tamamlandı'),
    ]
    # Öncelik seviyeleri
    PRIORITY_CHOICES = [
        ('low', 'Düşük'),
        ('medium', 'Orta'),
        ('high', 'Yüksek'),
    ] 
    # user tanımlaması
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Temel bilgiler
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    # Durum ve öncelik
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    # Tarihler
    created_at = models.DateTimeField(auto_now_add=True) # Sadece ilk oluşturma sırasında 
    due_date = models.DateField(null=True, blank=True) # Son tarih bitiş gibi

    def __str__(self):
        return f"{self.user.username} - {self.title}"
    class Meta:
        ordering = ['-created_at'] # Yeni önceliği belirler zamana göre işimizi kolaylaştırı.
# Admin paneli için
admin.site.register(Todo)
=======

# Create your models here.
>>>>>>> 053c74df2c30cc2feccea9dd9c2f9dffaed6b0ae
