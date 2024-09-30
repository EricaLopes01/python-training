from django.shortcuts import render


def post_list(request):
    posts = Post.objects.all()  # Busca todos os posts do banco de dados
    return render(request, 'blog/post_list.html', {'posts': posts}) 