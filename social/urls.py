from django.urls import path
from .views import AddCollectionView, AllCollectionsView, CollectionDetailView

urlpatterns = [
    path('add_collection/', AddCollectionView.as_view()),
    path('all_collection/', AllCollectionsView.as_view()),
    path('collection/<str:collection_id>/', CollectionDetailView.as_view()),
]
