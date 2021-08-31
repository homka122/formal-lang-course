[![Check code style](https://github.com/JetBrains-Research/formal-lang-course/actions/workflows/code_style.yml/badge.svg)](https://github.com/JetBrains-Research/formal-lang-course/actions/workflows/code_style.yml)
[![Code style](https://img.shields.io/badge/Code%20style-black-000000.svg)](https://github.com/psf/black)
---
# Formal Language Course

Курс по формальным языкам: шаблон структуры репозитория для выполнения домашних работ,
а также материалы курса и другая сопутствующая информация.

Актуальное:
- [Таблица с текущими результатами](https://docs.google.com/spreadsheets/d/18DhYG5CuOrN4A5b5N7-mEDfDkc-7BuXF3Qsu6HD-lks/edit?usp=sharing)
- [Стиль кода как референс](https://www.python.org/dev/peps/pep-0008/)

Технологии:
- python 3.8+
- pytest для unit тестирования
- GitHub Actions для CI
- Google Colab для постановки и оформления экспериментов
- Сторонние пакеты из `requirements.txt` файла
- Английский язык для документации или самодокументирующийся код

## Работа с проектом

- Для выполнения домашних практических работ необходимо сделать `fork` этого репозитория к себе в github.
- Ссылка на свой `fork` репозитория размещается в [таблице](https://docs.google.com/spreadsheets/d/18DhYG5CuOrN4A5b5N7-mEDfDkc-7BuXF3Qsu6HD-lks/edit?usp=sharing) курса с результатами.
- В свой репозиторий необходимо добавить проверяющих с `root` правами на чтение, редактирование и проверку `pull-request`'ов.
- Каждое отдельное домашнее задание выполняется в отдельной ветке. Ветка должна иметь осмысленное консистентное название.
- Проверка заданий осуществляется в `pull-request`.
- Когда проверка будет пройдена, и задание зачтено, его необходимо `merge` в свой `master`.
- Результаты выполненных заданий могут повторно использоваться в последующих свои домашних работах.

## Pull-request

- При выполнении домашнего задания в новой ветке необходимо открыть соответствующий `pull-request`.
- `Pull-request` снабдить понятным названием и описанием с соответствующими пунктами прогресса.
- Как только вы считаете, что задание выполнено, вы можете запросить `review` у проверяющего.
- Если это происходит в течение 4 дней до мягкого дедлайна, то вам гарантирована проверка, чтобы вы могли исправить замечания, и получить полный бал.
- Если это происходит после мягкого дедлайна, но до жесткого дедлайна, задание будет проверено, но нет гарантий, что вы успеете его исправить.  

## Код

- Исходный код практических задач по программированию размещаем в папке `python`.
- Файлам и модулям даем осмысленные имена, в соответствии с официально принятым стилем.
- Структурируем код, используем как классы, так и отдельно оформленные методы. Понятность кода => высокая скорость проверок.

## Тесты

- Тесты для домашних заданий размещаются в папке `test`.
- Формат именования файлов с тестами `test_[латинские буквы и цифры].py`.
- Для запуска тестов необходимо из корня проекта выполнить следующую команду:

```shell
$ python ./script/run.py
```

## Эксперименты

- Для выполнения экспериментов потребуется не только код, но окружение и некоторая его настройка.
- В качестве окружения используем только `Google Colab` ноутбуки. Для его создания требуется только учетная запись google.
- Создаем ноутбук, ссылка на ноутбук также размещается в [таблице](https://docs.google.com/spreadsheets/d/18DhYG5CuOrN4A5b5N7-mEDfDkc-7BuXF3Qsu6HD-lks/edit?usp=sharing) курса.
- В ноутбуке выполняется вся настройка, пишется код для экспериментов, подготовки отчетов и графиков.

## Структура репозитория

```
.
├── .github - файлы для настройки CI и проверок
├── docs - текстовые документы и материалы по курсу
├── python - исходный код домашних работ
├── script - вспомогательные скрипты для автоматизации разработки
├── test - директория для unit-тестов домашних работ
├── README.md - основная информация о проекте
└── requirements.txt - зависимости для настройки репозитория 
```

## Контакты

- Семен Григорьев [@gsvgit](https://github.com/gsvgit)
- Егор Орачев [@EgorOrachyov](https://github.com/EgorOrachyov)
- Вадим Абзалов [@vdshk](https://github.com/vdshk)