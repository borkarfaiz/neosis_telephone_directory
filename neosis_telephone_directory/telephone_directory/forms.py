from django.core.exceptions import ValidationError

from django.forms import ModelForm

from .models import Contacts


class PictureForm(ModelForm):

    def clean_profile_pic(self):
        image = self.cleaned_data.get('profile_pic')
        image_size = image.size
        if image:
            if image_size > 500*1024:
                raise ValidationError("Image file too large ( > 500kB )")
            return image
    class Meta:
        model = Contacts
        fields = [
        "first_name", "middle_name", "last_name", "email", "mobile_number",
        "landline_number", "notes", "profile_pic"
        ]
