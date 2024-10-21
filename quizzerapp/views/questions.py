# quizzerapp/views/question.py



# # Function-based view to handle form submission
# @api_view(['POST'])
# def add_question(request):
#     if request.method == 'POST':
#         form = QuestionAdminForm(request.POST)
#         if form.is_valid():
#             question = form.save()
#             serializer = QuestionSerializer(question)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


#utils

# # quizzerapp/views/question.py

# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from ..models.questions import Question
# from ..serializers.questions import QuestionSerializer
# from django.core.exceptions import ValidationError
# from ..utils.questions import validate_question_data  # Import your utility function

# class QuestionViewSet(viewsets.ModelViewSet):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer

#     def create(self, request, *args, **kwargs):
#         # Validate the incoming data
#         is_valid, validation_response = validate_question_data(request.data)
#         if not is_valid:
#             return Response(validation_response, status=status.HTTP_400_BAD_REQUEST)

#         # Proceed with serialization and saving
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         # Create a temporary Question instance for validation
#         question_instance = Question(**serializer.validated_data)

#         # Perform custom validation using model's `clean()` method
#         try:
#             question_instance.clean()
#         except ValidationError as e:
#             return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

#         # Save the validated data after passing clean() check
#         self.perform_create(serializer)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     def update(self, request, *args, **kwargs):
#         partial = kwargs.pop('partial', False)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=partial)
#         serializer.is_valid(raise_exception=True)

#         # Create a temporary Question instance for validation
#         question_instance = Question(**serializer.validated_data)

#         # Perform custom validation using model's `clean()` method
#         try:
#             question_instance.clean()
#         except ValidationError as e:
#             return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

#         self.perform_update(serializer)
#         return Response(serializer.data)

#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)

#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)

#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         self.perform_destroy(instance)
#         return Response(status=status.HTTP_204_NO_CONTENT)


# quizzerapp/views/question.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from ..models.questions import Question
from ..serializers.questions import QuestionSerializer
from django.core.exceptions import ValidationError
from ..utils.questions import validate_question_data  # Import your utility function

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def create(self, request, *args, **kwargs):
        # Validate the incoming data using utility function
        is_valid, validation_response = validate_question_data(request.data)
        if not is_valid:
            return Response(validation_response, status=status.HTTP_400_BAD_REQUEST)

        # Proceed with serialization and saving
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Create a temporary Question instance for validation
        question_instance = Question(**serializer.validated_data)

        # Perform custom validation using model's `clean()` method
        try:
            question_instance.clean()
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # Save the validated data after passing clean() check
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        # Validate the incoming data using utility function
        is_valid, validation_response = validate_question_data(request.data)
        if not is_valid:
            return Response(validation_response, status=status.HTTP_400_BAD_REQUEST)

        # Proceed with serialization and updating
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        # Create a temporary Question instance for validation
        question_instance = Question(**serializer.validated_data)

        # Perform custom validation using model's `clean()` method
        try:
            question_instance.clean()
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        self.perform_update(serializer)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

