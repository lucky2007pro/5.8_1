from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Shop
from .serializers import ShopSerializer

@api_view(['GET', 'POST'])
def shop_list_create(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        if search:
            shops = Shop.objects.filter(name__icontains=search)
        else:
            shops = Shop.objects.all()
        serializer = ShopSerializer(shops, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def shop_detail_update_delete(request, pk):
    try:
        shop = Shop.objects.get(pk=pk)
    except Shop.DoesNotExist:
        return Response({'error': 'Shop topilmadi'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ShopSerializer(shop)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ShopSerializer(shop, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        shop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
