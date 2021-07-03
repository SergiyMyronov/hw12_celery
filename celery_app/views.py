from celery_app.forms import TaskForm
from celery_app.tasks import send_mail as celery_send_mail

from django.contrib import messages
from django.shortcuts import render


def index(request):

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            subject = 'Celery test'
            from_email = 'sergemk@entecheco.com'
            recipient_list = [form.cleaned_data['email']]
            due_date = form.cleaned_data['date']
            message = form.cleaned_data['text']
            celery_send_mail.apply_async((subject, message, from_email, recipient_list), eta=due_date)
            messages.add_message(request, messages.SUCCESS, 'Message sent')
    else:
        form = TaskForm()

    return render(request, 'celery_app/task.html', {'form': form})
