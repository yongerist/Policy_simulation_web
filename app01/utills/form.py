from app01 import models
from app01.utills.bootstrap import BootStrapModelForm


class UserModelForm(BootStrapModelForm):
    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "age", "account", "create_time", "depart", "gender"]
