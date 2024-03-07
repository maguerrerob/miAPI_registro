from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario
from .serializers import UsuarioSerializer
from django.shortcuts import render
from django.http import JsonResponse

@api_view(['POST'])
def registro_usuario(request):
    if request.method == 'POST':
        username = request.data.get('username')
        if Usuario.objects.filter(username=username).exists():
            # El nombre de usuario ya está en uso
            return Response({'error': 'El nombre de usuario ya está en uso'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Crea el nuevo usuario
            serializer = UsuarioSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def lista_usuarios(request):
    # usuarios = Usuario.objects.all()
    # return render(request, 'registro/lista_usuarios.html', {'usuarios': usuarios})
    usuarios = Usuario.objects.all()
    serializer = UsuarioSerializer(usuarios, many=True)
    return JsonResponse(serializer.data, safe=False)


# class UsuarioRegistro(APIView):
#     def post(self, request):
#         serializer = UsuarioSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)