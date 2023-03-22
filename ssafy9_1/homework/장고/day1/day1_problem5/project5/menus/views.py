from django.shortcuts import render

# Create your views here.
def food(request):
    foods = ["피자","치킨","국밥","초밥", "민초흑당로제마라탕"]
    context = {
        'foods' : foods,
        'food' : food,
    }
    return render(request, 'menus/food.html', context)

def drink(request):
    drinks_list = ["cider","coke","miranda","fanta", "eye of finetree"]
    drinks = [d[0].upper() + d[1:] for d in drinks_list]
    
    context = {
        'drinks' : drinks,
    }
    return render(request, 'menus/drink.html', context)

def receipt(request):
    food = request.GET.get('food')
    drink = request.GET.get('drink')
    
    context = {
        'food' : food,
        'drink' : drink,
    }
    
    return render(request, 'menus/receipt.html', context)