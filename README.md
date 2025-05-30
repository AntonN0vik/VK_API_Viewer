# VK API Viewer

Консольное приложение на Python для просмотра информации о пользователях ВКонтакте через VK API.

## Возможности

-  **Поиск пользователей** - по ID или имени пользователя (screen_name)
-  **Информация о пользователе** - имя, фамилия, дата рождения, город, страна
-  **Список друзей** - просмотр друзей пользователя (до 15 отображается, общее количество указывается)
-  **Фотоальбомы** - просмотр списка альбомов с количеством фотографий

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/AntonN0vik/VK_API_Viewer.git
cd VK_API_Viewer
```

2. Установите зависимости:
```bash
pip install requests
```

## Использование

Запустите приложение:
```bash
python main.py
```

При первом запуске введите ваш VK API токен.

### Доступные команды:

- **[1] Показать меню команд** - отображение всех доступных команд
- **[2] Получить информацию о пользователе** - подробная информация о профиле
- **[3] Просмотреть список друзей** - список друзей пользователя
- **[4] Просмотреть фотоальбомы** - список альбомов с фотографиями
- **[0] Завершить работу программы** - выход из приложения

### Примеры использования:

1. **Просмотр своей информации**: оставьте поле ID пустым
![image](https://github.com/user-attachments/assets/bb808549-3702-4378-b6ec-6dea3b6c9899)

2. **Поиск по ID**: введите числовой ID пользователя (например: `123456789`)
![image](https://github.com/user-attachments/assets/b18c678d-8e9f-44a4-8433-d6d47245bd4c)

3. **Поиск по имени**: введите screen_name пользователя (например: `durov`)
![image](https://github.com/user-attachments/assets/b06fbc77-9f18-4ad3-85e8-f181a762ff1a)

## Структура проекта

```
VK_API_Viewer/
├── main.py              # Точка входа в приложение
├── сommand.py           # Основной класс для обработки команд
├── vk_user_explore.py   # Класс для работы с VK API
├── info_print.py        # Класс для форматированного вывода информации
└── README.md           # Документация проекта
```

## Классы и модули

### `VKUserExplore`
Основной класс для взаимодействия с VK API:
- `get_user_info()` - получение информации о пользователе
- `get_friends()` - получение списка друзей
- `get_albums()` - получение списка фотоальбомов
- `resolve_screen_name()` - преобразование screen_name в ID

### `InfoPrint`
Класс для красивого отображения информации:
- `print_user_info()` - форматированный вывод информации о пользователе
- `print_friends()` - вывод списка друзей
- `print_albums()` - вывод списка альбомов

### `command`
Основной класс приложения, управляющий меню и командами.

## Обработка ошибок

Приложение корректно обрабатывает:
- Неверные токены API
- Приватные профили и закрытую информацию
- Несуществующих пользователей
- Ошибки сети и API

## Примечания

- Приложение использует VK API версии 5.131
- Максимальное количество друзей для отображения: 5000
- В списке друзей отображается первые 15, остальные указываются общим количеством
- Все сообщения и интерфейс на русском языке
