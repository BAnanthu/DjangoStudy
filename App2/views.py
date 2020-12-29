from django.shortcuts import render

# Create your views here.
def app2(request):
    try:
        return render(request, "App2/app2.html",{'data': request.session['name']})
    except KeyError:
        pass
    return render(request, "App2/app2.html")
