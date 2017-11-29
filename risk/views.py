from django.http import JsonResponse

from risk.models import RiskValue

#import json
from django.db.models import Q


from django.shortcuts import render

def api(request, risk=None):
    if request.method == 'GET':
        if risk:
            obj = RiskValue.objects.filter(Q(entity__name='common') | Q(entity__name=risk))
            context = {'latest_question_list': obj}
            return render(request, 'api.json', context, content_type='application/json')
        else:
            return JsonResponse({'msg': 'Risk needs to be defined'})
    return JsonResponse({'msg': 'To be implemented'}, status=501)
