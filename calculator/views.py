from django.shortcuts import render, redirect
from .models import Consumer
from .forms import ConsumerForm


def consumer_list(request):
    consumers = Consumer.objects.all()
    context = {'consumers': consumers}
    return render(request, 'calculator/list.html', context)


def add_consumer(request):
    if request.method == 'POST':
        form = ConsumerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consumer_list')
    else:
        form = ConsumerForm()
    return render(request, 'calculator/form.html', {'form': form})
