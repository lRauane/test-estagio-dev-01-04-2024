from django.shortcuts import render, redirect
from .models import Consumer, DiscountRule

def consumer_list(request):
    consumers = Consumer.objects.all()
    for consumer in consumers:
        discount_rule = DiscountRule.objects.filter(consumer_type=consumer.consumer_type,
                                                    consumption_range=consumer.consumption_range).first()
        if discount_rule:
            consumer.annual_savings = consumer.consumption * consumer.distributor_tax * discount_rule.discount_value
    return render(request, 'list.html', {'consumers': consumers})

def add_consumer():
    if request.method == 'POST':
        form = ConsumerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consumer_list')
    else:
        form = ConsumerForm()
    return render(request, 'form.html', {'form': form})
