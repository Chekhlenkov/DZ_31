from rest_framework.fields import BooleanField
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer
from ads.models import Ad, Category, Selection
from ads.validators import check_published
from users.models import User
from users.serializers import UserDetailSerializer


class AdSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Ad


class AdListSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field="username", queryset=User.objects.all())
    category = SlugRelatedField(slug_field="name", queryset=Category.objects.all())

    class Meta:
        fields = "__all__"
        model = Ad


class AdCreateSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field="username", queryset=User.objects.all())
    category = SlugRelatedField(slug_field="name", queryset=Category.objects.all())
    is_published = BooleanField(validators=[check_published], required=False)

    class Meta:
        fields = "__all__"
        model = Ad


class AdDetailSerializer(ModelSerializer):
    author = UserDetailSerializer()
    category = SlugRelatedField(slug_field="name", queryset=Category.objects.all())

    class Meta:
        fields = "__all__"
        model = Ad


class CatSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Category


class SelectionDetailSerializer(ModelSerializer):
    items = AdSerializer(many=True)

    class Meta:
        fields = "__all__"
        model = Selection


class SelectionSerializer(ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Selection


class SelectionListSerializer(ModelSerializer):
    owner = SlugRelatedField(slug_field="username", queryset=User.objects.all())

    class Meta:
        fields = ["owner", "name"]
        model = Selection


class SelectionCreateSerializer(ModelSerializer):
    owner = SlugRelatedField(slug_field="username", read_only=True)
    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["owner"] = request.user
        return super().create(validated_data)

    class Meta:
        fields = "__all__"
        model = Selection