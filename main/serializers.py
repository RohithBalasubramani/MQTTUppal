from rest_framework import serializers
from django.apps import apps
from django.db import models

app_models = apps.get_app_config('main').get_models()

for model in app_models:
    fields_dict = {field.name: field for field in model._meta.fields if isinstance(field, models.DateTimeField)}

    class Meta:
        model = model
        fields = '__all__'

    for field_name, field in fields_dict.items():
        if hasattr(field, 'format'):  # Check if the field supports format setting
            field.format = "%Y-%m-%d %H:%M:%S"  # Set the desired date format for DateTimeField

    serializer_class = type(
        f"{model.__name__}Serializer",
        (serializers.ModelSerializer,),
        {"Meta": Meta}
    )

    locals()[f"{model.__name__}Serializer"] = serializer_class
