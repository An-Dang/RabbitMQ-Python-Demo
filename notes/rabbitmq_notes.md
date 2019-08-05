# RabbitMQ Notes
## 1 Hello World!
"Hello World!"

## 2 Work queues
- distribute the workload on the deifferent workers, good for webapp
- message acknowledge / even with breaks, the message will be forwarded
- message durability 
  
## 3 Publish/Subscribe
- add exchange 
    - it receives messages from producers
    - it pushes messages to the queue
    - define rules by exchange type 
- in the mid between producers and queue

## 4 Routing
- Bindings
    - like a relationship between exchange and queue - 'the queue is interested in messages from this exchange.'
    - extra routing key as 'binding key'
    

## 5 Topics
- topic exchange similar to direct exchange. Routing key - matching with binding key 
    - '*' can substitute for exactly one word
    - '#' can substitute for zero or more words
- topic exchange can behave like all other exchange type 
    
## 6 RPC
\o/