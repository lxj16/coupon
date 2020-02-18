from django import forms

class PromoCodeApplyForm(forms.Form):
    promoCode = forms.CharField()