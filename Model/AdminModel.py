class AdminModel:
    def __init__(self, admin_id=0, name=None, email=None, password=None):
        self._admin_id = admin_id
        self._name = name
        self._email = email
        self._password = password

    def get_admin_id(self):
        return self._admin_id

    def set_admin_id(self, admin_id):
        self._admin_id = admin_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_password(self):
        return self._password

    def set_password(self, password):
        self._password = password
