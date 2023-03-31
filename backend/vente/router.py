from rest_framework.routers import DefaultRouter
from .views import *

# router to allow user to acces in his page
router_user = DefaultRouter()
router_user.register('users', UserViewset, basename='user')

# build router to register user
router_user_post = DefaultRouter()
router_user_post.register('register', UserRegisterView, basename='register')

# router to see fruit
router_fruit = DefaultRouter()
router_fruit.register('fruits', FruitViewSet, basename="fruits")

# router to update state of fruit

