## RabbitMQ
RabbitMQ es un intermediario de mensajes pub-sub tradicional (publicar-suscribir), lo que significa que una parte del sistema se comunica con otra parte del sistema a través de una cola de mensajes.

Al usar una cola de mensajes, permite que su aplicacion responda rápidamente y guarde el trabajo pesado para más adelante. Gracias a esta cola, la aplicación no se ve obligada a realizar tareas intensivas en recursos de inmediato, algo que afectaría en gran medida el tiempo de respuesta.

RabbitMQ permite que productores y consumidores se ubiquen en servidores complemente diferentes. Y se puede solicitar un mensaje desde una aplicación construida  en un lenguaje de programación, que luego es manejado por un microservicio escrito en otro lenguaje de programación. Básicamente, las diferentes partes del sistema solo se cominucarán a través de la cola de mensajes. Esta arquitectura RabbitMQ da como resultado un bajo acoplamiento entre los servicios, lo que a su vez hace que la aplicación sea más robusta, más fácil de escalar, desarrollar y mantener.
<br>

### Pika 
Pika is a pure-Python implementation of the AMQP 0-9-1 protocol including RabbitMQ’s extensions.

<br>

### Creando y seteando Entorno virtual
```
python3 -m venv .venv
source .venv/bin/activate
```


### Instalando dependencias
```
pip install pika
pip freeze > requirements.txt
```

### Test local
```
python3 publisher.py
python3 consumer.py 
```