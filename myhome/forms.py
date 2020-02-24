

from django import forms

YEARS = [x for x in range(1940, 2021)]

FRUIT_CHOICES = [
    ('select', 'select'),
    ('orange', 'Oranges'),
    ('mangoe', 'Mangoes'),
    ('apple', 'Apples'),
    ('grape', 'Grapes'),

]

GENDER = [
    ('male', 'Male'),
    ('female', 'Female'),
]

TEST_CHOICES = [
    ('Math', 'Math'),
    ('Biology', 'Biology'),
    ('Physics', 'Physics'),
    ('Botany', 'Botany'),
]


class SignIn(forms.Form):
    fname = forms.CharField(label='Enter your first name', max_length=100)
    lname = forms.CharField(label='Enter your last name', max_length=100)
    email = forms.EmailField(label='Enter your email', max_length=100)
    state = forms.CharField(label='Enter your state', max_length=100)
    birth_date = forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget(years=YEARS))
    favorite_fruit = forms.CharField(label='What is your favorite fruit?',
                                     widget=forms.Select(choices=FRUIT_CHOICES))
    gender = forms.CharField(label='Select your gender', widget=forms.RadioSelect(choices=GENDER))
    # gender = forms.CharField(label='Select your gender  ',widget=forms.Select(choices=GENDER))
    test = forms.MultipleChoiceField(label="Select your subject", choices=TEST_CHOICES,
                                     widget=forms.CheckboxSelectMultiple())
