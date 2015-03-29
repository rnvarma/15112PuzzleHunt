from django.conf.urls import patterns, include, url
from django.contrib import admin
from puzzlehunt import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'puzzlehunt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.HomePage.as_view()),
    url(r'^register', views.RegistrationPage.as_view()),
    url(r'^puzzles', views.PuzzlePage.as_view())
)
