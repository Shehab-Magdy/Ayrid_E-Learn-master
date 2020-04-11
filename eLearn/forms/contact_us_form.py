from django import forms

class ContactUsForm (forms.Form):
    firstName = forms.CharField(max_length=60, required=True, label='First Name', help_text='Type Your First Name',error_messages={'required':'Please type yor first name to simplify the communication'})
    lastName = forms.CharField(max_length=60, label='Last Name', help_text='Type Your Last Name',error_messages={'required':'Please type yor last name to simplify the communication'})
    email = forms.EmailField(required=True, label='E-mail', help_text='Type Your Email Here',error_messages={'required':'Provide a correct email address'})
    message = forms.CharField(widget=forms.Textarea, max_length=200,required=True,help_text='Enter your message here',label='Message')
