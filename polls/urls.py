from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('perguntas', views.ultimas_perguntas, name='ultimas_perguntas'),
    path('sobre/', views.sobre, name='sobre'),
    path('pergunta/<int:question_id>', views.exibe_questao, name='exibe_questao'),
    path('cadastrar', views.QuestionCreateView.as_view(), name="question-create")
   
]

from . import views
urlpatterns = [
# (...manter tudo o que já existe…)
path('pergunta/<int:pk>/edit',
views.QuestionUpdateView.as_view(),
name="poll_edit"
),
path('pergunta/<int:pk>/delete',
views.QuestionDeleteView.as_view(),
name="poll_delete"
),
]

from . import views
urlpatterns = [
# (...manter tudo o que já existe…)
path('pergunta/<int:pk>/show',
views.QuestionDetailView.as_view(),
name="poll_show"
),
path('pergunta/all',
views.QuestionListView.as_view(),
name="polls_all"
),
]

from . import views
urlpatterns = [
# (...manter tudo o que já existe…)
path('about-us',
views.SobreTemplateView.as_view(),
name="about_page"
),
]

