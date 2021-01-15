from django.forms import ModelForm, TextInput
from .models import City_list


class City_list_form(ModelForm):
    class Meta:
        model = City_list
        fields = ['city_name']

        # here when i use {{form.city_name}} in index.html it create a new input box.but i already used a bootstrap
        # input form.so now make 2 input form into 1 we have to use widgets. attrs is the html attribute like class,placeholder etc
        widgets = {'city_name': TextInput(
            attrs={'class': 'input', 'placeholder': 'Add city name'})}
