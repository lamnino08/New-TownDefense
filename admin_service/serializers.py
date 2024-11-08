from rest_framework import serializers
from auth_service.models import Staff
from role_service.models import Role

class StaffUpdateSerializer(serializers.ModelSerializer):
    role_id = serializers.PrimaryKeyRelatedField(
        queryset=Role.objects.all(), source='role', write_only=True
    )

    class Meta:
        model = Staff
        fields = ['staff_id', 'username', 'name', 'phone_number', 'role_id', 'password']  # included all fields

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.name = validated_data.get('name', instance.name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.role = validated_data.get('role', instance.role)
        instance.password = validated_data.get('password', instance.password)  
        print(instance);
        instance.save()
        return instance
