1. Stwórz katalog, a w nim uruchom środowisko wirtualne Pythona:
`python3 -m venv venv`
2. Aktywacja środowiska wirtualnego:
`source venv/bin/activate` 
3. Instalacja django:
`pip install django`
4. Stwórz projekt Django:
`django-admin startproject nazwa_projektu`
5. Przejdź do katalogu z projektem:
 `cd nazwa_katalogu`.
6. Stwórz aplikację:
`django-admin startapp nazwa_aplikacji`
7. Uruchomienie serwera by podejrzeć stronę:
`python manage.py runserver`
8. W settings.py dodaj `<nazwa_aplikacji>.apps.<Nazwa_aplikacji>Config` do sekcji INSTALLED_APPS.
9. Do pliku projekt/urls.py dodaj path dla pliku aplikacja/urls.py, który utworzysz w katalogu aplikacji.
10. Napisz klasę reprezentującą widok strony w pliku aplikacja/views.py.
11. Do katalogu z projektem dodaj katalog 'templates' z bazą dla stron html. Drugi katalog 'templates' dodaj do katalogu z aplikacją, a w nim będziesz dodawał szablony szczegółowe (np. home.html).
12. W settings.py, w 'TEMPLATES' dodaj informację o lokalizacji katalogu templates:
`'DIRS': [(os.path.join(BASE_DIR, 'templates')),],` (zaimportuj os).
13. Pliki statyczne: w głównym katalogu projektu stwórz folder 'static', a w settings.py dodaj formułę:
`STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]`
14. W plikach html używających statycznych elementów należy dodać:
`{% load static %}`, następnie, jako src adres pliku, np:
`src="{% static 'images/1.jpg' %}"`

Tworzenie superusera:
1. `python manage.py createsuperuser` (admin, admin)

Modele do bazy danych
1. W pliku models.py stwórz klasę z polami modelu.
2. `python manage.py makemigrations`
3. `python manage.py migrate`
4. W pliku admin.py zarejestruj model.

Wyświetlenie danych z bazy
1. W pliku views.py pobierz dane `models.TaskList.objects.all()`, 
a w pliku .html użyj pętli 'for' i tabeli z Bootstrapa by wyświetlić dane.

Dodawanie danych do bazy 
1. Do pliku .html dodaj formularz z Bootstrapa. Dodaj metodę POST i 'name' do znacznika
'form' oraz `{% csrf_token %}`.
2. Stwórz nowy plik w aplikacji - 'forms.py', w którym zaimportuj swój model
oraz forms z django. Stwórz klasę formularza (tu: TaskForm) rozszerzającą
forms.ModelForm, z polami formularza jako klasa Meta. Meta klasa jest brana
pod uwagę w czasie tworzenia obiektu tej klasy.
3. W pliku views.py zaimportuj klasę formularza, następnie w widoku z formularzem
(tu: home) w przypadku POST pobierz dane z formularza i zapisz w bazie danych.
Dodaj message w przypadku udanego zapisu.
4. W .html wypisz message

Edycja i Usuwanie obiektów z bazy - CRUD
1. W pliku urls.py dodaj 'path' do usuwania (delete) z `<task_id>`
2. W pliku views.py dodaj metodę delete_task, która pobierze `<task_id>` z url
i usunie task z tym id.
3. W pliku .html dodaj znacznik 'a' i w nim 'href' do url `delete/<task_id>` co pozwoli usuwać.

Edycja
1. Dodaj path do edycji w urls.py
2. We views.py dodaj metodę edit_task
3. Dodaj widok edit_task.html
4. Aby edytować done/not done postępuj jak wyżej.

Paginacja
1. W views.py import Pagination z django.core.paginator
2. W metodzie home dodaj kod definiujący paginację.
3. W html dodaj element paginujący z bootstrapa i połącz go z paginatorem z views.py

1. Aby zmienić kolor tła całej strony dodaj klasę bootstrapa z kolorem (np. bg-light) do znacznika 
'body' base.html.
2. Darmowe obrazki - unsplash

Autentykacja użytkowników
1. Stwórz nową aplikację (users_app)
    `django-admin startapp users_app`
2. Zarejestruj ją w settings.py i stwórz w niej plik urls.py z path dla 
'register'.
3. W users_app/views.py zaimportuj UserCreationForm z 'django.contrib.auth.forms' 
i stwórz widok dla register.
4. Przygotuj register.html w users_app/templates.
5. Użyj crispy by poprawić wygląd formularza rejestracji:
    `pip install crispy-bootstrap5`
6. Dodaj 'crispy_forms' i 'crispy_bootstrap5' do settings.py i INSTALLED_APPS.
7. Na końcu settings.py dodaj info o CRISPY_TEMPLATE_PACK i
CRISPY_ALLOWED_TEMPLATE_PACKS.
8. W register.html dodaj instrukcję
`{% load crispy_forms_tags %}` i 
`{{ register_form|crispy }}` '|' oznacza filtrowanie w Jinja.

'user1, password888'