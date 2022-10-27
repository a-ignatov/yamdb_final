# Технологии проекта
![Yamdb workflow](https://github.com/a-ignatov/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646??style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![GitHub](https://img.shields.io/badge/-GitHub-464646??style=flat-square&logo=GitHub)](https://github.com/)
[![docker](https://img.shields.io/badge/-Docker-464646??style=flat-square&logo=docker)](https://www.docker.com/)
[![NGINX](https://img.shields.io/badge/-NGINX-464646??style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![Python](https://img.shields.io/badge/-Python-464646??style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646??style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646??style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)


# Проект YaMDb
Проект YaMDb собирает отзывы (Review) пользователей на произведения (Titles). Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Список категорий (Category) может быть расширен администратором (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).
Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
В каждой категории есть произведения: книги, фильмы или музыка. Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Насекомые» и вторая сюита Баха.
Произведению может быть присвоен жанр (Genre) из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). Новые жанры может создавать только администратор.
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы (Review) и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.

## Установка
Склонируйте репозиторий.
cd api_yamdb
Cоздать и активировать виртуальное окружение: python -m venv venv
source venv/scripts/activate
python -m pip install --upgrade pip
Установить зависимости из файла requirements.txt: pip install -r requirements.txt
Выполнить миграции: python manage.py migrate
Запустить проект: python manage.py runserver
Проект запущен и доступен по адресу [localhost:8000](http://localhost:8000/).

## Ресурсы API YaMDb

**AUTH**: 
Авторизация
```
http://127.0.0.1:8000/api/v1/auth/signup/
```
### Алгоритм регистрации пользователей
Пользователь отправляет POST-запрос на добавление нового пользователя с параметрами email и username на эндпоинт /api/v1/auth/signup/.
YaMDB отправляет письмо с кодом подтверждения (confirmation_code) на адрес email.
Пользователь отправляет POST-запрос с параметрами username и confirmation_code на эндпоинт /api/v1/auth/token/, в ответе на запрос ему приходит token . 

**USERS**: 
Пользователи
```
http://127.0.0.1:8000/api/v1/users/
```
 Создание пользователя и получение информации о всех пользователях. Доступны запросы **Get, Post**

**TITLES**: 
Произведения, к которым пишут отзывы (определённый фильм, книга или песенка).
```
http://127.0.0.1:8000/api/v1/titles/
```
Работа со статьями , доступны запросы **Get, Post, Patch и Del**

**CATEGORIES**: 
Категории (типы) произведений ("Фильмы", "Книги", "Музыка").
```
http://127.0.0.1:8000/api/v1/categories/
```
Работа с категориями, доступны запросы **Get, Post и Del**

**GENRES**: 
Жанры произведений. Одно произведение может быть привязано к нескольким жанрам.
```
http://127.0.0.1:8000/api/v1/genres/
```
Работа с жанрами, доступны запросы **Get, Post и Del**

**REVIEWS**: 
Отзывы на произведения. Отзыв привязан к определённому произведению.
```
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/
```
Работа с отзывами , доступны запросы **Get, Post, Patch и Del**

**COMMENTS**: 
Комментарии к отзывам. Комментарий привязан к определённому отзыву.
```
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/
```
Работа с комментариями , доступны запросы **Get, Post, Patch и Del**


