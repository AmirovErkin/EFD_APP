from django.shortcuts import render, redirect
from .forms import UserForm
# Create your views here.


def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UserForm()

    return render(request, 'create_file.html', {'form': form})

def success(request):
    return render(request, 'create_file.html')