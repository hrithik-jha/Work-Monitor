from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Meeting

def home(request):
    return render(request, 'meetings/home.html')



@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['meet_date'] and request.POST['agenda'] and request.POST['venue']:
            meeting = Meeting()
            meeting.title = request.POST['title']
            meeting.meet_date = request.POST['meet_date']
            meeting.agenda = request.POST['agenda']
            meeting.venue = request.POST['venue']
            #strn = meeting.title[0:2]# + meeting.venue[0:2]
            meeting.url = 0
            meeting.attendance = 0
            meeting.member = request.user
            meeting.save()
            #urln += 1
            #print(urln)

            return redirect('/meetings/' + str(meeting.id))

        else:
            return render(request, 'meetings/create.html', {'error': 'All fields are required.'})
    else:
        return render(request, 'meetings/create.html')

def detail(request, meeting_id):
    meeting = get_object_or_404(Meeting, pk = meeting_id)
    return render(request, 'meetings/detail.html', {'meeting': meeting})