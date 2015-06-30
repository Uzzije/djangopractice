from django import forms

class UserSignUpForm(forms.Form):
        name = forms.CharField(label='User Name',max_length=100)
        email = forms.CharField(label='Email', max_length=100)
        password = forms.CharField(label='Password', widget=forms.PasswordInput())
        verify_password = forms.CharField(label='Verify Password', widget=forms.PasswordInput())

        def clean(self):
            cleaned_data = super(UserSignUpForm, self).clean()
            user_password = self.cleaned_data.get('password')
            user_verify_password = self.cleaned_data.get('verify_password')
            if (user_password and user_verify_password) and user_password != user_verify_password:
                msg = "Passwords does not match"
                self.add_error('password', msg)

class NewBlogEntryForm(forms.Form):
        subject = forms.CharField(label='Subject', max_length=100, required=True)
        body = forms.CharField(label='Body', widget=forms.Textarea(attrs={'rows':40, 'cols':60}))


class LogInForm(forms.Form):
    my_default_errors = {
        'required': 'Make sure username and password are correct',
        'invalid': 'Make sure username and password are correct'
    }
    name = forms.CharField(label='User Name', max_length=100, error_messages=my_default_errors)
    password = forms.CharField(label='Password', widget=forms.PasswordInput(), error_messages=my_default_errors)
