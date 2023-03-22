from django import forms


class CartAddProductForm(forms.Form):
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class CartDeleteProductForm(forms.Form):
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
