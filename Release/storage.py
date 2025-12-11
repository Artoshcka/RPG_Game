import pickle
import os

path = r'Storage/data.pkl'


def save_data(user, characters):
    try:
        with open(path, 'wb') as f:
            pickle.dump({
                'user': user,
                'characters': characters
            }, f)
        #print(f"Данные сохранены: {path}")
    except Exception as e:
        print(f'Ошибка сохранения: {e}')


def load_data():
    if not os.path.exists(path):
        print(f'Файл сохранения не найден: {path}')
        return None, None
    try:
        with open(path, 'rb') as f:
            data = pickle.load(f)

        user = data['user']
        characters = data['characters']

        #print(f"Данные загружены: {path}")
        return user, characters

    except pickle.UnpicklingError as e:
        print(f'Ошибка распаковки pickle: {e}')
        return None, None
    except KeyError as e:
        print(f'Отсутствует ключ в данных: {e}')
        return None, None
    except Exception as e:
        print(f'Неожиданная ошибка: {e}')
        return None, None
