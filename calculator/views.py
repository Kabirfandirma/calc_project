from django.shortcuts import render
from datetime import datetime

def calculator_view(request):
    result = None

    if request.method == 'POST':
        try:
            num1 = float(request.POST.get('num1'))
            num2 = float(request.POST.get('num2'))
            operation = request.POST.get('operation')

            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                result = num1 / num2
            else:
                result = 'Invalid operation'
        except:
            result = 'Error: Invalid input'

    return render(request, 'calculator/index.html', {
    'result': result,
    'now': datetime.now().year
})
