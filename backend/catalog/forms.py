from django import forms
from store.models import Book, Publisher, Author, Genre


class BookForm(forms.ModelForm):
    author = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False,
        label='Автори',
    )

    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False,
        label='Жанри'
    )

    class Meta:
        model = Book
        fields = ['name', 'isbn', 'price', 'publisher',
                  'author', 'genres', 'image']
        widgets = {
            'publisher': forms.Select(),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['author'].label_from_instance = lambda obj: f"{obj.first_name} {obj.last_name}"
        self.fields['genres'].label_from_instance = lambda obj: obj.name

        if self.instance and self.instance.pk:
            self.fields['genres'].initial = self.instance.genres.values_list(
                'pk', flat=True)

    def save(self, commit=True):
        book = super().save(commit=False)
        if commit:
            book.save()
            self.save_m2m()
            book.genres.set(self.cleaned_data['genres'])
        return book