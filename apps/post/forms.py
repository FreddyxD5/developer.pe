from django import forms
from .models import Post
from pagedown.widgets import PagedownWidget

class PostForm(forms.ModelForm):
	nueva_entrada = forms.CharField(widget=PagedownWidget(show_preview=True))
	class Meta:
		model = Post 
		fields = ['nueva_entrada','titulo','fecha','firma','categoria','descripcion','imagen',]
		labels = {'nueva_entrada':'Post','titulo':'Titulo','fecha':'Fecha de creacion',
				'firma':'Autor','categoria':'Categoria','descripcion':'Breve Descripcion','image':'URL'}
		widgets = {'titulo':forms.TextInput(),				
				'firma':forms.TextInput(),'fecha':forms.SelectDateWidget,
				'categoria':forms.TextInput(),'descripcion':forms.Textarea(),}
				#forms.TextInput(attrs = {'placeholder':'AA/MM/DD'})
