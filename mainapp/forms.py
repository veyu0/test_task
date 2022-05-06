from django import forms

from mainapp.models import Cats


class CatsForm(forms.ModelForm):
    class Meta:
        model = Cats
        fields = ['name', 'age', 'breed', 'photo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CreationCatsForm(forms.ModelForm):
    class Meta:
        model = Cats
        fields = ['name', 'age', 'breed', 'photo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# class CatsEditForm(forms.ModelForm):
#     class Meta:
#         model = Cats
#         fields = ['name', 'age', 'breed', 'photo']
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)