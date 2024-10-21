#quizzerapp/admin.py

from django.contrib import admin
from .models.organization import Organization, Address
from .models.questiontype import QuestionType 

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('organization_name', 'organization_id', 'get_phone_number', 'admin_email', 'created_at', 'updated_at', 'disable')

    def get_phone_number(self, obj):
        return obj.address.phone_number if obj.address else "No address"
    get_phone_number.short_description = 'Phone Number'

admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Address)


@admin.register(QuestionType)
class QuestionTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'question_type_code', 'description')
    search_fields = ('title','question_type_code',)
    ordering = ('id',)
    list_filter = ('question_type_code',)

    # You can define any fields to show in the form (optional)
    fields = ['title','question_type_code', 'description']

    # You can customize the form validation or save process if needed
    def save_model(self, request, obj, form, change):
        obj.save()

    # Add logic for deleting
    def delete_model(self, request, obj):
        obj.delete()



# quizzerapp/admin.py

from django.contrib import admin
from .models.questions import Question
from .models.questiontype import QuestionType
from .forms import QuestionAdminForm

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    form = QuestionAdminForm
    list_display = ('id', 'question_text', 'question_type')  
    search_fields = ('question_text', 'question_type__question_type_code')  
    ordering = ('id',)
    list_filter = ('question_type',)

    # Specify the fields to show in the form
    fieldsets = (
        (None, {
            'fields': ('question_type', 'question_text')
        }),
        ('Multiple Choice (MCQ)', {
            'fields': ('choice_1', 'choice_2', 'choice_3', 'choice_4', 'correct_answer'),
            'classes': ('collapse',),  
        }),
        ('Match the Following (MTF)', {
            'fields': ('mtf_item_pairs',),
            'classes': ('collapse',),
        }),
    )

    def mtf_item_pairs(self, obj):
        """Display the item pairs for match the following questions in the admin."""
        if hasattr(obj, 'match_the_following'):
            return "\n".join(f"{key}: {value}" for key, value in obj.match_the_following.items())
        return "No pairs defined"

    mtf_item_pairs.short_description = 'Match Item Pairs'

    # Customize the save behavior
    def save_model(self, request, obj, form, change):
        obj.save()

    # Customize the delete behavior
    def delete_model(self, request, obj):
        obj.delete()





