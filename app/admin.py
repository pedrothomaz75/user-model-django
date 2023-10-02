from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', '_autor') # _autor = função

    # Exclue o dropbox de autores
    exclude = ['autor',] # É uma lista

    def _autor(self, instance):
        # retorna o valor formatado da instancia de post pegando o full name de autor 
        return f'{instance.autor.get_full_name()}'
    
    # Função que retorna a consulta ao banco de dados
    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        # Retorna apenas os livros publicados por aquele autor dentro da página da conta dele
        # basicamente se tu tiver uma conta e livros na conta, vai aparecer apenas os teus livros
        return qs.filter(autor=request.user)
    
    # Função que salva os dados para não dar EntigrityError por conta do Exclude
    def save_model(self, request, obj, form, change):
        
        # obj.autor pega o objeto que o autor vai salvar
        # request.user recebe o dado do usuário que tá logado
        obj.autor = request.user # pega o cara que tá logado

        super().save_model(request, obj, form, change) # Faz o retorno da função