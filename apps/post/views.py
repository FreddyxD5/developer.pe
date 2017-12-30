from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm
from django.http import HttpResponse,HttpResponseNotFound
#from django.views.generic import CreateView,DeleteView,UpdateView,ListView
from django.core.urlresolvers import reverse_lazy

def home(request):
	post = Post.objects.all()
	context = {'post':post}
	return render(request,'post/base.html',context)


############################### POST GENERALES ####################################
def crear_post_general(request):
	if request.method == 'POST':
		form = PostForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			form.save()
			return redirect('post:index')		
	else:
		form = PostForm()

	return render(request,'post/general/crear_post_general.html',{'form':form})

def list_post_general(request):
	post = Post.objects.filter(categoria = "General")
	context = {'post':post,}
	return render(request,'post/general/listar_post_general.html',context)


def detail_post_general(request,pk):
	post = Post.objects.filter(id=pk)
	post2 = post[0] if len(post) == 1 else None
	if post2 is not None:
		context = {
			'post2':post2
		}
		return render(request,'post/general/detail_general.html',context)
	else:
		return HttpResponseNotFound('No existe el post')

#############################################################################################

############################### POST TECNOLOGIA ####################################

def list_post_tecnologia(request):
    post = Post.objects.filter(categoria = "Tecnologia")
    context = {'post':post,}
    return render(request,'post/listar_post_tecnologia.html',context)

#############################################################################################

############################### POST VIDEOJUEGOS ####################################
def list_post_videojuegos(request):
    post = Post.objects.filter(categoria = "Videojuegos")
    context = {'post':post,}
    return render(request,'post/listar_post_videojuegos.html',context)

#############################################################################################


############################### POST GENERALES ####################################
def list_post_programacion(request):
    post = Post.objects.filter(categoria = "Programacion")
    context = {'post':post,}
    return render(request,'post/listar_post_programacion',context)






#############################################################################################