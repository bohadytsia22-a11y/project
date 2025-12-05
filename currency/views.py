from django.shortcuts import render
from .services import get_rate, get_all_currencies

def converter(request):
    result = None
    currencies = get_all_currencies()

    if request.method == "POST":
        amount = float(request.POST.get("amount"))
        from_currency = request.POST.get("from_currency")
        to_currency = request.POST.get("to_currency")

        rate_from = get_rate(from_currency)
        rate_to = get_rate(to_currency)
        result = amount * rate_from / rate_to

    return render(request, "currency/converter.html", {
        "result": result,
        "currencies": currencies
    })
