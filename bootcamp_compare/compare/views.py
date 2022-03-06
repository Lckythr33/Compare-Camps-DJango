from tkinter.messagebox import NO
from django.shortcuts import render
from django.http import HttpResponse
from . models import Camp

# camps = [
#     {
#         'id' : '1',
#         'name': 'Coding Dojo',
#         'cost' : '$15,745',
#         'length' : '4 Months',
#         'languages' : 'Python/Java/React',
#         'etype' : 'Online/In-Person',
#         'erate' : '95.3%',
#         'internship' : 'No',
#         'loc' : 'Locations: Burbank,CA | Seattle, WA ',
#         'desc' : 'Not all Coding Bootcamps are Created Equal! Unlike many bootcamps that specialize in 1 stack in order to maximize class size and limit the learning difficulty, Coding Dojo’s 3-stack curriculum provides graduates with a complete skill set and, more importantly, the ability to easily learn new tech and programming languages they will be required to learn throughout their careers. Plain and simple: Our curriculum is designed to make this the first AND last bootcamp you ever attend.',
#     },

#     {
#         'id' : '2',
#         'name': 'Kenzie Academy',
#         'cost' : '$20,000',
#         'length' : '12 Months',
#         'languages' : 'Java',
#         'etype' : 'Online',
#         'erate' : '90%',
#         'internship' : 'No',
#         'loc' : 'Locations: Online Only',
#         'desc' : "Throughout the course, you'll participate in Kenzie Academy's Career Development program and will work with our Placement team. We'll provide you with the tools needed to empower you to land a job as an entry level software engineer, or to land a job in a tech-adjacent position. The goal of this program is to help you be job-ready for a career in tech.",
#     },
# ]



def home(request):
    context = {
        'camps' : Camp.objects.all()
    }
    return render(request, 'compare/index.html', context)