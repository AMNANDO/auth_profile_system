from rest_framework import serializers
from .models import Account
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')

        def validate_age(self, value):
            if value < 18 :
                raise serializers.ValidationError('you can`t create account with underage value!')
            return value

        def validate_update(self,attrs):
            if self.instace and not self.instace.is_active:
                raise serializers.ValidationError('cannot update inactive account!')
            return attrs

        def create(self, validated_data):
            request=self.context.get('request')
            validated_data['user']=request.user
            return super().create(validated_data)

        def update(self, instance, validated_data):
            validated_data.pop('age', None)
            validated_data.pop('is_active', None)
            return super().update(instance, validated_data)