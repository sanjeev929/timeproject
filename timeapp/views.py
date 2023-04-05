from django.shortcuts import render
from datetime import datetime
def index(request):
    timenow=str(datetime.today().strftime("%G-%m-%d %I:%M:%S %p"))
    context={'time1':timenow}
    return render(request,'index.html',context)
