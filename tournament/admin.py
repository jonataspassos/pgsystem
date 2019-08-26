from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Tournament)
admin.site.register(Test)

admin.site.register(Proposition)
admin.site.register(IntegerProposition)
admin.site.register(TextProposition)
admin.site.register(FloatProposition)
admin.site.register(BooleanProposition)
admin.site.register(GroupProposition)

admin.site.register(Question)
admin.site.register(MultipleChoiceQuestion)
admin.site.register(TrueOrFalseQuestion)
admin.site.register(OpenQuestion)
admin.site.register(SumTypeQuestion)
admin.site.register(ManyPropositionQuestion)
admin.site.register(GroupQuestion)

admin.site.register(UserResponse)