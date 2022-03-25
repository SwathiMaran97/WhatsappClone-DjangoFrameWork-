from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

# chat/views.py
from django.shortcuts import render
from .models import ChatGroup

def index(request):
    return render(request, 'chat/index.html', {})

def get_participants(group_id=None, group_obj=None, user=None):
    """ function to get all participants that belong the specific group """
    
    if group_id:
        chatgroup = ChatGroup.objects.get(id=id)
    else:
        chatgroup = group_obj

    temp_participants = []
    for participants in chatgroup.user_set.values_list('username', flat=True):
        if participants != user:
            temp_participants.append(participants.title())
    temp_participants.append('You')
    return ', '.join(temp_participants)


def room(request, group_id):
    if request.user.groups.filter(id=group_id).exists():
        chatgroup = ChatGroup.objects.get(id=group_id)
        #TODO: make sure user assigned to existing group
        assigned_groups = list(request.user.groups.values_list('id', flat=True))
        groups_participated = ChatGroup.objects.filter(id__in=assigned_groups)
        return render(request, 'chat/room.html', {
            'chatgroup': chatgroup,
            'participants': get_participants(group_obj=chatgroup, user=request.user.username),
            'groups_participated': groups_participated
        })
    else:
        return HttpResponseRedirect(reverse("chat:unauthorized"))

def unauthorized(request):
    return render(request, 'chat/unauthorized.html', {})