from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=40)
    from_email = forms.EmailField(required=True, max_length=200)
    message = forms.CharField(required=True, max_length=2000, widget=forms.Textarea, help_text='Your message goes here')

def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Name:"
        self.fields['from_email'].label = "Email:"
        self.fields['message'].label = "What can we help you with?"

def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        from_email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not from_email and not message:
            raise forms.ValidationError('You have to write something')