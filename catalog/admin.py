from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

# admin.site.register(Book)
# admin.site.register(BookInstance)
# admin.site.register(Author)
admin.site.register(Genre)

# Inline bookInstance editor to be placed in the book editor
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

# Inline book editor to be placed in the author editor
class BooksInLine(admin.TabularInline):
    model = Book

# Define the admin class
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

    inlines = [BooksInLine]


# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

    inlines = [BooksInstanceInline]


# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'id', 'status', 'due_back')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )