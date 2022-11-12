from django.urls import path
from regist.views import *

urlpatterns = [
    path('list/', ad_list),
    path('', ad_create),
    path('<int:pk>', advert)
]
