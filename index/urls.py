from django.urls import path
from . import views
urlpatterns = [
    path("" , views.indexView.as_view() , name = "index") ,
    path("comment" , views.comment , name = "comment"),
    # path("send" , views.sendView.as_view() , name = "send"),
    path("send" , views.save_form.as_view() , name = "save_form"),
    path("<slug>" , views.slugView.as_view() , name = "slug")
]