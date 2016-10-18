from django.shortcuts import render, redirect
from .models import Email

# Create your views here.
def index(request):
    return render(request, 'emailvalidation/index.html')

def validate(request):
    if request.method == 'POST':
        email = Email.objects.validate(request.POST['email'])
        if 'error' in email:
            context = {
                'message': email['error']
            }
            return render(request, 'emailvalidation/index.html', context)
        if 'success' in email:
            context = {
                'message': email['success'],
                'emails': Email.objects.all()
            }
            return render(request, 'emailvalidation/success.html', context)
    else:
        return redirect(index)

#not sure if  should be doing a delete with a GET request...
def delete(request, id):
    print('Deleting email with id: {}'.format(id))
    Email.objects.filter(id=id).delete()
    return redirect(index)
