from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('signup/',views.signup,name='signup'),
    path('addstudent/',views.addstudent,name='addstudent'),
    path('loginto/',views.loginto,name='loginto'),
    path('adminhome/',views.adminhome,name='adminhome'),
    path('course/',views.course,name='course'),
    path('addcourse/',views.addcourse,name='addcourse'),
    path('studentdb/',views.studentdb,name='studentdb'),
    path('showstudent/',views.showstudent,name='showstudent'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('editdb/<int:pk>',views.editdb,name='editdb'),
    path('Delete/<int:pk>',views.Delete,name='Delete'),
    path('register/',views.register,name='register'),
    path('teacherpage/',views.teacherpage,name='teacherpage'),
    path('showteacher/',views.showteacher,name='showteacher'),
    path('Delete_teacher/<int:pk>',views.Delete_teacher,name='Delete_teacher'),
    path('Logout/',views.Logout,name='Logout'),
    path('showprofile/',views.showprofile,name='showprofile'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('showprofile1/<int:user_id>',views.showprofile1,name='showprofile1'),
    # path('editteacher/<int:pk>',views.editteacher,name='editteacher'),
    








]