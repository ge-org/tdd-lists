from django.shortcuts import redirect, render
from lists.models import Item


def home_page(request):
    if 'POST' == request.method:
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    return render(request, 'home.html')
