from rest_framework import serializers

from pic_share20_api.models import Follow_users, Posts, Users


class UsersSerializer(serializers.ModelSerializer):
    follower = serializers.SerializerMethodField()
    followered = serializers.SerializerMethodField()

    class Meta:
        model = Users
        fields = "__all__"

    def get_follower(self, obj):
        return Follower_usersSerializer(obj.follower.all(), many=True).data

    def get_followered(self, obj):
        return Followerd_usersSerializer(obj.followered.all(), many=True).data


class PostUserSerializer(serializers.ModelSerializer):

    follower = serializers.SerializerMethodField()
    followered = serializers.SerializerMethodField()

    class Meta:
        model = Users
        fields = ("id", "username", 'profile_image',
                  'follower', 'followered')

    def get_follower(self, obj):
        return Follower_usersSerializer(obj.follower.all(), many=True).data

    def get_followered(self, obj):
        return Followerd_usersSerializer(obj.followered.all(), many=True).data


class PostsSerializer(serializers.ModelSerializer):
    users = PostUserSerializer(read_only=True)

    class Meta:
        model = Posts
        fields = "__all__"


class Follower_usersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Follow_users
        fields = ('id', 'follower_user',
                  'followered_user')


class Followerd_usersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Follow_users
        fields = ('id', 'follower_user',
                  'followered_user')
