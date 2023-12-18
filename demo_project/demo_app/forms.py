from django import forms

from demo_app.models import Person, Course


class PersonCreationForm(forms.ModelForm):
    MATERIAL_CHOICES = [
        ('debit_note_book', 'Debit Note Book'),
        ('pen', 'Pen'),
        ('exam_papers', 'Exam Papers'),
        # Add more choices as needed
    ]

    materials = forms.MultipleChoiceField(
        choices=MATERIAL_CHOICES,
        widget=forms.CheckboxSelectMultiple,
    )
    class Meta:
        model = Person
        fields = '__all__'

    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=Person.GENDER_CHOICES)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('country'))
                self.fields['course'].queryset = Course.objects.filter(course_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.country.city_set.order_by('name')