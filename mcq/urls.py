
from django.urls import path, re_path
from mcq import views
# from django.contrib.auth import views as auth_views

urlpatterns =[
    
    path('',views.home_page,name='home'), #chenged
    path('home',views.home_page,name='home'),
    path('single_topic', views.single_topic, name='single_topic'),
    path('select_subjects',views.select_subject, name='select_subject'),
    # path('mcqlist', views.P_Mcq, name='P_Mcq'),
    path('subjectlist',views.select_subject, name='test_subject'),
    path('grandtest',views.GrandTest, name='grand_test'),
    path('test/<subject>/<topic>/<int:mcq_no>',views.test, name='test'),
    path('testresults', views.testresults, name='testresults'),
    # path('reportquestion/<int:pk>', views.report_question, name='report_question'),
    # path('postquestion', views.PublicMcqFormView.as_view(), name='post-question'),
    # path('postanswer', views.Post_A.as_view(), name='post-answer'),
    # path('oneliner', views.post_1liner,name='post-oneliner'),
    # path('postq', views.postq, name='postq'),
    # path('liner',views.post_1liner.as_view(), name='Post_form'),
    path('ajax/load-topic/', views.load_topic, name='ajax_load_topic'),
    # # path('posttestq', views.posttestq, name='posttestq'),
    # # path('pst', views.posttestqx, name='posttestqx'),


]
