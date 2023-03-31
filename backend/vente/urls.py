from django.urls import path, include
from .router import *

urlpatterns = [
    path("user", include(router_user.urls)),
    path("user/<int:id>", include(router_user.urls)),

    path("user/", include(router_user_post.urls)),
    path("fruit/", include(routet_fruit.urls)),
    path("fruit/<int:id>", include(routet_fruit.urls)),

    path("fruit", include(router_fruit_add.urls)),
    path("fruit/<int:id>", include(router_fruit_update.urls)),
    # login and logout url
    path("user", include(router_login.urls)),
    path("user", include(router_logout.urls)),
    

]