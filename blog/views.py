from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Story

# Create your views here.
def story_list(request):
    stories = Story.objects.order_by('created')
    return render(request,'blog/story_list.html',{'stories':stories})

def story_detail(request, pk):
    story = get_object_or_404(Story, pk=pk)
    return render(request, 'blog/story_detail.html',{'story': story})
