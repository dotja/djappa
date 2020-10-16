from django.shortcuts import render
from .models import MyTable

def home(request):
	recs = MyTable.objects.all()
	return render(request, 'home.html', {'db_rec': recs})

