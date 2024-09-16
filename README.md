# Kanade Record Store

> **Kanade Record Store** adalah aplikasi penjualan dan pembelian rilisan fisik sepert vinyl, tape, dll untuk kawula muda yang kalcer abiez.

## 💿🥁🎹**Link**🎸🎻🎼
[Kunjungin laman Kanade Record Store](http://adam-caldipawell-kanaderecordstore.pbp.cs.ui.ac.id/)

<details>
<summary> <b> Tugas 2: Implementasi Model-View-Template (MVT) pada Django </b> </summary>

## Langkah langkah implementasi Kanade Record Store

### 1. Membuat Directory Baru dan Menginisialisasi Git
1. Buat directory baru bernama `kanade-record-store`.
2. Inisialisasi repositori Git dan hubungkan ke GitHub:
    ```bash
    git init
    git remote add origin <URL>
    git add .
    git commit -m "Initial commit"
    git push origin master
    ```

### 2. Membuat Virtual Environment
1. Jalankan perintah berikut untuk membuat virtual environment:
    ```bash
    python -m venv env
    ```
2. Aktifkan virtual environment:
    - **Linux/macOS**:
        ```bash
        source env/bin/activate
        ```
    - **Windows**:
        ```bash
        env\Scripts\activate
        ```

### 3. Membuat dan Menginstall Requirements
1. Buat file `requirements.txt` yang berisi daftar package yang diperlukan.
2. Jalankan perintah berikut untuk menginstal package:
    ```bash
    pip install -r requirements.txt
    ```

### 4. Membuat Proyek Django
1. Buat proyek Django baru dengan nama `kanade_record_store`:
    ```bash
    django-admin startproject kanade_record_store
    ```
2. Buat aplikasi baru dengan nama `main`:
    ```bash
    django-admin startapp main
    ```

### 5. Mengupdate `settings.py`
1. Tambahkan aplikasi `main` ke dalam list `INSTALLED_APPS` di `settings.py` agar aplikasi tersebut terdaftar di proyek.
2. Tambahkan `"localhost"`, `"127.0.0.1"` ke dalam list `ALLOWED_HOSTS` untuk mengakses aplikasi secara lokal saat pengembangan.

### 6. Membuat View dan Template
1. Tambahkan kode berikut pada `views.py`:
    ```python
    from django.shortcuts import render

    def show_main(request):
        context = {
            'nama': 'Adam Caldipawell Sembiring',
            'class': 'PBP F'
        }
        return render(request, "main.html", context)
    ```
2. Di `urls.py`, tambahkan `path('', include('main.urls'))` pada `urlpatterns` agar URL aplikasi `main` bisa diakses.
3. Di folder `main`, buat folder bernama `templates` dan buat file `main.html` yang menampilkan nama e-commerce, nama, dan kelas.

### 7. Membuat Model Produk
1. Di `models.py`, buat model produk dengan atribut berikut:
    - `name`: CharField
    - `price`: IntegerField
    - `description`: TextField
      
### 8. Melakukan migration pada model
1. Pindah ke directory utama
2. Jalankan migration pada terminal:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
### 9. Deploy ke PWS (Pacil Web Service)
1. Buat project baru di PWS dengan nama `kanaderecordstore` dan simpan credential information.
2. Di `settings.py`, tambahkan URL `adam-caldipawell-kanaderecordstore.pbp.cs.ui.ac.id/` ke dalam list `ALLOWED_HOSTS`.
3. Simpan perubahan dengan menjalankan:
    ```bash
    git add .
    git commit -m "Deploy to PWS"
    git push origin master
    ```
4. Tambahkan remote PWS:
    ```bash
    git remote add pws http://pbp.cs.ui.ac.id/adam.caldipawell/kanaderecordstore
    git branch -M master
    git push pws master
    ```

### 10. Aplikasi Django Terdeploy
Aplikasi sekarang bisa diakses melalui URL:  
[http://adam-caldipawell-kanaderecordstore.pbp.cs.ui.ac.id/](http://adam-caldipawell-kanaderecordstore.pbp.cs.ui.ac.id/)

## Bagan Proses Request Client ke Web Aplikasi

Berikut adalah alur proses dari request client ke web aplikasi berbasis Django:

![alt text](image/image-1.png)

### Penjelasan
1. Ketika user mengirimkan HTTP request ke server PWS, request tersebut diteruskan ke WSGI server.
2. WSGI server meneruskan request tersebut ke Django.
3. `urls.py` mendeteksi URL request dan menghubungkannya dengan views yang sesuai.
4. `views.py` memproses request dan mengambil data dari `models.py`.
5. `views.py` kemudian mengirimkan response berupa template HTML (`main.html`) yang akan dikembalikan ke user sebagai response.

## Fungsi Git dalam Pengembangan Perangkat Lunak
Git berfungsi sebagai version control dalam pengembangan perangkat lunak. Dengan Git, kita dapat melacak setiap perubahan kode yang dilakukan, memudahkan proses kolaborasi, dan memungkinkan rollback ke versi sebelumnya jika terjadi kesalahan.

## Mengapa Django Digunakan sebagai Permulaan Pembelajaran?
Django menggunakan bahasa Python yang relatif mudah dipahami. Django menawarkan arsitektur MVT (Model, View, Template), yang memisahkan komponen UI (template), logika aplikasi (view), dan akses database (model), sehingga memudahkan pengembangan terstruktur. Django juga memudahkan pengembang untuk membangun aplikasi yang skalabel.

## Mengapa Model di Django Disebut sebagai ORM?
Django menggunakan ORM (Object-Relational Mapping), yang memodelkan data dari database relasional menjadi objek di Python. Ini memungkinkan pengembang untuk berinteraksi dengan database tanpa harus menulis query SQL secara eksplisit, melalui QuerySet API yang disediakan oleh Django.
</details>

<details>
<summary> <b> Tugas 3: Implementasi Form dan Data Delivery pada Django </b> </summary>
    
## Mengapa kita memerlukan *data delivery* dalam pengimplementasian sebuah platform?

Dalam pembuatan platform, tidak jarang ada kebutuhan untuk mengirim ataupun menerima data. Implementasi sebuah platform yang memiliki mekanisme *data delivery* dapat membuat sebuah platform lebih interaktif dan dinamis. 

## Mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

| Format       | XML                                                                 | JSON                                                                                     |
|--------------|---------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| Perbandingan | XML adalah bahasa mark up yang memiliki aturan dalam pendefinisian data. XML menggunakan tag yang memisahkan nama data dan nilai data. | JSON adalah format pertukaran data yang mudah dibaca oleh komputer dan manusia. JSON menyimpan data dengan pasangan string key dan value. JSON juga banyak didukung oleh bahasa pemrograman. |
| Sintaks      | `<tag>nilai</tag>`                                                  | `{nama: 'Adam'}`                                                                          |

Dalam konteks pemrograman platform web, JSON lebih baik dan lebih populer dibandingkan dengan XML dengan kelebihan berikut:

1. Sintaks JSON yang lebih ringkas, ringan, dan mudah untuk dibaca.
2. JSON mendukung berbagai tipe data, contohnya array.
3. JSON lebih cepat dibandingkan XML karena pada pemrograman web, JavaScript memiliki fungsi bawaan yang dapat parsing JSON menjadi JavaScript object.
4. JSON didukung oleh banyak bahasa pemrograman karena kemudahan yang diberikan.


## Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?

Validasi form model secara otomatis akan dilakukan oleh Django melalui pemanggilan fungsi `is_valid()' untuk memastikan kebenaran input yang diberikan.

##  Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

Cross-Site Request Forgery (csrf) adalah salah satu metode dalam penyerangan keamanan suatu website. Pada `tugas 3`, kita diminta untuk membuat suatu form yang kemudian dapat dikirimkan ke DJango (webserver) melalui request POST. Jika tidak ada `csrf_token` maka seorang attacker bisa saja melakukan request POST ini tanpa melalui website kanade record store. Saat seseorang ingin menambahkan object melalui form, Django akan mengirimkan `csrf_token` saat membuka laman `/create-item-entry` kemudian ketika form tersebut disubmit maka request POST + `csrf_token` akan dikirimkan ke Django kembali yang memastikan bahwa pengiriman data dilakukan di website kanade record store.

## Implementasi *data delivery*

### Implementasi skeleton sebagai kerangka views
1. Pertama saya membuat directory `templates` di `root directory`.
2. Membuat sebuah file html sebagai skeleton, `base.html` dengan kode berikut:
   ```html
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        {% block meta %} {% endblock meta %}
      </head>

      <body>
        {% block content %} {% endblock content %}
      </body>
    </html>
   ```
3. Pada `settings.py` di `kanade_record_store`. Pada variabel `TEMPLATES`. Ubah menjadi
   ```python
   TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
   ```
Langkah - langkah ini memberitahu Django untuk menggunakan base.html sebagai skeleton. Sehingga kedepannya yang perlu dilakukan untuk mengubah isi html adalah mengisi {% block         content %} <b> *isi disini* </b> {% endblock content %}. Sehingga tampilan untuk pengguna tetap dinamis dan minim redudansi.
### Menambahkan UUID sebagai id untuk object model
1. Pergi ke `./main` lalu ubah models.py menjadi:
   ```python
    import uuid

    class Item(models.Model):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        name = models.CharField(max_length=255)
        price = models.IntegerField(default=0)
        description = models.TextField(default="")
   ```
2. Migrasi model baru dengan menjalankan:
   ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
   ```
Pemberian ID dimaksudkan agar setiap object memiliki sebuah *identifier* yang berbeda - beda. Penggunaan UUID adalah salah satu upaya untuk mencegah serangan IDOR.

### Membuat form untuk menambahkan object 
1. Pada directory `main` saya menambahkan `forms.py`. Pembuatan `forms.py` dilakukan untuk membuat struktur *form* sederhana sesuai dengan `models.Item`:
   ```python
    from django.forms import ModelForm
    from main.models import Item
    
    class ItemEntryForm(ModelForm):
        class Meta:
            model = Item
            fields = ["name", "price", "description"]
   ```
   `model = Item` memberitahu ke Django bahwa gunakan Item sebagai model saat pengisian *form*
   `fields = ["name", "price", "description"]` mendefinisikan field yang akan diisi user. <b>ID digenerate secara otomatis oleh UUID</b>
2. Membuat template baru untuk tampilan dalam menambahkan item baru dengan nama `create_item.html` pada direktori `main/template`:
    ```html
    {% extends 'base.html' %} 
    {% block content %}
    <h1>Add New Item Entry</h1>
    
    <form method="POST">
      {% csrf_token %}
      <table>
        {{ form.as_table }}
        <tr>
          <td></td>
          <td>
            <input type="submit" value="Add Item" />
          </td>
        </tr>
      </table>
    </form>
    
    {% endblock %}
    ```
4. Pada berkas `views.py` di directory yang sama. Saya menambahkan sebuah fungsi `create_item_entry` untuk untuk menampilkan *form*:
   ```python
   ...
   from django.shortcuts import render, redirect #redirect untuk mengembalikan user ke halaman utama setelah pengisian *form*
   from main.forms import ItemEntryForm
   from main.models import Item
   
    def create_item_entry(request):
        form = ItemEntryForm(request.POST or None)
    
        if form.is_valid() and request.method == "POST":
            form.save()
            return redirect('main:show_main')
    
        context = {'form': form}
        return render(request, "create_item_entry.html", context)
   ```
   `form = MoodEntryForm(request.POST or None)` digunakan untuk membuat ItemEntryForm baru dengan memasukkan QueryDict berdasarkan input dari user pada request.POST.
   `form.is_valid()` digunakan untuk memvalidasi isi input dari form tersebut.
   `form.save()` digunakan untuk membuat dan menyimpan data dari form tersebut.
   `return redirect('main:show_main')` digunakan untuk melakukan redirect ke fungsi show_main pada views aplikasi main setelah data form berhasil disimpan.
5. Pada berkas yang sama, ubah fungsi `show_main`:
   ```python
   ...
   def show_main(request):
    items = Item.objects.all()
    context = {
        'name' : 'Adam Caldipawell Sembiring',
        'class' : 'PBP F',
        'items' : items,
    }
    return render(request, "main.html", context)
   ```
   Setiap item yang dibuat akan ditampilkan saat kembali ke halaman utama. Seluruh item diakses melalui `items = Item.objects.all()`.
6. Mengubah template untuk tampilan utama `main.html` pada direktori `main/template`:
```html
{% extends 'base.html' %}
{% block content %}
<h1>Kanade Record Store</h1>

<h5>Name:</h5>
<p>{{ name }}</p>

<h5>Class:</h5>
<p>{{ class }}</p>

{% if not items %}
<p>Belum ada data item pada Kanade Record Store.</p>
{% else %}
<table>
  <tr>
    <th>Name</th>
    <th>Price</th>
    <th>Description</th>
  </tr>

  {% comment %} Berikut cara memperlihatkan data mood di bawah baris ini 
  {% endcomment %} 
  {% for item in items %}
  <tr>
    <td>{{item.name}}</td>
    <td>{{item.price}}</td>
    <td>{{item.description}}</td>
  </tr>
  {% endfor %}
</table>
{% endif %}

<br />

<a href="{% url 'main:create_item_entry' %}">
  <button>Add New Item Entry</button>
</a>

{% endblock content %}
```
### Mengembalikan data dalam bentuk XML dan JSON
Untuk mengembalikan data dalam format XML dan JSON, Saya menggunakan `serializers` dan `HttpResponse`
```python
from django.http import HttpResponse
from django.core import serializers
...
```
<b>Mengembalikan Format XML</b>
```python
...
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
...
```
<b>Mengembalikan Format JSON</b>
```python
...
def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/xml")
...
```
### Mengembalikan data dalam bentuk XML dan JSON sesuai [id]
Untuk mengembalikan data sesuai dengan ID object tersebut maka:

<b>Mengembalikan Format XML by id</b>

```python
...
def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
...
```

<b>Mengembalikan Format JSON by id</b>

```python
...
def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
...
```
### Membuat routing URL untuk masing-masing views yang telah ditambahkan

```python
from django.urls import path
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id 

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),  
]
```

### Melakukan push ke github dan pws
```bash
git add .
git commit -m"tugas 3"
git push origin master
git push pws master
```
Sehingga aplikasi bisa dilihat di [website ini](http://adam-caldipawell-kanaderecordstore.pbp.cs.ui.ac.id/)

### Membuat *screenshot* menggunakan POSTMAN
1. HTML
![alt text](image/localhost:main.png)
2. XML
![alt text](image/localhost:xml.png)
3. JSON
![alt text](image/localhost:json.png)
4. XML by ID
![alt text](image/localhost:xml:[id].png)
5. JSON by ID
![alt text](image/localhost:json:[id].png)
source:
1. [Django DOCS](https://docs.djangoproject.com/)
2. [Slide Data Delivery](https://scele.cs.ui.ac.id/pluginfile.php/238122/mod_resource/content/1/04%20-%20Data%20Delivery.pdf)
3. [CSRF by computerphile](https://youtu.be/vRBihr41JTo?si=oXlMrDMj3HlvRsOU)
4. [Tutorial 2](https://pbp-fasilkom-ui.github.io/ganjil-2025/docs/tutorial-2)

</details>
