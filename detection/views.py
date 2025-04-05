from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Threat
from .serializers import ThreatSerializer
from .utils import send_threat_alert 

def create_threat(request):
    if request.method == "POST":             
        threat_type = request.POST.get("threat_type")
        severity = request.POST.get("severity")
        detected_at = request.POST.get("detected_at")

        new_threat = Threat.objects.create(threat_type=threat_type, severity=severity, detected_at=detected_at)

        # Notify Admins via Email
        admin_email = "morangaesther010@gmail.com" 
        send_threat_alert(admin_email, new_threat.threat_type, new_threat.severity, new_threat.detected_at)

        return JsonResponse({"message": "Threat created & email notification sent!"})


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def threat_list(request):
    """Fetches all threats (sorted by latest) or adds a new threat."""
    if request.method == "GET":
        threats = Threat.objects.all().order_by("-detected_at")
        serializer = ThreatSerializer(threats, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = ThreatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Threat added successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def threat_detail(request, pk):
    """Retrieve, update, or delete a specific threat by ID."""
    try:
        threat = Threat.objects.get(pk=pk)
    except Threat.DoesNotExist:
        return Response({"error": "Threat not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ThreatSerializer(threat)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = ThreatSerializer(threat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Threat updated successfully!"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        threat.delete()
        return Response({"message": "Threat deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)
