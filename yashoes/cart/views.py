from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from yashoes.cart.serilizer import CartSerializer, CartSerializer1
from yashoes.model.user_variant import UserVariant

success_response = {'message': 'success'}


class UserVariantView(APIView):
    @staticmethod
    def post(request):
        user_id = request.user.id
        variant_id = request.data.get('variant_id')
        quantity = request.data.get('quantity')
        data = {'user': user_id, 'variant': variant_id, 'quantity': quantity}
        try:
            user_variant = UserVariant.objects.get(
                variant__pk=variant_id, user__pk=user_id)
            serializer = CartSerializer(user_variant, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=success_response, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except UserVariant.DoesNotExist:
            serializer = CartSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=success_response, status=status.HTTP_200_OK)
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request):
        user_id = request.user.id
        variant_id = request.data.get('variant_id')
        user_variant = UserVariant.objects.filter(
            variant__pk=variant_id).filter(user__pk=user_id)
        if user_variant:
            user_variant.delete()
            return Response(data=success_response, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class Cart(viewsets.ViewSet):
    @staticmethod
    def list(request):
        user_id = request.user.id
        queryset = UserVariant.objects.filter(user__pk=user_id).values(
            'variant_id', 'variant__product__name', 'variant__price', 'variant__quantity',
            'variant__price', 'variant__color', 'variant__size', 'variant__image_link'
        )
        serializer = CartSerializer1(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, url_path='information', url_name='information')
    def total_cart(self, request):
        user_id = request.user.id
        total = UserVariant.objects.filter(user__pk=user_id, deleted_at=None).count()
        return Response(data={'total': total, }, status=status.HTTP_200_OK)
