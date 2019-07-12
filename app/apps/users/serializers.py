from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    locations = serializers.PrimaryKeyRelatedField(many=True, queryset=Location.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'locations')
