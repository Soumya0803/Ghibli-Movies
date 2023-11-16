from rest_framework.authentication import TokenAuthentication

class GhibliKeyAuthentication(TokenAuthentication):
    keyword = 'ghiblikey'

    def authenticate_header(self, request):
        return 'ghiblikey'