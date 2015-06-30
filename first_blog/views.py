from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView, FormView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Author, Blog
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from first_blog.blog_forms import form_templates
from django.views.generic.base import TemplateResponseMixin

# Create your views here.
class GeneralHomePageView(View):

    def get(self, request):
        return render(request, 'first_blog/general_home_page.html')

    def post(self, request):
        if request.POST.get("sign_up"):
            return HttpResponseRedirect(reverse('first_blog:sign_up_page'))
        else:
            return HttpResponseRedirect(reverse('first_blog:log_in_page'))


class SignUpPageView(View):
    def get(self, request):
        form = form_templates.UserSignUpForm()
        return render(request, 'first_blog/sign_up_page.html', {'form':form})

    def post(self, request):
        form = form_templates.UserSignUpForm(request.POST)

        if form.is_valid():
            user_name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username=user_name, password=password, email=email)
            user.save()
            author = Author(user=user)
            author.save()
            return HttpResponseRedirect(reverse('first_blog:user_home_page', kwargs={'user_name': user_name}))
        else:
            form = form_templates.UserSignUpForm()
            return render(request, 'first_blog/sign_up_page.html', {'form': form})


class UserHomePageView(View):
    template_name = 'first_blog/user_home_page.html'

    def get(self, request, user_name):
        user = User.objects.get(username=user_name)
        author = get_object_or_404(Author, user=user)
        user_entry = Blog.objects.all().filter(author=author)
        return render(request, self.template_name, {'user_entry': user_entry, 'author_name': user_name})

    def post(self, request, user_name):
        if request.POST.get("list_of_all_blogs"):
            return HttpResponseRedirect(reverse('first_blog:list_all_blog_entries', kwargs={'user_name': user_name}))
        elif request.POST.get("sign_out_button"):
            logout(request)
            return HttpResponseRedirect(reverse('first_blog:home_page'))
        else:
            return HttpResponseRedirect(reverse('first_blog:new_blog_entry', kwargs={'user_name': user_name}))


class NewEntryView(View):

    def get(self, request, user_name):
        form = form_templates.NewBlogEntryForm()
        return render(request, 'first_blog/new_entry_page.html', {'user_name': user_name, 'form':form})

    def post(self, request, user_name):
        form = form_templates.NewBlogEntryForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=user_name)
            the_author = Author.objects.get(user=user)
            subject = form.cleaned_data.get('subject')
            body = form.cleaned_data.get('body')
            new_blog = Blog(subject=subject, body=body, author=the_author, date_created=datetime.date.today())
            new_blog.save()
            return HttpResponseRedirect(reverse('first_blog:user_home_page', kwargs={'user_name': user_name}))
        else:
            form = form_templates.NewBlogEntryForm({})
            return render(request, 'first_blog/new_entry_page.html', {'form':form})


class ListOfBlogEntryViews(ListView):

    template_name = 'first_blog/list_all_entries_page.html'
    queryset = Blog.objects.order_by('date_created')
    context_object_name = 'all_blog_entry'

    def post(self, request, user_name):
        if self.request.POST.get('sign_out_button'):
            logout(request)
            return HttpResponseRedirect(reverse('first_blog:home_page'))


class LoginView(FormView):

    form_class = form_templates.LogInForm
    template_name = 'first_blog/log_in_page.html'

    def get_success_url(self):
        self.success_url = 'first_blog:user_home_page'
        return reverse(self.success_url, kwargs={'user_name': self.request.user.username})

    def form_valid(self, form):
        name = form.cleaned_data['name']
        password = form.cleaned_data['password']
        user = authenticate(username=name, password=password)
        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(self.get_success_url())
        else:
            form = form_templates.LogInForm({})
            return render(self.request,'first_blog/log_in_page.html', {'form': form})







