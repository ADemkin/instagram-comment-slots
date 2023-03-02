===============================
Instagram comments slot machine
===============================

Описание
========

Этот репозиторий облегачет проведение розыгрышей через инстаграм.
Вы выбираете пост, а скрипт выберет один из комментариев.


Установка
=========

Для установки нужен `poetry`::

 $ poetry install

Запуск
======

Перед первым запуском необходимо создать файл `.env` и положить в него
аккаунт и пароль::

 INSTAGRAM_ACCOUNT=my-account
 INSTAGRAM_PASSWORD=my-password


Для запуска через терминал::

 $ poetry run python cli.py [url-to-instagram-post]

Для запуска веб сервера с формой::

 $ poetry run python server.py

Сервер будет запущен по адресу `0.0.0.0:7777`

Пример
======

Вот пример работы скрипты через терминал::

 $ poetry run python cli.py https://www.instagram.com/p/CgMyENGM64m/
 account: moscowliuda
 name: Людмила Мельникова Мск🛫Кгд🛫EVN🛫TBS
 text: @surdologoped_zelenograd спасибо, милая. Мне тоже так понравилась)
