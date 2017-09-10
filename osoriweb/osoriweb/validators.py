from __future__ import unicode_literals

from django.contrib.auth.password_validation import *
from django.utils.translation import ugettext as _


class CustomUserAttributeSimilarityValidator(UserAttributeSimilarityValidator):

    def validate(self, password, user=None):
        if not user:
            return

        for attribute_name in self.user_attributes:
            value = getattr(user, attribute_name, None)
            if not value or not isinstance(value, string_types):
                continue
            value_parts = re.split(r'\W+', value) + [value]
            for value_part in value_parts:
                if SequenceMatcher(a=password.lower(), b=value_part.lower()).quick_ratio() >= self.max_similarity:
                    try:
                        verbose_name = force_text(user._meta.get_field(attribute_name).verbose_name)
                    except FieldDoesNotExist:
                        verbose_name = attribute_name
                    raise ValidationError(
                        _("비밀번호는 %(verbose_name)s와 유사해서는 안됩니다"),
                        code='password_too_similar',
                        params={'verbose_name': verbose_name},
                    )

    def get_help_text(self):
        return _("개인정보를 통해 유추할 수 없는 비밀번호로 작성해주세요")


class CustomMinimumLengthValidator(MinimumLengthValidator):

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                _("비밀번호는 최소 %(min_length)d자 이상이어야 합니다"),
                code='password_too_short',
                params={'min_length': self.min_length},
            )

    def get_help_text(self):
        return _("비밀번호를 최소 %(min_length)d자 이상으로 작성해주세요" % {'min_length': self.min_length})


class CustomCommonPasswordValidator(CommonPasswordValidator):

    def validate(self, password, user=None):
        if password.lower().strip() in self.passwords:
            raise ValidationError(
                _("흔하게 사용되는 비밀번호는 사용할 수 없습니다"),
                code='password_too_common',
            )

    def get_help_text(self):
        return _("흔하게 사용되지 않는 비밀번호로 작성해주세요")


class CustomNumericPasswordValidator(NumericPasswordValidator):

    def validate(self, password, user=None):
        if password.isdigit():
            raise ValidationError(
                _("숫자로만 구성된 비밀번호는 사용할 수 없습니다"),
                code='password_entirely_numeric',
            )

    def get_help_text(self):
        return _("숫자 이외의 문자들과 함께 비밀번호를 작성해주세요")
