from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomeUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email','first_name','last_name',)    # 사용자이름도 추가해야됨