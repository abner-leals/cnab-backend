from rest_framework import generics, views
from .serializers import FileSerializer
from .serializers import TransactionSerializer, StoreNameSerializer
from .models import Transaction, TransactionType
from django.shortcuts import get_object_or_404
import pandas as pd


class CreateTransaction(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = FileSerializer

    def post(self, request, *args, **kwargs):
        file = request.FILES["file"]
        datas = []
        transactions = []

        for line in file:
            line = line.decode("utf-8")
            line_replaced = line.replace("\n", "").replace(" ", "")
            if len(line_replaced) == 0:
                ...
            else:
                type = get_object_or_404(TransactionType, id=int(line[0:1]))

                datas.append(
                    {
                        "type": type,
                        "day": f"{line[1:5]}-{line[5:7]}-{line[7:9]}",
                        "value": float(line[9:19]) / 100,
                        "cpf": int(line[19:30]),
                        "card": line[30:42],
                        "hour": f"{line[42:44]}:{line[44:46]}:{line[46:48]}",
                        "owner": line[48:62],
                        "store": line[62:81].strip(" \n"),
                    }
                )

        for data in datas:

            serializer = TransactionSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save(type=data["type"])

            trans = Transaction.objects.filter(**serializer.validated_data)
            trye = TransactionSerializer(trans[0])
            transactions.append(trye.data)

        return views.Response(transactions)


class ListBalance(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = StoreNameSerializer

    def post(self, request):

        transactions = Transaction.objects.filter(
            store__icontains=request.data["store"]
        )
        saida = 0
        entrada = 0
        for item in transactions:
            if item.type.nature == "Entrada":
                entrada += item.value
            else:
                saida += item.value

        return views.Response(
            {
                "store": request.data["store"],
                "entrada": entrada,
                "saida": saida,
                "saldo": entrada - saida,
            },
        )
