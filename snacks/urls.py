from django.urls import path
from .views import SnackListView,SnackDetailView,SnackCreateView,SnackUpdateView,SnackDeleteView

urlpatterns=[
    path('',SnackListView.as_view(),name='snack'),
    path('<int:pk>/',SnackDetailView.as_view(),name='detail'),
    path('create/',SnackCreateView.as_view(),name='create'),
    path('<int:pk>/update/',SnackUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/',SnackDeleteView.as_view(), name='delete'),
]