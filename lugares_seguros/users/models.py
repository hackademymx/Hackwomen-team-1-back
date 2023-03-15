from django.db import models

# Create your models here.

class User(models.Model): 
    
    users = models.TextField()
    created = models.DateTimeField(auto_now_add=True) #auto_now_add=True significa que permite generar la fecha de creación, y no va a ser eliminable

class Meta:
    db_table = 'users'

def __str__(self):
    return self.users

#el id se forma de manera automático al hacer la migración, crearemos comment que es campo de
#tipo texto que me permitan guardar un montón de caracteres. ver la documentación en modo class
#también se revisará created, que es un campo que indica cuándo se generó ese comentario

#ahora vamos a referenciar la primary key aquí(ver línea 6), según el diagrama de relaciones, la relación places-comment es 1:N 
#foreign key debe llevar dos argumentos principalmente: ('self', on_delete) on_delete indica qué va a suceder cuando se elimine la instanacia padre, osea, 
#qué va a pasar cuando se elimine un place. aquí utilizaremos cascada, por lo que se eliminara en automático el comentario
