# from rest_framework import serializers
# from .models import Usuario

# class UsuarioSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Usuario
#         fields = ['username', 'correo_electronico', 'pais', 'password1','password2']

#     def create(self, validated_data):
#         usuario = Usuario.objects.create_user(
#             username=validated_data['username'],
#             correo_electronico=validated_data['correo_electronico'],
#             pais=validated_data.get('pais'),
#             password1=validated_data['password1'],
#             password2=validated_data['password2']
#         )
#         return usuario


"""
        {
    "nombre": "Ejemplo",
    "apellidos": "Apellido",
    "correo_electronico": "ejemplo@example.com",
    "pais": "Ejemplo",
    "password1": "contraseña123",
    "password2": "contraseña123"
}

"""

from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ['username', 'correo_electronico', 'pais', 'password', 'password2']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        password2 = validated_data.pop('password2')

        if password != password2:
            raise serializers.ValidationError("Las contraseñas no coinciden")

        user = Usuario(**validated_data)
        user.set_password(password)
        user.save()
        return user
