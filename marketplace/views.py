from django.shortcuts import render


def post_list(request):

    return render(request, 'marketplace/post_list.html',{})
    

