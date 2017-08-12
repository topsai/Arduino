from django.shortcuts import render
# Create your views here.
post = []
get = []
def index(request):
    # test
    if request.method =='POST':
        data = request.POST
        post.append(data)
    else:
        data = request.GET
        get.append(data)
    return render(request, 'index.html', {'post': post, 'get': get})




