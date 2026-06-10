from django.contrib import admin
from .models import Post, UpdateNote, VideoTutorial, DynamicPage, HomePageContent

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')

@admin.register(UpdateNote)
class UpdateNoteAdmin(admin.ModelAdmin):
    list_display = ('system', 'version', 'date')
    list_filter = ('system', 'date')
    search_fields = ('details',)

@admin.register(VideoTutorial)
class VideoTutorialAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_title', 'created_at')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('short_title',)}

@admin.register(DynamicPage)
class DynamicPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(HomePageContent)
class HomePageContentAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Apenas permite adicionar se não existir nenhum
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)
