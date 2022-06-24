from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post


class RegisterForm(UserCreationForm):
    # todo: we are adding a form to the default user creation form, because we want to show some custom stuffs 
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)

    
    
    # ? this is talking about what we are creating with the form 
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "password1", "password2"]
        
                
        
        # ! GETTING rid of the django helpertext
        # * [EXPLANATIONS] ===> the init method id taking in (self, *args, **kwargs)
    def __init__(self, *args, **kwargs):
        #  * so we are overwriting the whole funtionalities of that method
        super(RegisterForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'email', 'first_name', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            


# * this will allow us to create the instance of this form, and be able to pass it inside the [template] so we can render it there. 
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description"]