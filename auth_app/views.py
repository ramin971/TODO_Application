from .serializers import TokenRefreshSerializer,UserCreateSerializer,UserUpdateSerializer\
                ,ChangePasswordSerializer
from .models import User
from .permissions import CreateOrIsAdmin
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status,mixins,viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings



class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    pagination_class = PageNumberPagination
    permission_classes =[CreateOrIsAdmin]

    def get_serializer_class(self):
        if self.action in ['update','partial_update']:
            return UserUpdateSerializer
        else:
            return UserCreateSerializer
       
    
    # create_user / set refresh_cookie / add access_response
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.create_user(password=serializer.validated_data['password'],**serializer.data)
        print('@@@@@@@@@@',user)
        refresh_token = RefreshToken.for_user(user)
        
        result = {**serializer.data , **{'access':str(refresh_token.access_token)}}
        response = Response(result , status=status.HTTP_201_CREATED)
        response.set_cookie('refresh_token', refresh_token, max_age=settings.COOKIE_MAX_AGE, httponly=True, path='/api/auth/jwt/refresh')
        return response

    @action(detail=False , methods=['get','put','patch','delete'],permission_classes=[IsAuthenticated])
    def me(self,request):
        user = request.user
        if request.method == 'GET':
            serializer = UserUpdateSerializer(user)
            return Response(serializer.data,status=status.HTTP_200_OK)

        elif request.method in ['PUT','PATCH']:
            serializer = UserUpdateSerializer(user,data=request.data,partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)

        elif request.method == 'DELETE':
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
    @action(detail=False , methods=['post'],permission_classes=[IsAuthenticated])
    def change_password(self,request):
        serializer = ChangePasswordSerializer(data=request.data,context={'user':request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Password changed successfully'},status=status.HTTP_205_RESET_CONTENT)



class CustomTokenObtainPairView(TokenObtainPairView):
    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get('refresh'):
            response.set_cookie('refresh_token', response.data['refresh'], max_age=settings.COOKIE_MAX_AGE, httponly=True, path='/api/auth/jwt/refresh')
            del response.data['refresh']
        return super().finalize_response(request, response, *args, **kwargs)

class CustomTokenRefreshView(TokenRefreshView):
    serializer_class = TokenRefreshSerializer
    # If SimpleJWT ROTATE_REFRESH_TOKENS = True :
    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get('refresh'):
            response.set_cookie('refresh_token', response.data['refresh'], max_age=settings.COOKIE_MAX_AGE, httponly=True, path='/api/auth/jwt/refresh')
            del response.data['refresh']
        return super().finalize_response(request, response, *args, **kwargs)