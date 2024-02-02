from django import forms

from grades.models import Assigment, Grade
from schedule.models import Lesson

class CreateAssigment(forms.Form):
    def __init__(self, teacher, *args, **kwargs):
        super(CreateAssigment, self).__init__(*args, **kwargs)
        self.fields['lesson'].queryset = Lesson.objects.filter(teacher_id=teacher)

    WEIGHT_CHOICES = ((1, 1), (1.5, 1.5), (2, 2), (2.5, 2.5), (3, 3), (3.5, 3.5), (4, 4), (4.5, 4.5), (5, 5), (5.5, 5.5), (6, 6))

    # Tylko te lekcje, do których przypisany jest aktualnie
    # zalogowany nauczyciel
    lesson = forms.ModelChoiceField(queryset=Lesson.objects.all(),
        label='Wybierz klasę',
        empty_label='Wybierz klasę',
        required=False,
        widget=forms.Select(attrs={'placeholder': 'Klasa', 'class': 'form-control'}))
    name = forms.CharField(max_length=200, label='nazwa', 
                widget=forms.TextInput(attrs={'placeholder': 'nazwa', 'class': 'form-control'}))
    weight = forms.ChoiceField(label='Waga oceny',
                choices=WEIGHT_CHOICES,
                widget=forms.Select(attrs={'placeholder': 'Waga oceny', 'class': 'form-control'}))

class ContactForm(forms.Form):
    
    title = forms.CharField(
        max_length=64,
        widget=forms.TextInput(attrs={'placeholder': 'Tytuł', 'class': 'form-control'}))
    body = forms.CharField(
        max_length=512,
        widget=forms.Textarea(attrs={'placeholder': 'Tytuł', 'class': 'form-control'}))

# class GradeForm(forms.Form):
#     GRADE_CHOICES = ((1, 1), (1.5, 1.5), (2, 2), (2.5, 2.5), (3, 3), (3.5, 3.5), (4, 4), (4.5, 4.5), (5, 5), (5.5, 5.5), (6, 6))

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for assigment_id in self.initial.get('assigment_ids', []):
#             field_name = f'grade_{assigment_id}'
#             self.fields[field_name] = forms.ChoiceField(
#                 label='Ocena',
#                 choices=self.GRADE_CHOICES,
#                 required=False,
#                 widget=forms.Select(attrs={'class': 'form-control'})
#             )
    