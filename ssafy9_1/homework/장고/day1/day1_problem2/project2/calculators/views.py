from django.shortcuts import render

# Create your views here.
def calculation(request):
    return render(request, 'calculators/calculation.html')

def result(request):
    first = request.GET.get('first')
    second = request.GET.get('second')
    minus = request.GET.get('second')
    context = {
        'first' : first,
        'second' : second,
        'minus' : -int(minus),
    }

    return render(request, 'calculators/result.html', context)
