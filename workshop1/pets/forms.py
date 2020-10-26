from django import forms


class PetCreateForm(forms.Form):
    DOG = "Dog"
    CAT = 'cat'
    PARROT = 'parrot'
    UNKNOWN = 'Unknown'

    PET_TYPES = [
        (DOG, 'Dog'),
        (CAT, 'Cat'),
        (PARROT, 'Parrot'),
        (UNKNOWN, 'Unknown')
    ]

    type = forms.ChoiceField(choices=PET_TYPES)
    name = forms.CharField(max_length=6, required=True)
    age = forms.IntegerField(required=True, min_value=1, max_value=101)
    description = forms.CharField(widget=forms.Textarea, max_length=100, required=False)
    image_url = forms.URLField(required=True)
    # username_id = forms.IntegerField(required=True)
    # username_id.widget.build_attrs({'class': 'col-12', 'name': 'username_id', 'value': })
    # username_id = forms.CharField(widget=forms.HiddenInput())
    # username_id.widget.build_attrs({'value': 'request.user_id'})
    name.widget.attrs.update({'class': 'col-12', 'name': 'name'})
    age.widget.attrs.update({'class': 'col-12', 'name': 'age'})
    image_url.widget.attrs.update({'class': 'col-12', 'name': 'image'})
    description.widget.attrs.update({'class': 'col-12', 'name': 'description'})
    type.widget.attrs.update({'class': 'col-12', 'name': 'type'})