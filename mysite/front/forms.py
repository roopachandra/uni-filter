from django import forms

class choiceform(forms.Form):
    loc = forms.ChoiceField(label = "Location", choices = ( \
                                        ('UK','Scotland'),\
                                        ('US','United States'),\
                                        ('WA','Wales')))


    deg = forms.ChoiceField(label = "Degree level", choices = ( \
                                        ('XyZ','BSc'),\
                                        ('YzX','MSc'),\
                                        ('ZxY','Phd')))


    sub = forms.ChoiceField(label = "Subject", choices = ( \
                                        ('AbC','Informatics'),\
                                        ('BcA','Physics'),\
                                        ('CaB','Chemistry')))

    def process(self):
        location = self.cleaned_data
