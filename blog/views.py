from django.shortcuts import render
# render is a function which we will be using..

# Create your views here.
def post_list(request):
    return(render(request,'blog/post_list.html',{}))
