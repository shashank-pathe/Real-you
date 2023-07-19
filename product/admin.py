from django.contrib import admin
from .models import *
from nested_admin import NestedModelAdmin, NestedTabularInline

class CategoryAttributeInline(admin.TabularInline):
    model = CategoryAttribute

class CategoryAdmin(admin.ModelAdmin):
    inlines = [CategoryAttributeInline]

class SpecificationsInline(NestedTabularInline):
    model = Specifications
    extra = 1

class VariantImageInline(NestedTabularInline):
    model = VariantImage
    extra = 1

class VariantInline(NestedTabularInline):
    model = Variant
    inlines = [VariantImageInline]
    extra = 1

class HighlightsInline(NestedTabularInline):
    model = Highlights
    extra = 1

class OfferInline(NestedTabularInline):
    model = Offer
    extra = 1

class ProductAdmin(NestedModelAdmin):
    inlines = [VariantInline, SpecificationsInline, HighlightsInline,OfferInline]

class VariantAdmin(NestedModelAdmin):
    inlines = [VariantImageInline]
    list_display = ('product','color')

class OfferAdmin(admin.ModelAdmin):
    list_display = ('product', 'discount', 'start_date', 'end_date')

admin.site.register(Product, ProductAdmin)
