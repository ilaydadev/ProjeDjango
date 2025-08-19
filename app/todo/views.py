from django.shortcuts import render
from django.http import HttpResponse


from django.shortcuts import render
from django.http import HttpResponse


data = {
    'pazartesi': {
        'gun_adi': 'Pazartesi',
        'tarih': '19.08.2024',
        'gorevler': [
            {
                'id': 1,
                'saat': '09:00',
                'baslik': 'Güne Başlangıç',
                'aciklama': 'Kahvaltı yapıp güne başlamak',
                'kategori': 'Günlük Rutin',
                'oncelik': 'yüksek',
                'durum': 'tamamlanmadı',
                'tahmini_sure': '30 dakika'
            },
            {
                'id': 2,
                'saat': '10:00',
                'baslik': 'E-posta Kontrolü',
                'aciklama': 'Gelen e-postaları kontrol et ve cevapla',
                'kategori': 'İş',
                'oncelik': 'orta',
                'durum': 'tamamlandı',
                'tahmini_sure': '45 dakika'
            },
            {
                'id': 3,
                'saat': '14:00',
                'baslik': 'Proje Toplantısı',
                'aciklama': 'Django projesi hakkında ekip toplantısı',
                'kategori': 'İş',
                'oncelik': 'yüksek',
                'durum': 'tamamlanmadı',
                'tahmini_sure': '90 dakika'
            }
        ]
    },
    'sali': {
        'gun_adi': 'Salı',
        'tarih': '20.08.2024',
        'gorevler': [
            {
                'id': 4,
                'saat': '08:30',
                'baslik': 'Spor Salonu',
                'aciklama': 'Haftalık fitness rutini',
                'kategori': 'Sağlık',
                'oncelik': 'yüksek',
                'durum': 'tamamlanmadı',
                'tahmini_sure': '60 dakika'
            },
            {
                'id': 5,
                'saat': '19:00',
                'baslik': 'Akşam Yemeği',
                'aciklama': 'Aile ile birlikte yemek',
                'kategori': 'Kişisel',
                'oncelik': 'orta',
                'durum': 'tamamlanmadı',
                'tahmini_sure': '45 dakika'
            }
        ]
    },
    'carsamba': {
        'gun_adi': 'Çarşamba',
        'tarih': '21.08.2024',
        'gorevler': [
            {
                'id': 6,
                'saat': '11:00',
                'baslik': 'Django Kodlama',
                'aciklama': 'Todo uygulaması geliştirme',
                'kategori': 'Programlama',
                'oncelik': 'yüksek',
                'durum': 'devam ediyor',
                'tahmini_sure': '120 dakika'
            },
            {
                'id': 7,
                'saat': '16:00',
                'baslik': 'Kitap Okuma',
                'aciklama': 'Python öğrenme kitabı',
                'kategori': 'Eğitim',
                'oncelik': 'orta',
                'durum': 'tamamlanmadı',
                'tahmini_sure': '60 dakika'
            }
        ]
    },
    'persembe': {
        'gun_adi': 'Perşembe',
        'tarih': '22.08.2024',
        'gorevler': [
            {
                'id': 8,
                'saat': '09:30',
                'baslik': 'Kod İnceleme',
                'aciklama': 'Önceki günün kodlarını gözden geçir',
                'kategori': 'Programlama',
                'oncelik': 'orta',
                'durum': 'tamamlanmadı',
                'tahmini_sure': '45 dakika'
            },
            {
                'id': 9,
                'saat': '21:00',
                'baslik': 'Yeni Özellik Kodlama',
                'aciklama': 'Todo uygulamasına yeni özellikler ekle',
                'kategori': 'Programlama',
                'oncelik': 'yüksek',
                'durum': 'tamamlanmadı',
                'tahmini_sure': '90 dakika'
            }
        ]
    },
    'cuma': {
        'gun_adi': 'Cuma',
        'tarih': '23.08.2024',
        'gorevler': [
            {
                'id': 10,
                'saat': '10:00',
                'baslik': 'Haftalık Değerlendirme',
                'aciklama': 'Bu haftaki işleri gözden geçir',
                'kategori': 'Planlama',
                'oncelik': 'orta',
                'durum': 'tamamlanmadı',
                'tahmini_sure': '30 dakika'
            },
            {
                'id': 11,
                'saat': '15:00',
                'baslik': 'Arkadaşlarla Buluşma',
                'aciklama': 'Hafta sonu planları yapmak',
                'kategori': 'Sosyal',
                'oncelik': 'düşük',
                'durum': 'tamamlanmadı',
                'tahmini_sure': '120 dakika'
            }
        ]
    }
}
def todo_list(request, id):
    # ID'ye göre spesifik görev bulma
    for gun_key, gun_data in data.items():
        for gorev in gun_data.get('gorevler', []):
            if gorev['id'] == id:
                context = {
                    'gorev': gorev,
                    'gun': gun_data['gun_adi'],
                    'tarih': gun_data['tarih'],
                    'id': id
                }
                return render(request, 'todo/todo_list.html', context)
    
    # Görev bulunamazsa
    return render(request, 'todo/todo_list.html', {
        'hata': 'Görev bulunamadı',
        'id': id
    })

def login(request):
    return render(request, 'todo/login.html')

def register(request):
    return render(request, 'todo/register.html')

def home(request):
    # Ana sayfada günlerin özetini göster
    gun_ozeti = {}
    for gun_key, gun_data in data.items():
        toplam_gorev = len(gun_data.get('gorevler', []))
        tamamlanan = len([g for g in gun_data.get('gorevler', []) if g['durum'] == 'tamamlandı'])
        gun_ozeti[gun_key] = {
            'gun_adi': gun_data['gun_adi'],
            'tarih': gun_data['tarih'],
            'toplam_gorev': toplam_gorev,
            'tamamlanan': tamamlanan,
            'kalan': toplam_gorev - tamamlanan
        }
    
    context = {'gun_ozeti': gun_ozeti}
    return render(request, 'todo/home.html', context)

def get_todo_list_day(request, day):
    try:
        gun_data = data[day.lower()]
        context = {
            'gun_data': gun_data,
            'gun': day.lower()
        }
        return render(request, 'todo/gunluk_todo.html', context)
    except KeyError:
        return HttpResponse("Geçersiz gün. Lütfen geçerli bir gün adı girin (pazartesi, sali, vs.)")

def get_all_todos(request):
    context = {'data': data}
    return render(request, 'todo/tum_gorevler.html', context)
def get_todo_by_category(request, kategori):
    kategorili_gorevler = []
    for gun_key, gun_data in data.items():
        for gorev in gun_data.get('gorevler', []):
            if gorev['kategori'].lower() == kategori.lower():
                gorev['gun'] = gun_data['gun_adi']
                kategorili_gorevler.append(gorev)
    
    context = {
        'gorevler': kategorili_gorevler,
        'kategori': kategori
    }
    return render(request, 'todo/kategori_gorevler.html', context)