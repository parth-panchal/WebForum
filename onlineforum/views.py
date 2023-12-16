from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from onlineforum.models import Post, CustomUser
from onlineforum.serializers import PostSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .serializers import PostSerializer, CustomUserSerializer, UserSerializer
from rest_framework.decorators import api_view

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class CustomUserView(APIView):
    parser_classes = [JSONParser]

    def get(self, request):

        username = request.GET.get('username')

        if id is None:
            qs = CustomUser.objects.all()
        else:
            qs = CustomUser.objects.filter(username=username)
        
        if qs.exists():
            data = UserSerializer(qs, many=True).data
            return Response(data, status=status.HTTP_200_OK)
        return Response({}, status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        username = request.data.get('username')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')

        if username is None or type(username) != str:
            return Response({"error": "username is incorrect"}, status=status.HTTP_400_BAD_REQUEST)
        
        if first_name is None or type(first_name) != str:
            return Response({"error": "first_name is incorrect"}, status=status.HTTP_400_BAD_REQUEST)
        
        if last_name is None or type(last_name) != str:
            return Response({"error": "last_name is incorrect"}, status=status.HTTP_400_BAD_REQUEST)
        
        # usr = CustomUser.objects.filter(username=username)
        # if usr.exists():
        #     return Response({"error": "username already exists"}, status=status.HTTP_400_BAD_REQUEST)
        # else:
        usr = CustomUser.objects.create(username=username, first_name=first_name, last_name=last_name)
        res = {
            'id': usr.id,
            'username': usr.username,
            'first_name': usr.first_name,
            'last_name': usr.last_name,
            'key': usr.key,
        }

        return Response(res, status=status.HTTP_200_OK)
        
class FullTextSearch(APIView):
    parser_classes = [JSONParser]

    def get(self, request):
        query = request.query_params.get('query', '')
        if query:
            # Perform a simple case-insensitive search within the msg field
            posts = Post.objects.filter(msg__icontains=query)
            serializer = PostSerializer(posts, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "A search query is required."}, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
class PostView(APIView):

    parser_classes = [JSONParser]

    def get(self, request, id):
        user_id = request.GET.get('user_id')
        if user_id is not None:
            try:
                usr = CustomUser.objects.get(id=user_id)
            except CustomUser.DoesNotExist:
                return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
            
            qs = Post.objects.filter(user=usr)
            if qs.exists():
                data = PostSerializer(qs, many=True).data
                return Response(data)
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        if id is None:
            qs = Post.objects.all()
        else:
            qs = Post.objects.filter(id=id)
        
        if qs.exists():
            data = PostSerializer(qs, many=True).data[0]
            return Response(data, status=status.HTTP_200_OK)
        return Response({}, status=status.HTTP_404_NOT_FOUND)
    

    def post(self, request):
        user_id = request.data.get('user_id')
        msg = request.data.get('msg')

        if msg is None or type(msg) != str:
            return Response({"error": "msg is incorrect"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            usr = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            usr = CustomUser.objects.all().first()
            if usr is None:
                return Response({"error": "No users exist"}, status=status.HTTP_404_NOT_FOUND)
        
        post = Post.objects.create(msg=msg, user=usr)

        res = {
            'id': post.id,
            'key': post.key,
            'timestamp': post.timestamp,
        }

        return Response(res, status=status.HTTP_200_OK)
    
    def delete(self, request, id, key):
        try:
            post = Post.objects.get(id=id)
            user_key = request.query_params.get('user_key')
            print(post.user.key)
            print(user_key)

            if post.key == key or post.user.key == user_key:
                res = {
                    'id': post.id,
                    'key': post.key,
                    'timestamp': post.timestamp,
                    'key_origin': "post_key" if post.key==key else "user_key",
                }
                post.delete()
                return Response(res, status=status.HTTP_200_OK)

            if post.key != key:
                return Response({"error": "Incorrect key."}, status=status.HTTP_403_FORBIDDEN)
        
        except Post.DoesNotExist:
            return Response({"error": "Post not found."}, status=status.HTTP_404_NOT_FOUND)
        


# Write a non class based view to get posts by a user id
# @api_view(['GET'])
# def get_posts_by_user_id(request):
#     if request.method == 'GET':
#         try:
#             print(request.GET.get('user_id'))
#             usr = CustomUser.objects.get(id=request.GET.get('user_id'))
#         except CustomUser.DoesNotExist:
#             return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
#         qs = Post.objects.filter(user=usr)
#         if qs.exists():
#             data = PostSerializer(qs, many=True).data
#             return Response(data)
#         return Response({}, status=status.HTTP_404_NOT_FOUND)
    
#     return Response({"error": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@method_decorator(csrf_exempt, name='dispatch')
class PostUserView(APIView):
    parser_classes = [JSONParser]

    def get(self, request):
        print(request.GET.get('user_id'))
        user_id = request.GET.get('user_id')
        if user_id is None:
            # return 400 bad request
            return Response({"error": "user_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                usr = CustomUser.objects.get(id=user_id)
            except CustomUser.DoesNotExist:
                return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
            
            qs = Post.objects.filter(user=usr)
            if qs.exists():
                data = PostSerializer(qs, many=True).data
                return Response(data)
            return Response({}, status=status.HTTP_404_NOT_FOUND)