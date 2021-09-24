from core.models import Account
from rest_framework import viewsets
from core.serializers import AccountSerializer


class AccountViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
