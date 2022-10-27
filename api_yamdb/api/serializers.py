from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
import re

from reviews.models import Category, Comment, Genre, Review, Title, User


class RegisterDataSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField()

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                'Имя пользователя "me" не разрешено.')
        if not re.match('^[a-zA-Z0-9_@+-._]{5,150}$', value):
            raise serializers.ValidationError(
                'Имя пользователя должно содержать от 5 до 150 символов, '
                'может состоять из латинских букв или цифр, '
                'может содержать символы @ + - . _ '
            )

        return value


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField()


class ReviewSerializer(serializers.ModelSerializer):
    title = serializers.SlugRelatedField(slug_field='name', read_only=True)
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    def validate(self, ser_data):
        author = None
        request = self.context.get('request')

        if request and hasattr(request, 'user'):
            author = request.user

        title_id = self.context.get('view').kwargs.get('title_id')
        title = get_object_or_404(Title, pk=title_id)

        if (request.method == 'POST' and Review.objects.filter(
                title=title, author=author).exists()):
            raise serializers.ValidationError(
                'Можно оставить только один отзыв')

        return ser_data

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'pub_date', 'score', 'title')


class CommentSerializer(serializers.ModelSerializer):
    review = serializers.SlugRelatedField(slug_field='text', read_only=True)
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date', 'review')
        extra_kwargs = {'text': {'required': True}}


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ('id', )


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        exclude = ('id', )


class TitleSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(slug_field='slug',
                                         many=True,
                                         queryset=Genre.objects.all())
    category = serializers.SlugRelatedField(slug_field='slug',
                                            queryset=Category.objects.all())

    class Meta:
        model = Title
        fields = '__all__'


class TitlesReadSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False, required=True)
    genre = GenreSerializer(many=True, required=False)
    rating = serializers.IntegerField(read_only=True, required=False)

    class Meta:
        model = Title
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())],
        required=True,
    )
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        fields = ("username", "email", "first_name", "last_name", "bio",
                  "role")
        model = User


class UserEditSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ("username", "email", "first_name", "last_name", "bio",
                  "role")
        model = User
        read_only_fields = ('role', )
