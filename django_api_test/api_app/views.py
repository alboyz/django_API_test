from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import APIView

from rest_framework import generics
from rest_framework import mixins

from .models import Article
from .serializers import ArticleSerializer
# Create your views here.

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


