# quizzerapp/views/questionbank.py

# from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework import status
# from quizzerapp.models.questionbank import QuestionBank
# from quizzerapp.serializers.questionbank import QuestionBankSerializer
# from quizzerapp.models.questions import Question
# from django.shortcuts import get_object_or_404

# class QuestionBankViewSet(viewsets.ModelViewSet):
#     queryset = QuestionBank.objects.all()
#     serializer_class = QuestionBankSerializer

#     def list(self, request, *args, **kwargs):
#         """
#         Get all question banks with their details.
#         """
#         question_banks = self.get_queryset()
#         serializer = self.get_serializer(question_banks, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def retrieve(self, request, *args, **kwargs):
#         """
#         Get a specific question bank by ID, with questions grouped by question types.
#         """
#         question_bank = self.get_object()
#         serializer = self.get_serializer(question_bank)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def create(self, request, *args, **kwargs):
#         """
#         Override create method to handle many-to-many relationships (questions).
#         """
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         question_bank = serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     def update(self, request, *args, **kwargs):
#         """
#         Update a question bank by updating its name, description, and questions.
#         """
#         question_bank = self.get_object()

#         # Update all fields, including name, description, and questions
#         serializer = self.get_serializer(question_bank, data=request.data)
#         serializer.is_valid(raise_exception=True)

#         # Save the updated question bank
#         self.perform_update(serializer)

#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def partial_update(self, request, *args, **kwargs):
#         """
#         Partially update the question bank (add/remove questions without replacing all).
#         This endpoint can be used to either add or remove specific questions.
#         """
#         question_bank = self.get_object()
#         add_questions = request.data.get('add_questions', [])
#         remove_questions = request.data.get('remove_questions', [])

#         # Add questions if provided
#         if add_questions:
#             for question_id in add_questions:
#                 question = get_object_or_404(Question, id=question_id)
#                 question_bank.questions.add(question)
        
#         # Remove questions if provided
#         if remove_questions:
#             for question_id in remove_questions:
#                 question = get_object_or_404(Question, id=question_id)
#                 question_bank.questions.remove(question)

#         question_bank.save()

#         serializer = self.get_serializer(question_bank)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def destroy(self, request, *args, **kwargs):
#         """
#         Override destroy method to delete a question bank and return a custom message.
#         """
#         question_bank = self.get_object()
#         question_bank_name = question_bank.name  # Get the name of the question bank
#         self.perform_destroy(question_bank)  # Perform the deletion
#         return Response({'message': f'"{question_bank_name}"Question bank is deleted'}, status=status.HTTP_200_OK)



from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from quizzerapp.models.questionbank import QuestionBank
from quizzerapp.serializers.questionbank import QuestionBankSerializer
from quizzerapp.models.questions import Question
from django.shortcuts import get_object_or_404
from quizzerapp.utils.questionbank import validate_question_bank_name, validate_questions  # Import validation functions

class QuestionBankViewSet(viewsets.ModelViewSet):
    queryset = QuestionBank.objects.all()
    serializer_class = QuestionBankSerializer

    def list(self, request, *args, **kwargs):
        """
        Get all question banks with their details.
        """
        question_banks = self.get_queryset()
        serializer = self.get_serializer(question_banks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        """
        Get a specific question bank by ID, with questions grouped by question types.
        """
        question_bank = self.get_object()
        serializer = self.get_serializer(question_bank)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        """
        Override create method to handle many-to-many relationships (questions) and validate.
        """
        data = request.data

        # Validate name
        validate_question_bank_name(data.get('name'))

        # Validate questions
        validate_questions(data.get('questions', []))

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        question_bank = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        """
        Update a question bank by updating its name, description, and questions.
        """
        question_bank = self.get_object()

        # Validate updated name and questions
        data = request.data
        validate_question_bank_name(data.get('name'))
        validate_questions(data.get('questions', []))

        serializer = self.get_serializer(question_bank, data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        """
        Partially update the question bank (add/remove questions without replacing all).
        This endpoint can be used to either add or remove specific questions.
        """
        question_bank = self.get_object()
        add_questions = request.data.get('add_questions', [])
        remove_questions = request.data.get('remove_questions', [])

        if add_questions:
            validate_questions(add_questions)  # Validate before adding

            for question_id in add_questions:
                question = get_object_or_404(Question, id=question_id)
                question_bank.questions.add(question)

        if remove_questions:
            validate_questions(remove_questions)  # Validate before removing

            for question_id in remove_questions:
                question = get_object_or_404(Question, id=question_id)
                question_bank.questions.remove(question)

        question_bank.save()
        serializer = self.get_serializer(question_bank)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        """
        Override destroy method to delete a question bank and return a custom message.
        """
        question_bank = self.get_object()
        question_bank_name = question_bank.name  # Get the name of the question bank
        self.perform_destroy(question_bank)  # Perform the deletion
        return Response({'message': f'"{question_bank_name}"Question bank is deleted'}, status=status.HTTP_200_OK)
