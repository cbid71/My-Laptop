En l'état nous avons installé Ollama en bare-metal et non sur kubernetes, ç'aurait été mieux mais nous avons eu trop d'erreurs.
Ollama est donc sur le host de Minikube.

```
ollama run mistral
```

Nous avons configuré Ollama pour qu'il soit en écoute sur toutes les interfaces (OLLAMA_HOST=0.0.0.0:11434) en modifiant le service Ollama en conséquence

Puis appel via : http://localhost:11434/api/generate

Nous allons réaliser une interface entre KubeFlow et Ollama en tant que service d'inférence, cela se présente sous la forme d'une API qui fait l'interface.

Nous allons compiler l'image interface qui fait l'interface avec Ollama
```
docker build inferenceimagemistral/ -t $(minikube ip):5000/inferenceimagemistral
docker push $(minikube ip):5000/inferenceimagemistral
```

---
Si le push ne fonctionne pas `sudo nano /etc/docker/daemon.json`

```
{
  "insecure-registries": ["aa.bb.cc.dd:5000"]
}
```
où `aa.bb.cc.dd` est l'IP renvoyée par la commande `minikube ip`1

et redémarrer docker et Minikube

systemctl restart docker
minikube start
---



Deployer l'objet InferenceService in `inferenceService.yaml`
