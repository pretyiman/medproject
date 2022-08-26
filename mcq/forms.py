from django import forms
from dal import autocomplete
from mcq.models import Subject, Topic, Question, Answers, Quiz, PublicMcq, PublicAnswers
from django_select2.forms import Select2MultipleWidget
from django.forms import formset_factory
from django.forms.models import inlineformset_factory, modelformset_factory
from django.contrib.auth.models import User
# django_select2.forms.Select2Mixin, django.forms.widgets.Select

class QuestionForm(forms.ModelForm):
    class  Meta:
        model = Question
        fields = ('subject', 'topic', 'desciption')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['topic'].queryset = Topic.objects.none()

        if 'subject' in self.data:
            try:
                subject_id = int(self.data.get('subject'))
                self.fields['topic'].queryset = Topic.objects.filter(
                    subject_id=subject_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['topic'].queryset = self.instance.subject.topic_set.order_by(
                'name')


      
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answers
        fields = ('option', 'is_true', 'explaination')


AnswerFormSet = inlineformset_factory(Question,Answers,form=AnswerForm, extra=4, max_num=4)



class PublicMcqForm(forms.ModelForm):
    class Meta:
        model = PublicMcq
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['topic'].queryset = Topic.objects.none()
        # self.fields['city'].queryset = City.objects.none()

        if 'subject' in self.data:
            try:
                subject_id = int(self.data.get('subject'))
                self.fields['topic'].queryset = Topic.objects.filter(
                    subject_id=subject_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['topic'].queryset = self.instance.subject.topic_set.order_by(
                'name')


# class OneLinerForm(forms.ModelForm):
#      class Meta:
#          model = OneLiner
#          fields= '__all__'

# trying to make view mcq_post view






# class PublicAnswersForm(forms.ModelForm):

    
#     class Meta:
#          model = PublicAnswers
#          fields = '__all__'

# class UserRegistrationForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput(
#         attrs={'placehlder':'Enter Passowrd Here....'}))
#     confirm_password = forms.CharField(widget=forms.PasswordInput(
#         attrs={'placehlder': 'Confirm Passowrd....'}))
#     class Meta:
#         model = User
#         fields =(
#             'username',
#             'first_name',
#             'last_name',
#             'email',
#         )

#     def clean_confirm_password(self):
#         password = self.cleaned_data.get('password')
#         confirm_password = self.cleaned_data.get('confirm_password')
#         if password != confirm_password:
#             raise forms.ValidationError("Password Mismatch")
#         return confirm_password





