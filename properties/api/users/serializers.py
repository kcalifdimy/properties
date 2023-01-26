from rest_framework import serializers
from .models import Profile, User




class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(required=False)



    class Meta:
        model = Profile
        fields = ('bio', 'photo', 'address', 'id', 'user')
        extra_kwargs = {'user': {'read_only': True}}  
        


class UserSerializer(serializers.ModelSerializer):
    #url = serializers.HyperlinkedRelatedField(view_name='user-detail')
   # url = serializers.HyperlinkedIdentityField(view_name="user")
    password2 = serializers.CharField(label='Confirm Password', write_only=True)
    profile = ProfileSerializer()




    def validate(self, data):
        password2 = data.pop('password2')
        password = data.get('password')
        if password != password2:
            raise serializers.ValidationError("Password does not match!")       
        if len(password) < 6:
           raise serializers.ValidationError("Password must be at least 6 characters")
        return data



    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user


    class Meta:
            model = User
            fields = ('password', 'password2','first_name', 'last_name', 'email', 'phone_number', 'type', 'id', 'profile',)
            extra_kwargs = {'password': {'write_only': True}, 'password2': {'write_only': True}, }  




class ProfileSerializer(serializers.ModelSerializer):
    #url = serializers.HyperlinkedRelatedField(view_name='user-detail')
   # url = serializers.HyperlinkedIdentityField(view_name="user")
    profile = ProfileSerializer()

    def update(self, instance, validated_data, uuid=None):

            instance.first_name = validated_data.get('first_name', instance.first_name)
            instance.last_name = validated_data.get('last_name', instance.last_name)
            instance.email = validated_data.get('email', instance.email)
            instance.phone_number = validated_data.get('phone_number', instance.phone_number)
            instance.type = validated_data.get('type', instance.type)

            instance.save()

            profile_data = validated_data.pop('profile')
            #print(profile_data)

            profile = Profile.objects.get(user=instance) # this will crash if the id is invalid though
            profile.bio = profile_data.get('bio', profile.bio)
            profile.photo = profile_data.get('photo', profile.photo)
            profile.address = profile_data.get('address', profile.address)
            profile.save()

            return instance


    class Meta:
            model = User
            fields = ('first_name', 'last_name', 'email', 'phone_number', 'type', 'id', 'profile',)


