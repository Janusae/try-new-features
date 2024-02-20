from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.base import  TemplateView
from django.http import Http404
from django.views import View
from .form import model_form

from .form import model_form
from .models import Products , Category ,Comments
# Create your views here.
class indexView(ListView):
    template_name = "index/index.html"
    context_object_name = "data"
    model = Products
class slugView(DetailView):
    template_name = "index/detail.html"
    model = Products
    context_object_name = 'data'
    def get_context_data(self, **kwargs):
        context = super(slugView, self).get_context_data()
        context["comments"] = Comments.objects.all()
        return context
def comment(request):
   return render(request , "index/comment.html" , {
       "form" : model_form
   })
# class sendView(View):
#     def get(self , request):
#         pass
#     def post(self , request):
#         file = model_form(request.)
class save_form(View):
    def get(self , request):
        pass
    def post(self , request):
        file = model_form(request.POST)
        file.save()
        return redirect(reverse("index"))

