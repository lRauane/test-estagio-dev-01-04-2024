from django.shortcuts import render, redirect

import calculator_python
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

        # obter os dados
        consumption_month1 = int(request.POST.get('consumption1'))
        consumption_month2 = int(request.POST.get('consumption2'))
        consumption_month3 = int(request.POST.get('consumption3'))
        distributor_tax = float(request.POST.get('distributor_tax'))
        tax_type = request.POST.get("tax_type")

        calculation_result = calculator_python.calculator([consumption_month1, consumption_month2,consumption_month3], distributor_tax, tax_type)

        # Formatando os valores para exibir duas casas decimais
        annual_savings_formatted = "{:.2f}".format(calculation_result[0])
        monthly_savings_formatted = "{:.2f}".format(calculation_result[1])

        context = {'form': form, 'annual_savings': annual_savings_formatted,
                   'monthly_savings': monthly_savings_formatted,
                   'applied_discount': calculation_result[2],
                   'coverage': calculation_result[3]
        }

        return render(request, 'calculator/form.html', context)
    else:
        return render(request, 'calculator/form.html')
