from django.shortcuts import render, redirect

def index(request):
    return render(request, 'survey/index.html')

def process(request):
    if request.method == 'POST':
        request.session['first'] = request.POST['html_first']
        request.session['last'] = request.POST['html_last']
        request.session['location'] = request.POST['html_location']
        request.session['favorite'] = request.POST['html_favorite']
        request.session['comments'] = request.POST['html_comments']
        return redirect('/result')
    else:
        return redirect('/')

def result(request):
    return render(request, 'survey/result.html')
   
