from django import forms


class RegistrationForm(forms.Form):

    username=forms.CharField()

    password=forms.CharField()

    email=forms.EmailField()



class BmrForm(forms.Form):

    height=forms.IntegerField()

    weight=forms.IntegerField()

    age=forms.IntegerField()

    options=(
        ("male","male"),
        ("female","female")
    )

    gender=forms.ChoiceField(choices=options)

    choices=(
        (1,"Sedentary"),
        (2,"lightlyActive"),
        (3,"ModeractivlyActive"),
        (4,"VeryActive"),
        (5,"ExtraActive")
    )


    activity_level=forms.ChoiceField(choices=choices)












class TemparatureForm(forms.Form):

    temp_in_deg=forms.IntegerField(required=False)

    temp_in_fh=forms.IntegerField(required=False)


    



class EmiForm(forms.Form):

    amount=forms.IntegerField()
    
    interest=forms.IntegerField()

    tenure=forms.IntegerField()