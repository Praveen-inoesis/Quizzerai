# # quizzerapp/serializers/organization.py

# from rest_framework import serializers
# from ..models.organization import Organization, Address  


# class AddressSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Address
#         fields = ['street', 'city', 'state', 'country', 'postal_code', 'phone_number']

# class OrganizationSerializer(serializers.ModelSerializer):
#     address = AddressSerializer()
   
#     class Meta:
#         model = Organization
#         fields = ['organization_name', 'organization_id', 'domain_name', 'admin_email', 'created_at', 'updated_at', 'disable',  'logo', 'address']

#     def create(self, validated_data):
#         address_data = validated_data.pop('address')
#         address = Address.objects.create(**address_data)
#         organization = Organization.objects.create(address=address, **validated_data)
#         return organization

#     def update(self, instance, validated_data):
#         address_data = validated_data.pop('address')
#         address = instance.address

#         instance.organization_name = validated_data.get('organization_name', instance.organization_name)
#         instance.domain_name = validated_data.get('domain_name', instance.domain_name)
#         instance.admin_email = validated_data.get('admin_email', instance.admin_email)
#         instance.disable = validated_data.get('disable', instance.disable)
#         instance.logo = validated_data.get('logo', instance.logo)
#         instance.save()

#         address.street = address_data.get('street', address.street)
#         address.city = address_data.get('city', address.city)
#         address.state = address_data.get('state', address.state)
#         address.country = address_data.get('country', address.country)
#         address.postal_code = address_data.get('postal_code', address.postal_code)
#         address.phone_number = address_data.get('phone_number', address.phone_number)
#         address.save()

#         return instance


# quizzerapp/serializers/organization.py

from rest_framework import serializers
from ..models.organization import Organization, Address  


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['street', 'city', 'state', 'country', 'postal_code', 'phone_number']

class OrganizationSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
   
    class Meta:
        model = Organization
        fields = ['organization_name', 'organization_id', 'domain_name', 'admin_email', 'created_at', 'updated_at', 'disable',  'logo', 'address']

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)
        organization = Organization.objects.create(address=address, **validated_data)
        return organization

    def update(self, instance, validated_data):
        address_data = validated_data.pop('address')
        address = instance.address

        instance.organization_name = validated_data.get('organization_name', instance.organization_name)
        instance.domain_name = validated_data.get('domain_name', instance.domain_name)
        instance.admin_email = validated_data.get('admin_email', instance.admin_email)
        instance.disable = validated_data.get('disable', instance.disable)
        instance.logo = validated_data.get('logo', instance.logo)
        instance.save()

        address.street = address_data.get('street', address.street)
        address.city = address_data.get('city', address.city)
        address.state = address_data.get('state', address.state)
        address.country = address_data.get('country', address.country)
        address.postal_code = address_data.get('postal_code', address.postal_code)
        address.phone_number = address_data.get('phone_number', address.phone_number)
        address.save()

        return instance


