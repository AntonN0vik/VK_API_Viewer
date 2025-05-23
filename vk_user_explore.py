import requests


class VKUserExplore:
    def __init__(self, token):
        self.token = token
        self.api_version = '5.131'
        self.base_url = 'https://api.vk.com/method/'

    def _make_request(self, method, params):
        params.update({
            'access_token': self.token,
            'v': self.api_version
        })
        response = requests.get(f'{self.base_url}{method}', params=params)
        data = response.json()

        if 'error' in data:
            error_msg = data['error']['error_msg']
            raise Exception(f"Ошибка API: {error_msg}")
        return data['response']

    def get_user_info(self, user_id):
        if user_id:
            params = {
                'user_ids': user_id,
                'fields': 'first_name,last_name,bdate,city,country,photo_200'
            }
        else:
            params = {
                'fields': 'first_name,last_name,bdate,city,country,photo_200'
            }
        response = self._make_request('users.get', params)
        return response[0] if response else None

    def resolve_screen_name(self, screen_name):
        params = {
            'screen_name': screen_name
        }
        try:
            response = self._make_request('utils.resolveScreenName', params)
            return response.get('object_id') if response else None
        except Exception:
            return None

    def get_friends(self, user_id):
        if not str(user_id).isdigit():
            resolved_id = self.resolve_screen_name(user_id)
            if not resolved_id:
                raise ValueError("Не удалось найти указанного пользователя")
            user_id = resolved_id

        params = {
            'user_id': user_id,
            'fields': 'first_name,last_name,photo_50',
            'count': 5000
        }
        try:
            response = self._make_request('friends.get', params)
            return response['items']
        except Exception as e:
            if "15" in str(e):
                raise ValueError(
                    "Список друзей недоступен (закрыт настройками приватности)")
            raise e

    def get_albums(self, user_id):
        if not str(user_id).isdigit():
            resolved_id = self.resolve_screen_name(user_id)
            if not resolved_id:
                raise ValueError("Не удалось найти указанного пользователя")
            user_id = resolved_id

        params = {
            'owner_id': user_id,
            'need_system': 0,
            'need_covers': 1
        }
        try:
            response = self._make_request('photos.getAlbums', params)
            return response['items']
        except Exception as e:
            if "15" in str(e):
                raise ValueError(
                    "Фотоальбомы недоступны (закрыты настройками приватности)")
            raise e

    def get_user_wall(self, user_id, count=10):
        if not str(user_id).isdigit():
            resolved_id = self.resolve_screen_name(user_id)
            if not resolved_id:
                raise ValueError("Не удалось найти указанного пользователя")
            user_id = resolved_id

        params = {
            'owner_id': user_id,
            'count': count,
            'filter': 'owner'
        }
        try:
            response = self._make_request('wall.get', params)
            return response['items']
        except Exception as e:
            if "15" in str(e):
                raise ValueError(
                    "Записи на стене недоступны (закрыты настройками приватности)")
            raise e
