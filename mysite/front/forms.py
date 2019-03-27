from django import forms

class choiceform(forms.Form):
    loc = forms.ChoiceField(label = "Location", choices = ( \
                                        ('NA', 'Select'),\
                                        ('UK','United Kingdom'),\
                                        ('US','United States')))


    stud = forms.ChoiceField(label = "Number of Students", choices = ( \
                                        ('any', 'Select'),\
                                        ('small','< 5,000'),\
                                        ('med','5,000 - 15,000'),\
                                        ('large','> 15,000')))


    tuit = forms.ChoiceField(label = "Tuition", choices = ( \
                                        ('all', 'Select'),\
                                        ('less','< $15,000'),\
                                        ('midless','$15,000 - $30,000'),\
                                        ('midmore','$30,000-$45,000'),\
                                        ('more', '> $45,000')))

    def process(self):
        location = self.cleaned_data
