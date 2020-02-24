from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from myhome.forms import SignIn


class HomePageView(TemplateView):
    template_name = 'home.html'


def signin(request):
    form = SignIn

    if request.method == 'POST':
        form = SignIn(request.POST)

        # print(form.is_valid())
        if form.is_valid():

            # print(form.cleaned_data)
            # name = request.POST.get('name')

            return render(request, 'login_page.html', {'form': form,
                                                  'fname': form.cleaned_data['fname'],
                                                  'lname': form.cleaned_data['lname'],
                                                  'email': form.cleaned_data['email'],
                                                  'birth_date': form.cleaned_data['birth_date'],
                                                  'favorite_fruit': form.cleaned_data['favorite_fruit'],
                                                  'gender': form.cleaned_data['gender'],
                                                  'test': form.cleaned_data['test'],
                                                  'state': form.cleaned_data['state'],
                                                  })
        else:
            form = SignIn()
    return render(request, 'login_page.html', {'form': form});
