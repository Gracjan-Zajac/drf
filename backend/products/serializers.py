from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product
from . import validators


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail", lookup_field="pk")
    edit_url = serializers.SerializerMethodField(read_only=True)
    delete_url = serializers.SerializerMethodField(read_only=True)
    # email = serializers.EmailField(write_only=True)
    title = serializers.CharField(
        validators=[validators.validate_title_no_hello, validators.uniqe_product_title])

    class Meta:
        model = Product
        fields = [
            'pk',
            # 'user',
            'title',
            # 'email',
            'content',
            'price',
            'sale_price',
            'my_discount',
            'url',
            'edit_url',
            'delete_url',
        ]

    # def create(self, validated_data):
    #     email = validated_data.pop("email")
    #     print(email)
    #     obj = super().create(validated_data)
    #     return obj

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit", kwargs={'pk': obj.pk}, request=request)

    def get_delete_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-delete", kwargs={'pk': obj.pk}, request=request)

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
