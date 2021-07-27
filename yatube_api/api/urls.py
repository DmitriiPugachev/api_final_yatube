"""API app v.1 URLs."""


from django.urls import include, path

urlpatterns = [
    path('v1/', include('api.v1.urls'))
]
