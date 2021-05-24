from django.urls import path
from .views import (login_view,
                    register_view,
                    logoutUser,
                    own_profile_view,
                    own_bookcase_view,
                    other_user_view
                    )

urlpatterns = [
    path('login', login_view, name='login-view'),
    path('logout', logoutUser, name='logout'),
    path('register', register_view, name='register-view'),
    path('own/profile', own_profile_view, name='own-profile-view'),
    path('own/bookcase', own_bookcase_view, name='own-bookcase-view'),
    path('user/<int:id>', other_user_view, name='other_user_view'),
]