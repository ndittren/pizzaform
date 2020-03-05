from django.shortcuts import render
from .forms import PizzaForm

def home(request):
    return render(request, 'pizza/home.html')

def order(request):
    if request.method == 'POST':
        filledform = PizzaForm(request.POST)
        if filledform.is_valid():
            note = 'Thanks for ordering! Your %s %s and %s pizza is on its way!' %(filledform.cleaned_data['size'], filledform.cleaned_data['topping1'], filledform.cleaned_data['topping2'], )
            new_form = PizzaForm()
            return render(request, 'pizza/order.html', {'pizzaform': new_form, 'note': note})
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'pizzaform': form})
