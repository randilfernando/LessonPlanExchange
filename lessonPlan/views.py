from django.shortcuts import render

def landing(request):
    return render(request, 'lessonPlan/home-page.html')

def add_lesson(request):
    return render(request, 'lessonPlan/add-plan.html', {
        "mediums": ['Sinhala', 'English', 'Tamil'],
        "grades": [6,7,8,9,10,11],
        "days": [1,2,3,4,5,6,7],
        "topics": ['How be a millionaire', 'What to do man', 'Hello brother', 'Brother from another mother']
    })

def browse_by_subject(request):
    return render(request, 'lessonPlan/browse-by-subject.html')
