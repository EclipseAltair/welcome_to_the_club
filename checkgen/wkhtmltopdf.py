# -*- coding: utf-8 -*-
from base64 import b64encode
import requests

from django.template.loader import render_to_string

from .models import Check 


def generate_pdf(check_type, check_id, check_path, order):
    if check_type == 'kitchen':
        order['check_type'] = 'kitchen'    # добавление в json check_type
        html_like_string = render_to_string('checkgen/kitchen_check.html', {'order': order})
    else:
        order['check_type'] = 'client'
        html_like_string = render_to_string('checkgen/client_check.html', {'order': order})
    
    html_like_bytes = b64encode(bytes(html_like_string, encoding='UTF-8')).decode('UTF-8')  # преобразование
 
    response = requests.post('http://localhost:8001', json={'contents': html_like_bytes})  # запрос к wkhtmltopdf

    Check.objects.filter(id=check_id).update(status='rendered')
    
    with open(check_path, 'wb') as f:
        f.write(response.content)
