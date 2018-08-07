from django.shortcuts import render
from django.utils import timezone
from .models import Story

# Create your views here.
def story_list(request):
    stories = Story.objects.order_by('created')
    return render(request,'blog/story_list.html',{'stories':stories})
