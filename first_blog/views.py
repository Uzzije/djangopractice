from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import Author, Blog
from Useful_Blog_Code import user_validation
import datetime

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        if request.POST.get("sign_up"):
            return HttpResponseRedirect(reverse('first_blog:sign_up_page'))
        elif request.POST.get("log_in"):
            return HttpResponseRedirect(reverse('first_blog:log_in_page'))
    return render(request, 'first_blog/General_Home_Page.html')


def sign_up_page(request):
    if request.method == 'POST':
        user_name = request.POST.get("user_name")
        password = request.POST.get("user_password")
        verify_password = request.POST.get("verify_user_password")
        email = request.POST.get("user_email")
        entries_valid = user_validation.sign_up_entry_validation(user_name, password, verify_password, email)
        if entries_valid is True:
            new_author = Author(user_name=user_name, password=password, email=email)
            new_author.save()
            return HttpResponseRedirect(reverse('first_blog:user_home_page', kwargs={'user_name': user_name}))
        else:
            user_name_error = user_validation.sign_up_check_valid_name(user_name)
            user_password_error = user_validation.sign_up_password_valid(password, verify_password)
            email = user_validation.check_valid_email(email)
            return render(request, 'first_blog/Sign_In_Page.html', {'user_name_error': user_name_error,
                                                                   'user_password_error':user_password_error,
                                                                    'email_error': email})
    return render(request, 'first_blog/Sign_In_Page.html')

def user_home_page(request, user_name):
    user_entry = Blog.objects.all().filter(author__user_name=user_name)
    if request.POST.get("sign_out_button"):
            return HttpResponseRedirect(reverse('first_blog:home_page'))
    if request.method == 'POST':
        if request.POST.get("list_of_all_blogs"):
            return HttpResponseRedirect(reverse('first_blog:list_all_blog_entries', kwargs={'user_name': user_name}))
        return HttpResponseRedirect(reverse('first_blog:new_blog_entry', kwargs={'user_name': user_name}))
    return render(request, 'first_blog/user_home_page.html', {'user_entry': user_entry,
                                                              'author_name': user_name})


def new_blog_entry(request, user_name):
    if request.method == 'POST':
        subject = request.POST.get("subject")
        blog_body = request.POST.get("user_blog_body")
        subject_error = ""
        if subject is None:
            subject_error = "Sorry Subject is Invalid"
        blog_body_error = ""
        if blog_body is None:
            blog_body_error = "Sorry Body of Blog is Invalid"
        if subject_error is not None and blog_body is not None:
            the_author = Author.objects.get(user_name=user_name)
            new_blog = Blog(subject=subject, body=blog_body, author=the_author, date_created=datetime.date.today())
            new_blog.save()
            return HttpResponseRedirect(reverse('first_blog:user_home_page', kwargs={'user_name': user_name}))
        else:
            return render(request,'first_blog/new_entry_page.html', {'subject_error': subject_error,
                                                                'blog_body_error': blog_body_error})
    return render(request, 'first_blog/new_entry_page.html', {'user_name': user_name})


def list_all_blog_entries(request, user_name):
    all_blogs = Blog.objects.order_by('date_created')
    if request.method == 'POST':
        return HttpResponseRedirect(reverse('first_blog:home_page'))
    return render(request, 'first_blog/list_all_entries_page.html', {
                                                                'all_blogs': all_blogs})

def log_in_page(request):
    if request.method == 'POST':
        user_name = request.POST.get("user_name")
        password = request.POST.get("user_password")
        user_entry = user_validation.log_in_check_valid_entry(user_name, password)
        if user_entry:
            return HttpResponseRedirect(reverse('first_blog:user_home_page', kwargs={'user_name': user_name}))
        else:
            return render(request, 'first_blog/Log_In_Page.html', {'input_error': "Sorry, Invalid Input"})
    return render(request, 'first_blog/Log_In_Page.html')




