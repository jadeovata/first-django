from django.shortcuts import render

# Create your views here.
def story_list(request):
    return render(request,'blog/story_list.html',{})
