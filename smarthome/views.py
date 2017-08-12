from django.shortcuts import render
# Create your views here.


def index(request):
    # test
    if request.method =='POST':
        data = request.POST
    else:
        data = request.GET
    print(data)
    return render(request, 'index.html', {'data': data})




