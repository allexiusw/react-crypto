from rest_framework.views import APIView
from django.http.response import JsonResponse


class HelloWorldView(APIView):
    def get(self, request):
        return JsonResponse({'message': 'Welcomo to the api'})
