from django.db import models

# Create your models here.


class Estudiante(models.Model):
    ApellidoP = models.CharField(max_length=35)
    ApellidoM = models.CharField(max_length=35)
    Nombres = models.CharField(max_length=35)
    Matricula = models.CharField(max_length=8)
    FechaNacimiento=models.DateField()
    SEXOS=(('F', 'Femenino'),('M','Masculino'))
    Sexo=models.CharField(max_length=1, choices=SEXOS, default='M')

    def NombreCompleto(self):
        cadena="{0} {1}, {2}"
        return cadena.format(self.ApellidoP, self.ApellidoM, self.Nombres)
    
    def __str__(self):
        return self.NombreCompleto()

    
class Materia(models.Model):
    NombreM=models.CharField(max_length=50)
    Creditos=models.PositiveSmallIntegerField()
    Estado=models.BooleanField(default=True)

    def __str__(self):
        return "{0} ({1})".format(self.NombreM, self.Creditos)

class NumeroControl(models.Model):
    Estudiante=models.ForeignKey(Estudiante, null=False, blank=False, on_delete=models.CASCADE)
    Materia=models.ForeignKey(Materia, null=False, blank=False, on_delete=models.CASCADE)
    FechaMatricula=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        cadena = "{0} => {1}"
        return cadena.format(self.Estudiante, self.Materia.NombreM)

