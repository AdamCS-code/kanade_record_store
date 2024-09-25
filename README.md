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

<details>
<summary> <b> Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django </b> </summary>


## Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`
`HttpResponseRedirect` adalah *class* dari modul django.http yang mengembalikan respons pengalihan HTTP dengan kode status 302 (Found). Kode status ini menunjukkan bahwa pengguna atau klien akan dialihkan ke URL baru. *class* ini menerima parameter berupa URL tujuan yang spesifik dan sangat berguna jika kita ingin mengarahkan pengguna ke URL statis atau memerlukan logika pengalihan yang lebih kompleks.

Sementara itu, `redirect()` adalah fungsi dari modul django.shortcuts yang memberikan cara yang lebih sederhana dan fleksibel untuk melakukan pengalihan. Parameter yang diterima bisa berupa string URL, nama view, atau objek model, yang kemudian dikonversi oleh Django menjadi URL.

Perbedaan utama antara `HttpResponseRedirect` dan redirect terletak pada jenis parameter yang diterima. `HttpResponseRedirect` hanya menerima URL yang spesifik, sementara redirect lebih fleksibel karena dapat menerima URL, nama view, atau objek model yang akan secara otomatis dikonversi menjadi URL tujuan.

## Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut?
Authentication adalah proses untuk memastikan identitas pengguna. Misalnya, dalam kanade record store, Hanya pengguna yang memasukan username dan password yang sesuai memiliki akses pada akun yang berisi data - data entry. 

Sementara itu, authorization adalah proses untuk memastikan hak akses yang sesuai pada pengguna yang telah diauthentication. Jadi, pengguna yang telah login, hanya bisa mendapat akses akun yang bersangkutan. Hal ini mencegah pihak yang tidak bersangkutan dengan data yang kita miliki, tidak dapat melakukan modifikasi terhadap data tersebut.

Secara umum, ketika pengguna ingin login pada suatu aplikasi. Pengguna diminta untuk memasukan username dan password. Pada tahap ini, pengguna akan diauthentication. Pengguna tidak akan mendapat akses terhadap akun apabila memberikan username dan password yang salah. Pengguna yang telah masuk pun hanya mendapat akses modifikasi pada akun bersangkutan.

Django sendiri memudahkan authentication dan authorization dengan menyediakan fungsi dan class bawaan. Sistem ini menyediakan model untuk user dan group. Kemudian, ada juga views untuk login dan registrasi. Modul yang digunakan sendiri adalah `django.contrib.auth`. Lebih spesifik lagi terdapat fungsi `authenticate` yang menerima 3 argumen, yaitu request, username, password. Fungsi tersebut mengembalikan user jika argumen yang diberikan benar. Sementara itu, django juga menyediakan fitur authorization berupa penggunaan middleware untuk mengatur user sessionsd dan permissions.

## Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

Ketika ada pengguna yang telah login dan agar tetap login. Django menyediakan frameword session untuk menyimpan data user yang sedang login di server. Setiap user yang berhasil login akan diberikan cookie yang berisi SessionID, last login, atau csrf token. Kemudian, apabila pengguna logout, django akan menghapus session. sehingga, ketika memasuki website, pengguna perlu login ulang.

Beberapa fungsi lain dari cookies meliputi:

1. Menyimpan preferensi pengguna selama menjelajahi situs web, seperti pengaturan antarmuka atau bahasa.
2. Melacak aktivitas pengguna di situs untuk mempersonalisasi konten atau iklan yang ditampilkan, misalnya konten media sosial atau iklan yang relevan dengan minat pengguna.
3. Menganalisis perilaku pengguna di situs web, seperti minat atau durasi kunjungan, guna meningkatkan kualitas situs.

Pada sisi keamanan, Tidak semua cookie aman bagi pengguna. Misalnya, cookie yang menyimpan informasi penting seperti token autentikasi dapat diakses oleh JavaScript di situs web, atau cookie yang disetel oleh pihak ketiga. Cookie yang tidak dilindungi rentan terkena serangan Cross-Site Scripting (XSS). Untuk mitigasi masalah ini, django menyediakan beberapa fitur. Secure mengirim cookie hanya melalui HTTPS reques dan HttpOnly yang mencegah cookie diakses melalui JavaScript.

## Jelaskan cara kerja penghubungan model Product dengan User!
Model Item sendiri dihubungkan dengan model User melalui ForeignKey. ForeignKey menghubungkan setiap pengguna dengan Item yang dibuat oleh pengguna tersebut.

Implementasi dalam project:
```python
...
class Item(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=500)
...
```
Pengguna yang telah login, dapat menambah entri Item. Dimana setiap entri yang dibuat tersebut diasoasiasikan melalui ForeignKey

## Implementasi Checklist

### 1. Membuat fungsi register
Pada `/main/views.py` saya menambahkan fungsi register. 
```
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```
### 2. Membuat tampilan register
Saya membuat tampilan untuk registrasi pengguna dengan membuat `register.html` di `/main/template`
```
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}

<div class="login">
  <h1>Register</h1>

  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input type="submit" name="submit" value="Daftar" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
</div>

{% endblock content %}
```
### 3. Membuat fungsi login
Saya membuat fungsi login agar pengguna yang telah registrasi bisa menggunakan web. Pada `/main/views.py` saya menambahkan:
```
...
def login_user(request):
   if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
...
```
### 4. Membuat tampilan login
Saya membuat file html baru bernama `login.html` pada `/main/templates`. Berikut ini implementasi tampilan ketika pengguna akan login pada web.
```
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} Don't have an account yet?
  <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}
```
### 5. Membuat fungsi logout
Fungsi ini ditambahkan pada `views.py` agar pengguna yang sedang login bisa logout.
```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
### 6. Membuat tombol logout
Membuat tombol logout pada `main.html` agar pengguna bisa logout dari session sekarang.
```
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>
```
### 7. Routing setiap fungsionalitas
Agar setiap fungsionalitas bisa diakses melalui URL. Saya mengubah `urls.py` menjadi
```
from django.urls import path
from main.views import show_main, create_item_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register
from main.views import login_user
from main.views import logout_user

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item-entry', create_item_entry, name='create_item_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
```
### 8. Menghubungkan product dan user
Pada models.py saya menambahkan field baru, yaitu user. Sehingga, setiap user yang telah registrasi dapat melihat produk yang telah ia buat. Berikut ini implementasi yang saya lakukan.
```
from django.db import models
import uuid 

class Product(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=500)
```
### 9. Menampilkan detail pengguna yang sedang login
Pada main url, tampilkan detail pengguna seperti username dan last login. Informasi last_login diambil dari cookie browser user. 
```
def login_user(request):
   if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)
    context = {
        'name': request.user.username,
        'class': 'PBP F',
        'npm': '2306227160',
        'items': items,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "main.html", context)
```
### 10. Fitur Cookie
Data - data terkait seperti session id dan last login ditambahkan melalui fungsi `login_user`
```
def login_user(request):
   if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
```
</details>
