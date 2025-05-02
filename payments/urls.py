from django.urls import path
from .views import CollectionListCreateView

urlpatterns = [
    path('collections/', CollectionListCreateView.as_view(), name='collection-list-create'),
]
