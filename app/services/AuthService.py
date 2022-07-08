class AuthService:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(self):
        return self.username == "pierre@palenca.com" and self.password == "MyPwdChingon123"

    def getToken(self):
        return "cTV0aWFuQ2NqaURGRE82UmZXNVBpdTRxakx3V1F5"

