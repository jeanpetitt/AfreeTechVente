from django.urls import path, include
from .router import *

urlpatterns = [
    path("viewset/", include(router_user.urls)),
    path("viewset/<int:id>/", include(router_user.urls)),

    path("users/", include(router_user_post.urls)),
    path("views/", include(router_fruit.urls)),
    path("views/<int:id>", include(router_fruit.urls)),

    # login and logout url
    path("user/login", UserLoginView.as_view()),
    path("user/logout", UserLogoutView.as_view()),
    

]