"""Formularios de contacto y de solicitud de demo.

Antispam sin dependencias: honeypot (campo oculto ``website``) + time-trap
(campo ``iniciado`` con la marca de tiempo de carga del formulario).
"""
import time

from django import forms

from core.models import ContactMessage

MIN_SECONDS = 2          # más rápido que esto = bot
MAX_SECONDS = 60 * 60    # más lento que esto = sesión caducada / bot lento


class _AntispamMixin(forms.ModelForm):
    website = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"tabindex": "-1", "autocomplete": "off", "class": "hp-field"}
        ),
        label="No rellenes este campo",
    )
    iniciado = forms.CharField(required=False, widget=forms.HiddenInput())

    consentimiento = forms.BooleanField(
        required=True,
        label="He leído y acepto la política de privacidad.",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not (self.is_bound and self.data.get("iniciado")):
            self.fields["iniciado"].initial = str(int(time.time()))

    def clean_website(self):
        if self.cleaned_data.get("website"):
            raise forms.ValidationError("Envío no válido.")
        return ""

    def clean_iniciado(self):
        raw = self.cleaned_data.get("iniciado") or ""
        try:
            started = int(raw)
        except (TypeError, ValueError):
            return raw
        elapsed = time.time() - started
        if elapsed < MIN_SECONDS or elapsed > MAX_SECONDS:
            raise forms.ValidationError("El formulario ha caducado. Vuelve a enviarlo.")
        return raw


class ContactForm(_AntispamMixin):
    class Meta:
        model = ContactMessage
        fields = ["nombre", "email", "empresa", "mensaje"]
        widgets = {
            "nombre": forms.TextInput(attrs={"autocomplete": "name"}),
            "email": forms.EmailInput(attrs={"autocomplete": "email"}),
            "empresa": forms.TextInput(attrs={"autocomplete": "organization"}),
            "mensaje": forms.Textarea(attrs={"rows": 5}),
        }
        labels = {
            "nombre": "Nombre y apellidos",
            "email": "Correo electrónico",
            "empresa": "Inmobiliaria o empresa",
            "mensaje": "¿En qué podemos ayudarte?",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["empresa"].required = False
        self.fields["mensaje"].required = True

    def save(self, commit=True):
        obj = super().save(commit=False)
        obj.origen = ContactMessage.ORIGIN_CONTACT
        if commit:
            obj.save()
        return obj


class DemoForm(_AntispamMixin):
    class Meta:
        model = ContactMessage
        fields = ["nombre", "email", "empresa", "num_agentes", "num_oficinas", "mensaje"]
        widgets = {
            "nombre": forms.TextInput(attrs={"autocomplete": "name"}),
            "email": forms.EmailInput(attrs={"autocomplete": "email"}),
            "empresa": forms.TextInput(attrs={"autocomplete": "organization"}),
            "num_agentes": forms.TextInput(attrs={"inputmode": "numeric"}),
            "num_oficinas": forms.TextInput(attrs={"inputmode": "numeric"}),
            "mensaje": forms.Textarea(attrs={"rows": 4}),
        }
        labels = {
            "nombre": "Nombre y apellidos",
            "email": "Email de trabajo",
            "empresa": "Nombre de la agencia",
            "num_agentes": "Nº de agentes",
            "num_oficinas": "Nº de oficinas",
            "mensaje": "Necesidad específica (opcional)",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["empresa"].required = False
        self.fields["mensaje"].required = False
        self.fields["num_agentes"].required = False
        self.fields["num_oficinas"].required = False

    def save(self, commit=True):
        obj = super().save(commit=False)
        obj.origen = ContactMessage.ORIGIN_DEMO
        if commit:
            obj.save()
        return obj
