from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, QRUserLink
from .serializers import UserSerializer, QRUserLinkSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication


class GetUserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        name = request.query_params.get('name')
        mobile = request.query_params.get('mobile')
        user_id = request.query_params.get('id')
        qr_unique_id = request.query_params.get('qr_unique_id')

        if name:
            users = User.objects.filter(name__icontains=name)
            if users.exists():
                serializer = UserSerializer(users, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        elif mobile:
            user = User.objects.filter(mobile=mobile).first()
        elif user_id:
            user = User.objects.filter(id=user_id).first()
        elif qr_unique_id:
            qr_link = QRUserLink.objects.filter(qr_unique_id=qr_unique_id).first()
            if qr_link:
                return Response(UserSerializer(qr_link.user).data, status=status.HTTP_200_OK)
            return Response({"error": "QR ID not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Provide 'name', 'mobile', 'id', or 'qr_unique_id' query parameter"}, status=status.HTTP_400_BAD_REQUEST)
        
        if user:
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    
class SearchUserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        name = request.query_params.get('name')
        mobile = request.query_params.get('mobile')
        qr_unique_id = request.query_params.get('qr_unique_id')

        if name:
            users = User.objects.filter(name__icontains=name)
        elif mobile:
            users = User.objects.filter(mobile=mobile)
        elif qr_unique_id:
            qr_link = QRUserLink.objects.filter(qr_unique_id=qr_unique_id).first()
            if qr_link:
                return Response(UserSerializer(qr_link.user).data, status=status.HTTP_200_OK)
            return Response({"error": "QR ID not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Provide 'name', 'mobile', or 'qr_unique_id' as query parameter"}, status=status.HTTP_400_BAD_REQUEST)

        if users.exists():
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)


class CreateQRUserLinkView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    def post(self, request):
        user_data = request.data.get('user')
        qr_unique_id = request.data.get('qr_unique_id')

        if not user_data or not qr_unique_id:
            return Response({"error": "User details and QR unique ID are required"}, status=status.HTTP_400_BAD_REQUEST)
        
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            qr_link = QRUserLink.objects.create(user=user, qr_unique_id=qr_unique_id)
            qr_link_serializer = QRUserLinkSerializer(qr_link)
            return Response(qr_link_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetUserByQRIDView(APIView):
    def get(self, request, qr_unique_id):
        qr_link = QRUserLink.objects.filter(qr_unique_id=qr_unique_id).first()
        if qr_link:
            serializer = UserSerializer(qr_link.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "QR ID not found"}, status=status.HTTP_404_NOT_FOUND)
