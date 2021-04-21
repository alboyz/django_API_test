from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins, status, viewsets
from rest_framework.decorators import APIView
from rest_framework.response import Response

from .models import Article
from .serializers import ArticleSerializer

# Create your views here.

class ArticleViewSet(viewsets.GenericViewSet, 
                     mixins.ListModelMixin, 
                     mixins.CreateModelMixin,  
                     mixins.RetrieveModelMixin, 
                     mixins.UpdateModelMixin, 
                     mixins.DestroyModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer





'''
class ArticleViewSet(viewsets.ViewSet):
    def list(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def update(self, request, pk=None):
        article = Article.objects.get(pk=pk)

        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        article = Article.objects.get(pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    '''


'''
class ArticleList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class ArticleDetails(generics.GenericAPIView, 
                     mixins.RetrieveModelMixin, 
                     mixins.UpdateModelMixin, 
                     mixins.DestroyModelMixin):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    lookup_field='id'

    def get(self, request, id):
        return self.retrieve(request, id=id)

    def put (self, request, id):
        return self.update(request, id=id)

    def delete (self, request, id):
        return self.destroy(request, id=id)
'''


'''
@api_view(['GET', 'POST'])
def article_list(request):
    # Get All Article
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': 
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET',  'PUT', 'DELETE'])
def article_details (request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT': 
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''
