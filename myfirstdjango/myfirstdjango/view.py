# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 14:57:14 2020

@author: 90463
"""

from django.shortcuts import render
 
def mymain(request):
    
    return render(request, 'main.html')

