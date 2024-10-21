# # #quizzerapp/views/organization.py

# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework.parsers import MultiPartParser, FormParser
# from ..models.organization import Organization
# from ..serializers.organization import OrganizationSerializer

# @api_view(['POST'])
# def add_organization(request):
#     serializer = OrganizationSerializer(data=request.data)
    
#     if serializer.is_valid():
#         organization = serializer.save()  # Save the organization
#         response_serializer = OrganizationSerializer(organization)  # Serialize to return
#         return Response(response_serializer.data, status=status.HTTP_201_CREATED)  # Return response
    
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if invalid


# @api_view(['GET'])
# def get_organizations(request):
#     organizations = Organization.objects.all()
#     serializer = OrganizationSerializer(organizations, many=True)
#     return Response(serializer.data)

# @api_view(['GET', 'PATCH', 'DELETE'])
# def organization_detail(request, pk):
#     try:
#         organization = Organization.objects.get(pk=pk)
#     except Organization.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = OrganizationSerializer(organization)
#         return Response(serializer.data)
    
#     elif request.method == 'PATCH':
#         serializer = OrganizationSerializer(organization, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         organization_name = organization.organization_name
#         organization.delete()
#         return Response({"message": f"{organization_name} removed successfully."}, status=status.HTTP_200_OK)

# #quizzerapp/views/organization.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from rest_framework.parsers import MultiPartParser, FormParser
from ..models.organization import Organization
from ..serializers.organization import OrganizationSerializer

@api_view(['POST'])
def add_organization(request):
    serializer = OrganizationSerializer(data=request.data)
    
    if serializer.is_valid():
        organization = serializer.save()  # Save the organization
        response_serializer = OrganizationSerializer(organization)  # Serialize to return
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)  # Return response
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if invalid


@api_view(['GET'])
def get_organizations(request):
    organizations = Organization.objects.all()
    serializer = OrganizationSerializer(organizations, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PATCH', 'DELETE'])
def organization_detail(request, pk):
    try:
        organization = Organization.objects.get(pk=pk)
    except Organization.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrganizationSerializer(organization)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = OrganizationSerializer(organization, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        organization_name = organization.organization_name
        # Delete the associated address if it exists
        if organization.address:
            organization.address.delete()
        organization.delete()  # Delete the organization itself
        return Response({"message": f"{organization_name} and its address removed successfully."}, status=status.HTTP_200_OK)
    try:
        organization = Organization.objects.get(pk=pk)
    except Organization.DoesNotExist:
        return Response({"error": "Organization not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # GET method: Return organization details
        serializer = OrganizationSerializer(organization)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        # PATCH method: Update organization details partially
        serializer = OrganizationSerializer(organization, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # DELETE method: Delete the organization and its associated address
        organization_name = organization.organization_name
        organization.delete()  # This will also delete the related Address due to on_delete=models.CASCADE
        return Response({"message": f"Organization '{organization_name}' and its address were deleted successfully."}, status=status.HTTP_200_OK)