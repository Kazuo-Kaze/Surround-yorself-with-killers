from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmailForm, MailMessageForm
from django.contrib import messages
from django.core.mail import send_mail
from django_pandas.io import read_frame
from .models import UserEmail
from django.template.loader import render_to_string
# Create your views here.
from .models import MailMessage
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def frontpage(request):
    form = EmailForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks for Subscribing')
            form = EmailForm()
        else:
            form = EmailForm()

    posts = MailMessage.objects.all()
    

    context = {
        'form': form,
        'posts': posts,
    }


    return render(request, "core/frontpage.html", context);


def loginView(request):
    return render(request, "core/login.html")


@login_required
def mail_letter(request):
    emails = UserEmail.objects.all()
    df = read_frame(emails, fieldnames=['email'])
    mail_list = df['email'].values.tolist()
    if request.method == 'POST':
        form = MailMessageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # slug = form.cleaned_data.get('slug')
            # slug.replace(" ", "")
            # print(slug)
            # form.save()
            title = form.cleaned_data.get('title')
            first_para = form.cleaned_data.get('first_para')
            second_para = form.cleaned_data.get('second_para')
            third_para = form.cleaned_data.get('third_para')
            fourth_para = form.cleaned_data.get('fourth_para')
            fifth_para = form.cleaned_data.get('fifth_para')
            ctx = {
                'first_para': first_para,
                'second_para': second_para,
                'third_para': third_para,
                'fourth_para': fourth_para,
                'fifth_para': fifth_para,
            }
            message = render_to_string('core/mail.html', ctx)
            send_mail(
                title,
                message,
                '',
                mail_list,
                fail_silently=False,
                html_message=message,
            )
            messages.success(request, 'Message has been sent to the Subscribers')
            return redirect('mail_letter')
    else:
        form = MailMessageForm()
        
    context = {
        'form': form,
    }
    return render(request, 'core/mail_letter.html', context)



def search(request):
    form = EmailForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks for Subscribing')
            form = EmailForm()
        else:
            form = EmailForm()

    query = request.GET.get('query', '')

    posts = MailMessage.objects.filter(Q(title__icontains=query) | Q(first_para__icontains=query))

    return render(request, 'core/search.html', {'posts': posts, 'query': query, 'form': form})



def detailPage(request, slug):
    form = EmailForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks for Subscribing')
            form = EmailForm()
        else:
            form = EmailForm()

    post = get_object_or_404(MailMessage, slug=slug)
    return render(request, "core/detail.html", { 'post': post, 'form': form})