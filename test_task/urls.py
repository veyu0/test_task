from django.contrib import admin
from django.urls import path, include
from mainapp.views import MainListView, CatsCreateView, AboutUsListView, CatsListView, CatsUpdateView, CatDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainListView.as_view(), name='main'),
    path('cats/', CatsListView.as_view(), name='cats'),
    path('about_us/', AboutUsListView.as_view(), name='about_us'),
    path('accounts/', include('authapp.urls', namespace='auth')),
    path('create_cats/', CatsCreateView.as_view(), name='create_cats'),
    path('update_cats/<int:pk>', CatsUpdateView.as_view(), name='update_cats'),
    path('delete_cat/<int:pk>', CatDeleteView.as_view(), name='delete_cat')
]
