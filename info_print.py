class InfoPrint:
    @staticmethod
    def print_user_info(user_info):
        print("\n" + "=" * 40)
        print("ИНФОРМАЦИЯ О ПОЛЬЗОВАТЕЛЕ")
        print("=" * 40)
        print(f"Имя: {user_info.get('first_name', 'Не указано')}")
        print(f"Фамилия: {user_info.get('last_name', 'Не указано')}")
        print(f"Дата рождения: {user_info.get('bdate', 'Не указана')}")

        city = user_info.get('city', {})
        city_name = city.get('title', 'Не указан') if isinstance(city,
                                                                 dict) else 'Не указан'
        print(f"Город: {city_name}")

        country = user_info.get('country', {})
        country_name = country.get('title', 'Не указана') if isinstance(
            country, dict) else 'Не указана'
        print(f"Страна: {country_name}")

        user_id = user_info.get('id', 'Неизвестен')
        print(f"ID пользователя: {user_id}")
        print("=" * 40)

    @staticmethod
    def print_friends(friends):
        print("\n" + "=" * 40)
        print(f"СПИСОК ДРУЗЕЙ (всего: {len(friends)})")
        print("=" * 40)

        if not friends:
            print("Список друзей пуст или недоступен")
            return

        # Показываем первых 15 друзей
        display_count = min(15, len(friends))
        for i, friend in enumerate(friends[:display_count], 1):
            first_name = friend.get('first_name', '')
            last_name = friend.get('last_name', '')
            friend_id = friend.get('id', '')
            print(f"{i:2d}. {first_name} {last_name} (ID: {friend_id})")

        if len(friends) > display_count:
            print(f"... и еще {len(friends) - display_count} друзей")
        print("=" * 40)

    @staticmethod
    def print_albums(albums):
        print("\n" + "=" * 40)
        print(f"ФОТОАЛЬБОМЫ (всего: {len(albums)})")
        print("=" * 40)

        if not albums:
            print("Альбомы отсутствуют или недоступны")
            return

        for i, album in enumerate(albums, 1):
            title = album.get('title', 'Без названия')
            size = album.get('size', 0)
            album_id = album.get('id', '')

            print(f"{i:2d}. {title}")
            print(f"    Фотографий: {size}")
            print(f"    ID альбома: {album_id}")
        print("=" * 40)