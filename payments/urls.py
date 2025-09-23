from django.urls import path
from django.http import JsonResponse

def health_check(request):
    return JsonResponse({"status": "ok"})

urlpatterns = [
    path("health/", health_check, name="health_check"),  # 👈 put health check FIRST
    path("payments/", lambda r: JsonResponse({"msg": "process_payment"}), name="process_payment"),
]
