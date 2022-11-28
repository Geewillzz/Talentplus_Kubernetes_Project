# **Talent Plus Project**

# Deploying a simeple microservice application in Kubernetes cluster


Below are the steps required to get this working on a Windows system using VS Code.

+ Build your backend and frontend images and push to your Docker Hub repository
+ Push both images to your Docker Hub repository
+ Create a helm chart
+ Create a Kubernetes cluster (AWS EKS in my own case)
+ Deploy the backend and frontend services
+ Test the service

## 1. Build your backend and frontend images
docker build -t backend:1.0.4 .
docker build -t frontend:1.0.4 .

==========================================================================

## 2. Push both images to your Docker Hub repository
Firstly, you need to tag the image to your Docker hub account

docker image tag backend:1.0.4 geewillzz/backend:1.0.4
docker image tag frontend:1.0.4 geewillzz/frontend:1.0.4

Now, push both images

docker image push geewillzz/backend:1.0.4

docker image push geewillzz/frontend:1.0.4

==========================================================================

## 3. Create a custom Helm chart
Have Helm installed in your Vs Code

helm version --short

### Then create a custom Helm chart

helm create talentplus

### Vaidate the manifest file

helm template talentplus/

It is important to deploy ingress-nginx on your Kubernetes cluster

helm install ingress-nginx ingress-nginx/ingress-nginx

==========================================================================


## 4. Create a Kubernetes cluster
eksctl create cluster --name talentplus --node-type t2.micro --nodes 4 --nodes-min 4 --nodes-max 5 --region us-east-1 --zones us-east-1a,us-east-1b

It is important to deploy ingress-nginx on your Kubernetes cluster. To do this, run the command below

helm install ingress-nginx ingress-nginx/ingress-nginx

==========================================================================

## 4. Deploy the backend and frontend services
helm install backend talentplus -f talentplus/values/values-backend.yaml
helm install frontend talentplus -f talentplus/values/values-frontend.yaml

Run 'kubectl get pods' to confirm if your pods have been created and are running

==========================================================================

## 5. Test the service
http://a22f91fe13a8e4bc6a2b59c76b1ccfcb-1479939477.us-east-1.elb.amazonaws.com/frontend


