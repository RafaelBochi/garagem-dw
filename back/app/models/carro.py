from django.db import models

class Carro(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.ForeignKey("Marca", on_delete=models.CASCADE)
    cor = models.ForeignKey("Cor", on_delete=models.CASCADE)
    acessorio = models.ForeignKey("Acessorio", on_delete=models.CASCADE)
    categoria = models.ForeignKey("Categoria", on_delete=models.CASCADE)
    pic = models.ForeignKey("CarPic", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.nome} - {self.marca}"