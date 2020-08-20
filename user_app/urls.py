from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.home, name="Home"),
    path("invest/<int:username>/", views.investinfo, name="InvestInfo" ),
    path("entre/idea/", views.entreidea, name="EntreIdea" ),
    path("entre/<int:username>/", views.entreinfo, name="EntreInfo" ),
    path("moreinfo/", views.moreinfo, name="MoreInfo" ),
    path("idea", views.ideah, name="Ideah"),
    path("idea/<int:username>/", views.ideainfo, name="IdeaInfo" ),
    path("about", views.about, name="About"),
    path("contact", views.contact, name="Contact"),
    path("invest/", views.investindex, name="InvestIndex" ),
    path("entre/", views.entreindex, name="EntreIndex" ),
    path("login/", views.login_user, name="Login"),
    path("sign_up", views.sign_up, name="Sign_up"),
    path("logout/", views.logout_user, name="logout"),
    path("abc/", views.abc, name="abc")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)