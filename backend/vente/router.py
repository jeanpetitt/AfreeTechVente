from rest_framework.routers import DefaultRouter
from .views import *

# router to allow user to acces in his page
router_user = DefaultRouter()
router_user.register('', UserViewset, basename='user')

# build router to register user
router_user_post = DefaultRouter()
router_user_post.register('register', UserRegisterViewSet, basename='register')

# router to see fruit
routet_fruit = DefaultRouter()
routet_fruit.register('', FruitViewSet, basename="fruit")

# router to add fruit
router_fruit_add = DefaultRouter()
router_fruit_add.register('add', FruitViewsetPost, basename="post_fruit")

# router to update state of fruit
router_fruit_update = DefaultRouter()
router_fruit_update.register('update', FruitViewsetUpdate, basename='update_fruit')

# router login user
router_login = DefaultRouter()
router_login.register('login', UserLoginView, basename='login')

# router logout user
router_logout = DefaultRouter()
router_logout.register('logout', UserLogoutView, basename="logout")





