from django.shortcuts import render
from django.http import HttpResponse
from my_shop.models import Iteam
from math import ceil
def shop(request):
    prod=Iteam.objects.all()
    n=len(prod)
    num_slide=n//4+ceil((n/4)-(n//4))
    cat_list=[]
    cat_obj=Iteam.objects.values("category")
    cat_set={itm["category"] for itm in cat_obj}
    for i in cat_set:
        cat_itm=Iteam.objects.filter(category=i)
        cat_list.append([cat_itm,range(1,num_slide)])
    parm={"cat_list":cat_list}
    
    return render(request,"shop/shop.html",parm)

def product(request):

    return render(request,"shop/product.html")
 
    


