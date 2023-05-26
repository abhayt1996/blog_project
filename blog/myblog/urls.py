from django.urls import include

urlpatterns = [
    # Other URL patterns in your project
    path('api/', include('myblog.urls')),
]
