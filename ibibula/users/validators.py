from django.core.exceptions import ValidationError

def validate_telegram(value):
    if not value.startswith('@'):
        raise ValidationError(
            'Telegram username must start with @',
            params={'value': value},
        )
