from django.urls import include, path
from rest_framework import routers
from django.conf.urls import url
from myapi import views

router = routers.DefaultRouter()
router.register(r'post-it', views.PostItView)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', views.PostItView),
    path('<int:pk/>', views.postit_details)
]
