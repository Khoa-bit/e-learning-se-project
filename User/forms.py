from django import forms


class PasswordResetForm(forms.Form):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    # add morjor field when implemented
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    confirm_password = forms.CharField(
        max_length=50, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(PasswordResetForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
        return cleaned_data
