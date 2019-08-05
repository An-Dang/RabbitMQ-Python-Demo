# RabbitMQ Notes
## 1 Hello World!
## 2 Work queues
  - Verteilung der Aufgabe/ Parallelisierung der Aufgaben auf verschiedene Worker (Gut bei Webapplikationen)
  - Message acknowledge (auch wenn es abgebrochen wird, werden die MSGs weitergeleitet bis der Kernel stirbt)
  - Message durability 
  
## 3 Publish/Subscribe

## 4 Routing

## 5 Topics
- topic exchange similar to direct exchange. Routing key - matching with binding key 
    - '*' can substitute for exactly one word
    - '#' can substitute for zero or more words
- topic exchange can behave like all other exchange type 
    
## 6 RPC