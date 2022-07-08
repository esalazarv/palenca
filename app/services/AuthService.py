class AuthService:
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def authenticate(self):
        return self.username == "pierre@palenca.com" and self.password == "MyPwdChingon123"

    def check_token(self, token):
        return self.get_token() == token

    def get_token(self):
        return "cTV0aWFuQ2NqaURGRE82UmZXNVBpdTRxakx3V1F5"

    def get_profile(self):
        return {
            "country": "mx",
            "city_name": "Ciudad de Mexico",
            "worker_id": "34dc0c89b16fd170eba320ab186d08ed",
            "first_name": "Pierre",
            "last_name": "Delarroqua",
            "email": "pierre@palenca.com",
            "phone_prefix": "+52",
            "phone_number": "5576955981",
            "rating": "4.8",
            "lifetime_trips": 1254
        }

