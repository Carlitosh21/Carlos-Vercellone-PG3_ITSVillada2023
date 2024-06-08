from django.shortcuts import render
import requests
from django.http import HttpResponse



def api_view(request):
    
    if request.method == 'POST':
        C1 = request.POST.get('currency1')
        C2 = request.POST.get('currency2')
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        
        
        
        if C1 is not None and C2 is not None and amount is not None and date is not None:
            url = f"https://api.apilayer.com/fixer/convert?to={C2}&from={C1}&amount={amount}&date={date}"
            
            payload = {}
            headers= {
                "apikey": "B9P0C6J1guwq8lFRCTfIMR7VStBlsRpU"
            }
            
            response = requests.request("GET", url, headers=headers, data = payload)
            if response.status_code == 200:
                data = response.json()
                context = {'data': data}
                return render(request, 'proyecto1/template1.html', context)
            else:
                return HttpResponse(f"Error: {response.status_code}")  
            
        if C1 is not None and C2 is not None and amount is not None:
            url = f"https://api.apilayer.com/fixer/convert?to={C2}&from={C1}&amount={amount}"
            
            payload = {}
            headers= {
                "apikey": "B9P0C6J1guwq8lFRCTfIMR7VStBlsRpU"
            }
            
            response = requests.request("GET", url, headers=headers, data = payload)
            if response.status_code == 200:
                data = response.json()
                context = {'data': data}
                return render(request, 'proyecto1/template1.html', context)
            else:
                return HttpResponse(f"Error: {response.status_code}")  
               
        
        else:
            return HttpResponse(f"Error: Id o recurso Invalido") 
    else:
        return render(request, 'proyecto1/template1.html')
    

