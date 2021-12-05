from django.db import models
from django.db.models.fields import DateField

class Usuario(models.Model):
    ESTADO_CIVIL = (
        ('Solteiro', 'S'),
        ('Casado', 'C'),
        ('Divorciado', 'D'),
    )
    S_N = (
        ('Sim - Sim', 'S - S'),
        ('Sim - Não', 'S - N'),
        ('Não - Sim', 'N - S'),
    )
    IdUsuarios = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=100)
    Email = models.CharField(max_length=50)
    Senha = models.CharField(max_length=20)
    Estado = models.CharField(max_length=80)
    Data_de_Nascimento = models.DateField()
    Telefone = models.CharField(max_length=20)
    Estado_Civil = models.CharField(max_length=10, choices=ESTADO_CIVIL)
    Chef_e_ou_Cliente = models.CharField(max_length=9, choices=S_N)
    Itens_Comprados = models.IntegerField()


class Receitas(models.Model):
    IdReceitas = models.AutoField(primary_key=True)
    Receitas = models.CharField(max_length=50)
    

class Acessos(models.Model):
    IdUsuarios = models.ForeignKey(Usuario, related_name='Acessos_IdUsuarios', on_delete=models.CASCADE)
    IdReceitas = models.ForeignKey(Receitas, related_name='Acessos_IdReceitas', on_delete=models.CASCADE)
    Data = DateField()

