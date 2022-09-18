from django.urls import  path
from . import views
from django.contrib.auth.views import LogoutView



urlpatterns=[
    path("",views.TaskList.as_view(),name="tasks"),
    path("register/", views.RegisterPage.as_view(), name="user-register"),
    path("login/",views.CustomLoginView.as_view(),name="user-login"),
    path("logout/",LogoutView.as_view(next_page='user-login'),name="user-logout"),
    path("task/<int:pk>/",views.TaskDetail.as_view(),name="task-detail"),
    path("create-task/",views.CreateTask.as_view(),name="task-create"),
    path("update-task/<int:pk>/",views.TaskUpdate.as_view(),name="task-update"),
    path("delete-task/<int:pk>/",views.TaskDelete.as_view(),name="task-delete"),
    path('notes/', views.index),  
    path('notes/upload/', views.FileUploadView , name = "upload"),  
    path('notes/preview/', views.showimages , name = "preview"),  
]





from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)