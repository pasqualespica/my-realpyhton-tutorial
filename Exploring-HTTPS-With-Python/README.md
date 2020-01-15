


# Useful links
<!-- Following link is the mai article resource  -->
https://realpython.com/python-https/

https://en.wikipedia.org/wiki/Transmission_Control_Protocol

https://www.restapitutorial.com/

https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview

# Environment steps 
1. pip install -r requirements.txt

# HowTo... and Tip&Tricks 

## Install uwsgi
Anche se "uwsgi" deve essere installato tramite "pip" su MacOs ho avuto alcuni problemi, e per risolverlo ho preferito installarlo tramite brew

```bash
brew install uwsgi
```

## Run uwsgi
Doesn't use port 5683 it associated to Constrained Application Protocol (CoAP) 
into WireShark 

![alt text](img/coAP.png)

```bash
uwsgi --http-socket 127.0.0.1:5985 --mount /=server:app
```


