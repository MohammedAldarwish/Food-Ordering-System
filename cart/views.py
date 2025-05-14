from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Meals, Cart, CartItem
from .serializers import CartItemSerializers, CartSerializers

class CartViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
<<<<<<< HEAD
=======
        # التأكد من وجود الـ Cart وتهيئة الـ serializer
>>>>>>> 384d072cae553316b277c547a712ba2176ce2416
        if created:
            return Response({"message": "Cart created successfully."}, status=status.HTTP_201_CREATED)
        serializer = CartSerializers(cart)
        return Response(serializer.data)

class CartItemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CartItemSerializers

    def get_queryset(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        if cart:
            return CartItem.objects.filter(cart=cart)
<<<<<<< HEAD
        return CartItem.objects.none()  
=======
        return CartItem.objects.none()  # لو مافي Cart يرجع Empty Queryset
>>>>>>> 384d072cae553316b277c547a712ba2176ce2416
    
    def perform_create(self, serializer):
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        serializer.save(cart=cart)

    def destroy(self, request, *args, **kwargs):
<<<<<<< HEAD
=======
        # لو كان فيه CartItem يتم مسحه بشكل صحيح
>>>>>>> 384d072cae553316b277c547a712ba2176ce2416
        try:
            cart_item = self.get_object()
            cart_item.delete()
            return Response({"message": f"Item with id {cart_item.id} removed from cart."}, status=status.HTTP_204_NO_CONTENT)
        except CartItem.DoesNotExist:
            return Response({"message": "CartItem not found."}, status=status.HTTP_404_NOT_FOUND)
