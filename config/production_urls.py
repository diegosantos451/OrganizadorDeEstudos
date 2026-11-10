from django.db import DatabaseError, connection
from django.http import JsonResponse
from django.urls import path
from django.views.generic import RedirectView
from .urls import urlpatterns as app_urls


def health(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute('SELECT 1')
            cursor.fetchone()
    except DatabaseError:
        return JsonResponse({'status': 'unavailable'}, status=503)
    return JsonResponse({'status': 'ok'})


urlpatterns = [
    path('', RedirectView.as_view(pattern_name='lista_tarefas')),
    path('saude/', health),
    *app_urls,
]
