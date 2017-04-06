import os

from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.template.backends.utils import csrf_input
from django.templatetags.static import static

from comments.models import Comment
from php_template import render

class CommentForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
    name = forms.CharField(label='Your name', max_length=100)

def index(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment(message=form.cleaned_data['message'], name=form.cleaned_data['name']).save()
            return HttpResponseRedirect(request.get_full_path())
    else:
        form = CommentForm()

    return HttpResponse(render(
        template="%s/templates/comments/comments.php" % os.path.dirname(__file__),
        payload={
            "comments": list(Comment.objects.all().values()),
            "form": form.as_table(),
            "csrf_token": csrf_input(request),
            "css_path": static("comments/style.css")
        }
    ))
