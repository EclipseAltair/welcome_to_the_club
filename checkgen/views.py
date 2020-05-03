# -*- coding: utf-8 -*-
import os
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from smena_test.settings import BASE_DIR
from .models import Check, Printer


@csrf_exempt    # исключение из CSRF-проверки для CORS
def create_checks(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        try:
            body_data = json.loads(body_unicode)
        except json.JSONDecodeError:
            response = JsonResponse({"error": "Invalid JSON"})
            response.status_code = 400
            return response
        
        if Check.objects.filter(order__id=body_data['id']).count() != 0:    # если заказ с таким id уже есть в БД
            response = JsonResponse({"error": "Для данного заказа уже созданы чеки"})
            response.status_code = 400
            return response
        
        if Printer.objects.filter(point_id=body_data['point_id']).count() == 0:    # если у точки нет принтера
            response = JsonResponse({"error": "Для данной точки не настроено ни одного принтера"})
            response.status_code = 400
            return response

        kitchen_printers = Printer.objects.filter(point_id=body_data['point_id'], check_type='kitchen')
        for kitchen_printer in kitchen_printers:
            kitchen_path = os.path.join(BASE_DIR, f'media/pdf/{body_data["id"]}_{"kitchen"}')
            kitchen_check = Check.objects.create(printer_id=kitchen_printer, type='kitchen', order=body_data,
                                                 status='new', pdf_file=kitchen_path)
    
        client_printers = Printer.objects.filter(point_id=body_data['point_id'], check_type='client')
        for client_printer in client_printers:
            client_path = os.path.join(BASE_DIR, f'media/pdf/{body_data["id"]}_{"client"}')
            client_check = Check.objects.create(printer_id=client_printer, type='client', order=body_data, 
                                                status='new', pdf_file=client_path)
        
        response = JsonResponse({"ok": "Чеки успешно созданы"})
        response.status_code = 200
        return response
    
    response = JsonResponse({"error": "Method Not Allowed"})
    response.status_code = 405
    return response
        

def new_checks(request):
    return JsonResponse({})


def check(request):
    return JsonResponse({})
