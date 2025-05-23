from info_print import InfoPrint
from vk_user_explore import VKUserExplore


class command:
    def __init__(self):
        self.printer = InfoPrint()
        self.vk = None
        self.current_user = None
        self.commands = {
            '1': ('help', "Показать меню команд"),
            '2': ('info', "Получить информацию о пользователе"),
            '3': ('friends', "Просмотреть список друзей"),
            '4': ('albums', "Просмотреть фотоальбомы"),
            '0': ('exit', "Завершить работу программы")
        }

    def _initialize_api(self):
        token = input("Пожалуйста, введите ваш VK API токен: ").strip()

        self.vk = VKUserExplore(token)
        try:
            self.current_user = self.vk.get_user_info('')
            print(
                f"\nВход выполнен успешно! Приветствую, {self.current_user['first_name']}!")
        except Exception as e:
            print(f"Не удалось выполнить авторизацию: {e}")
            raise e

    def _show_menu(self):
        print("\n" + "=" * 50)
        print("МЕНЮ КОМАНД:")
        print("=" * 50)
        for num, (cmd, desc) in self.commands.items():
            print(f"[{num}] {desc}")
        print("=" * 50)

    def _process_command(self, command_num):
        if command_num not in self.commands:
            print("Неверный номер команды. Попробуйте снова.")
            return True

        command_name = self.commands[command_num][0]

        if command_name == 'exit':
            print("\nРабота программы завершена. До встречи!")
            return False
        elif command_name == 'help':
            self._show_menu()
        elif command_name in ['info', 'friends', 'albums']:
            self._handle_user_command(command_name)

        return True

    def _handle_user_command(self, command):
        user_input = input(
            "\nВведите ID пользователя или его имя (оставьте пустым для своего профиля): ").strip()

        user_id = None
        if user_input:
            if user_input.isdigit():  # Если введен числовой ID
                user_id = int(user_input)
            else:  # Если введен screen_name
                try:
                    user_id = self.vk.resolve_screen_name(user_input)
                    if not user_id:
                        print("Пользователь с таким именем не найден")
                        return
                except Exception as e:
                    print(f"Ошибка при поиске пользователя: {e}")
                    return
        else:
            user_id = self.current_user['id']

        try:
            if command == 'info':
                user_info = self.vk.get_user_info(user_id)
                if user_info:
                    self.printer.print_user_info(user_info)
                else:
                    print("Информация о пользователе недоступна")
            elif command == 'friends':
                self.printer.print_friends(self.vk.get_friends(user_id))
            elif command == 'albums':
                self.printer.print_albums(self.vk.get_albums(user_id))
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    def run(self):
        try:
            self._initialize_api()
        except:
            return

        self._show_menu()

        while True:
            try:
                command_num = input(
                    "\nВыберите команду (введите номер): ").strip()
                if not self._process_command(command_num):
                    break
            except KeyboardInterrupt:
                print("\nВыполнение прервано пользователем")
                break