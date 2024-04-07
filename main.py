class User:
    def __init__(self, user_id, name, access_level='user'):
        self._user_id = user_id
        self._name = name
        self._access_level = access_level

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, new_name):
        self._name = new_name

    def __str__(self):
        return f"ID: {self._user_id}, Name: {self._name}, Уровень доступа: {self._access_level}"


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, 'admin')
        self.users = []

    def add_user(self, user):
        if user not in self.users:
            self.users.append(user)
            print(f"User {user.get_name()} добавлен успешно.")
        else:
            print("Пользователь уже в системе.")

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)
            print(f"User {user.get_name()} удален успешно.")
        else:
            print("Пользователь не найден в системе.")

    def list_users(self):
        print("Все пользователи:")
        for user in self.users:
            print(user)


# Example usage
if __name__ == "__main__":
    admin = Admin("1", "Админ Вася")
    user1 = User("2", "Петя")
    user2 = User("3", "Света")

    admin.add_user(user1)
    admin.add_user(user2)

    # List all users
    admin.list_users()

    # Remove a user
    admin.remove_user(user1)

    # List all users again to confirm removal
    admin.list_users()