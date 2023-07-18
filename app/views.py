from django.shortcuts import render

# Create your views here.
def user_defined_filters(request):
    d={'data':'siVa Is a soFtWARE developeR','krish':'Krishna Is a soFtWARE developeR'}






    return render(request,'user_defined_filters.html',context=d)