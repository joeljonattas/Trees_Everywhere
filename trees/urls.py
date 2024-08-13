from django.urls import path, include
from . import views
from .views import PlantedTreeCreateView, PlantedTreeApiView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'planted_trees', PlantedTreeApiView, basename='planted_tree')

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('trees/', views.user_trees, name='user_trees'),
    path('tree/<int:id>/', views.tree_detail, name='tree_detail'),
    path('add_tree/', PlantedTreeCreateView.as_view(), name='add_tree'),
    path('api/', include(router.urls)),
]  