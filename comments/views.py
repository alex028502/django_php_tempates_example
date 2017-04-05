import os

from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.template.backends.utils import csrf_input

from comments.models import Comment
from php_template import render

class CommentForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    message = forms.CharField(widget=forms.Textarea)

def index(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment(comment=form.cleaned_data['message'], name=form.cleaned_data['name']).save()
            return HttpResponseRedirect(request.get_full_path())
    else:
        form = CommentForm()

    comments = list(Comment.objects.all().values())

    csrf_token = csrf_input(request)

    return HttpResponse(render(
        template=os.path.join(os.path.dirname(__file__), 'templates/comments/comments.php'),
        payload={"comments": comments, "form": str(form), "csrf_token": csrf_token}
    ))
