from django.shortcuts import render
from testapp.models import Group

def index(request):
    groups = Group.objects.all()
    return render(request, 'index.html', {'groups': groups})