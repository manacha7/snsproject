# Create your views here.
from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import SnsappPostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import SnsappPost
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage
# Create your views here
 
class IndexView(ListView):
    template_name ='index.html'
    queryset = SnsappPost.objects.order_by('-posted_at')
    paginate_by = 100
 
@method_decorator(login_required, name='dispatch')
class CreateSnsappView(CreateView):
    form_class = SnsappPostForm
    template_name = "post.html"
    success_url = reverse_lazy('snsapp:post_done')
    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)
   
class PostSuccessView(TemplateView):
    template_name = 'post_success.html'
 
class CategoryView(ListView):
    template_name ='index.html'
    paginate_by = 9
    def get_queryset(self):
        category_id = self.kwargs['category']
        categories = SnsappPost.objects.filter(category=category_id).order_by('-posted_at')
        return categories
   
class UserView(ListView):
    template_name ='mypage.html'
    paginate_by = 9
    def get_queryset(self):
        user_id = self.kwargs['user']
        user_list = SnsappPost.objects.filter(user=user_id).order_by('-posted_at')
        return user_list
   
class DetailView(DetailView):
    template_name ='detail.html'
    model = SnsappPost
 
class MypageView(ListView):
    template_name ='mypage.html'
    paginate_by = 9
    def get_queryset(self):
        queryset = SnsappPost.objects.filter(user=self.request.user).order_by('-posted_at')
        return queryset
   
class SnsappDeleteView(DeleteView):
    model = SnsappPost
    template_name ='post_delete.html'
    success_url = reverse_lazy('snsapp:mypage')
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
   
class ContactView(FormView):
    template_name='contact.html'
    form_class= ContactForm
    success_url = reverse_lazy('snsapp:contact')
    def form_valid(self, form):
        name = form.cleaned_data['name']
        email= form.cleaned_data['email']
        title= form.cleaned_data['title']
        message= form.cleaned_data['message']
        subject ='お問い合わせ:{}'.format(title)
        message= \
            '送信者名:{0}\nメールアドレス:{1}\n タイトル:{2}\n メッセージ:\n{3}' \
            .format(name,email,title,message)
        from_email = 'mcd2376024@stu.o-hara.ac.jp'
        to_list = ['mcd2376024@stu.o-hara.ac.jp']
        message = EmailMessage(subject=subject,
                               body=message,
                               from_email=from_email,
                               to=to_list,
                               )
        message.send()
        messages.success(self.request,'お問い合わせは正常に送信されました。')
        return super().form_valid(form)