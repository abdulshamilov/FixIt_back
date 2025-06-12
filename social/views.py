from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from .models import Collection
from .serializers import CollectionSerializer

class AddCollectionView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = CollectionSerializer 

    def post(self, request):
        data = request.data.copy()
        data['author'] = request.user.id
        serializer = self.serializer_class(data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True, 'collection': serializer.data, 'error': []})
        return Response({'status': False, 'error': serializer.errors})


class AllCollectionsView(APIView):
    serializer_class = CollectionSerializer 

    def get(self, request):
        collections = Collection.objects.all()
        serializer = self.serializer_class(collections, many=True)
        return Response({'status': True, 'collection_list': serializer.data, 'error': []})


class CollectionDetailView(APIView):
    serializer_class = CollectionSerializer 

    def get(self, request, collection_id):
        try:
            collection = Collection.objects.get(id=collection_id)
            serializer = self.serializer_class(collection)
            return Response({'status': True, 'collection_list': [serializer.data], 'error': []})
        except Collection.DoesNotExist:
            return Response({'status': False, 'error': ['Сбор не найден']})
