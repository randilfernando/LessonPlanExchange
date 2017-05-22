from django.conf.urls import url

from lessonPlan import views

urlpatterns = [
    url(r'^$', views.landing, name='index'),
    url(r'^add-lesson$', views.add_lesson, name='add_question'),
    url(r'browse-by-subject', views.browse_by_subject, name='browse by subject'),
]
