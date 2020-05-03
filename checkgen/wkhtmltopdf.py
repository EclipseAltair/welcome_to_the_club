# -*- coding: utf-8 -*-
from base64 import b64encode

from django.template.loader import render_to_string


def pdf_generate(check_type, check_id, order):
    if check_type == 'kitchen':
        order['check_type'] = 'kitchen'
        html_like_string = render_to_string('checkgen/kitchen_check.html', {'order': order})
        
    elif check_type == 'client':
        order['check_type'] = 'client'
        html_like_string = render_to_string('checkgen/client_check.html', {'order': order})
