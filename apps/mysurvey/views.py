from django.shortcuts import render, HttpResponse, redirect

#if using messages be sure to import and possibly terminal stuff for sessions
from django.contrib import messages


def index(request):
    return render(request, 'mysurvey/index.html')


def process(request):
    if request.method == "POST":
        print "post it is"
        request.session['fullform'] = request.POST
        
        # try:
        #     request.session['count'] += 1
        # except:
        #     request.session['count'] = 1
        # I think the if statement below is better than the try above

        if 'count' in request.session:
            request.session['count'] += 1
        else:
            request.session['count'] = 1
        print request.session['fullform']
        print request.session['fullform']['yourname']
        print request.POST
        
        messages.success(request, 'Thanks for submitting this form! You have subitted this form ' + str(request.session['count']) + ' times now.')
        return redirect('/result')


def result(request):
    return render(request, 'mysurvey/result.html')


# def goback(request):

#     return redirect('/')

def reset(request):
    try:
        del request.session['count']
        # request.session['count'] = 0
    # this try except is needed just in case the key doesn't exist! Also don't need both del count and count = 0 choose one.
        return redirect('/')
    except:
        return redirect('/')
