from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Order, OrderItem
from .serializers import OrderSerializer
from cart.models import Cart
from rest_framework import status


class CheckoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        cart = Cart.objects.get(user=request.user)
        
        address = request.data.get('address')

        if not address:
            return Response({"error": "Address is required"}, status=status.HTTP_400_BAD_REQUEST)
 

        
        order = Order.objects.create(
            user = request.user,
            total_price = cart.total_price,
            address = request.data.get('address'),
            restaurant = cart.items.first().meal.restaurant
        )


            # Add each item in the cart to the order
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                meal=item.meal,
                quantity=item.quantity,
                price=item.total_price,
            )
            cart.items.all().delete()
        
        # Serialize the order data
        serializer = OrderSerializer(order)
        
        return Response(serializer.data, status=201)