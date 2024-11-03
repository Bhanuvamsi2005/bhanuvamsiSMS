from django.urls import path
from. import views

urlpatterns = [
    path('', views.projecthomepage, name='projecthomepage'),
    path('printpagecall/', views.printpagecall, name='printpagecall'),
    path('printpagelogic/', views.printpagelogic, name='printpagelogic'),
    path('exceptionpagecall/', views.exceptionpagecall, name='exceptionpagecall'),
    path('exceptionpagelogic/', views.exceptionpagelogic, name='exceptionpagelogic'),
    path('randompagecall/', views.randompagecall, name='randompagecall'),
    path('randomlogic/', views.randomlogic, name='randomlogic'),
    path('calpagecall/', views.calpagecall, name='calpagecall'),
    path('calculatorlogic/', views.calculatorlogic, name='calculatorlogic'),
    path('add_task/', views.add_task, name='add_task'),
    path('<int:pk>/delete/', views.delete_task, name='delete_task'),
    path('loginpagecall/', views.loginpagecall, name='loginpagecall'),
    path('registerpagecall/', views.registerpagecall, name='registerpagecall'),
    path('dateandtimepagecall/', views.dateandtimepagecall, name='dateandtimepagecall'),
    path('dateandtimelogic/', views.dateandtimepagelogic, name='dateandtimepagelogic'),
    path('UserLoginPageCall/', views.UserLoginPageCall, name='UserLoginPageCall'),
    path('UserLoginLogic/', views.UserLoginLogic, name='UserLoginLogic'),
    path('UserRegisterPageCall/', views.UserRegisterPageCall, name='UserRegisterPageCall'),
    path('UserRegisterLogic/', views.UserRegisterLogic, name='UserRegisterLogic'),
    path('add_student/', views.add_student, name='add_student'),
    path('logout/', views.logout, name='logout'),
    path('student_list/', views.student_list, name='student_list'),
    path('upload_file/', views.upload_file, name='upload_file'),
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
    path('feedback_success/', views.feedback_success, name='feedback_success'),
    path('add_contact/', views.add_contact, name='add_contact'),
    path('view_contacts/', views.view_contacts, name='view_contacts'),

]