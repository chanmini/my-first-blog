from django.shortcuts import render
from django.http import JsonResponse

def keyboard(request):
	return JsonResponse(
		{
		'type': 'buttons',
		'buttons': ['학식','내일의 학식','도서관']
		}
	)