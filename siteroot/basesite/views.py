from django.shortcuts import render



# the view is returning data via a post request,
# so make it pay attention to the request method.
def index_view(request):
    return render(request, 'basesite/index.html')
