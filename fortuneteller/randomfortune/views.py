from django.shortcuts import render
import random

# Create your views here.
fortuneList = ['Good Luck','fortune','Try Again', 'Success', 'Wealth','Lesson']

def fortune(request):
    fortune = random.choice(fortuneList)
    context = {'fortune':fortune}
    return render(request, "randomfortune/fortune.html", context)