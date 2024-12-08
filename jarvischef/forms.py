from django import forms

class ReciepeForm(forms.Form):
    reciepe_message = forms.CharField(max_length=255, 
                                      widget=forms.TextInput(attrs={'placeholder':'Ask your reciepe'}))
