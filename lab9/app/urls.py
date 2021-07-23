from . import views
#from django.contrib.auth.views import LoginView

urlpatterns = [
    path('',views.indexView,name="home"),
    path('display/',views.display,name="display"),
]
