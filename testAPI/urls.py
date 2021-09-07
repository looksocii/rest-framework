from django.urls import include, path
from rest_framework import routers
from testAPI import views
# from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register(r'users', views.UseraccountViewSet)
router.register(r'Book', views.BooklistViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/', views.user_list),
    path('users/<int:id>', views.user_detail),
    path('allbook/', views.allbook_list)
]
