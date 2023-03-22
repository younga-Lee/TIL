from django.shortcuts import render

# Create your views here.
def first(request):
    third = request.GET.get('third')
    if third is None:
        third = 'nothing'
    
    context = {
        'third': third,
    }
    
    return render(request, 'throw_loops/first.html', context)

def second(request):
    one = request.GET.get('first')
    context = {
        'one' : one,
    }
    return render(request, 'throw_loops/second.html', context)

def third(request):
    two1 = request.GET.get('second')
    two2 = request.GET.get('second')
    two_list = [two1, two2]
    context = {
        'two_list' : two_list,
    }
    return render(request, 'throw_loops/third.html', context)
