from django import forms

from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'description',
            'price',
            'category'
        ]

class RawBookForm(forms.Form):
    title       = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your title'}))
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(attrs={
                                                'placeholder' : 'Your description',
                                                'rows' : 20,
                                                'cols': 12
                                            }
                                      )
                                  )
    price       = forms.DecimalField(initial=19.99)
    category    = forms.ChoiceField(
        choices=Book.CATEGORY_CHOICES
    )
    cover       = forms.ImageField(required=False)

    class Meta:
        model = Book
        fields = [
            'title',
            'description',
            'price',
            'category',
            'cover'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        blocked_phrases = ('admin', 'title', 'book')
        for phrase in blocked_phrases:
            if phrase in title:
                raise forms.ValidationError('Wrong title')
        else:
            return title