from django.shortcuts import render

# Create your views here.
def app(request):
    request.session['name']="ananthu"
    request.session.set_expiry(20)
    try:
        return render(request,"App/app.html",{'data': request.session['name']})
    except:
        pass
    return render(request, "App/app.html")