from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render

from risk.models import RiskValue

def api(request, risk=None):
    if request.method == 'GET':
        if risk:
            # retieve all common and 'risk' defined RiskValue entries
            vals = RiskValue.objects.filter(Q(entity__name='common') | Q(entity__name=risk))
            context = {'entries': vals}
            return render(request, 'api.json', context, content_type='application/json')
        else:
            return JsonResponse({'msg': 'Risk needs to be defined'})
    return JsonResponse({'msg': 'To be implemented'}, status=501)
