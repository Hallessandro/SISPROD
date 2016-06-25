from django.conf.urls import patterns,include,url
from appprod.views import *

urlpatterns=[
    url(r'^$',home,name='home'),
    url(r'^prestador/$',exibirPrestador,name='prestador'),
    url(r'^materia/$',exibirMateria,name='materia'),
    url(r'^processo/$', exibirProcesso, name='processo'),
]

