from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Meeting

def home(request):
    
    query = request.GET.get("q")
    meets = Meeting.objects
    if query:
        meets = meets.filter(title__icontains=query)
        
    return render(request, 'meetings/home.html', {'meets':meets})



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

def attend(request, meeting_id):
    if request.method == 'POST':    
        meeting = get_object_or_404(Meeting, pk = meeting_id)
        meeting.attendance += 1
        meeting.save()
        return redirect('/meetings/' + str(meeting.id))