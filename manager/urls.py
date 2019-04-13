from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from manager.views import TaskViewSet, BoardViewSet

router = DefaultRouter()
router.register(r'task', TaskViewSet, base_name='task')
router.register(r'board', BoardViewSet, base_name='board')


urlpatterns = router.urls
