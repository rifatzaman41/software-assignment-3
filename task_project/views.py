from django.shortcuts import render
from add_category.models import TaskCategory

def home(request):
   data=TaskCategory.objects.all()
  # print(data)
  # for i in data:
  #    print(i.category_name)
  #    for j in i.tasks.all():
    #     print(j)
     #    print()
   return render(request,'index.html',{'data':data}) 
