import os

import subprocess

def doProductcatalogservice():
    os.system("cd src/productcatalogservice && docker build -f Dockerfile -t productcatalogservice:latest . && minikube image load productcatalogservice:latest && cd ../.. && cd kubernetes-manifests && kubectl create --filename productcatalogservice.yaml")
    
def doPaymentservice():
    os.system("cd src/paymentservice && docker build -f Dockerfile -t paymentservice:latest . && minikube image load paymentservice:latest && cd ../.. && cd kubernetes-manifests && kubectl create --filename paymentservice.yaml")
    
def doShippingservice():
    os.system("cd src/shippingservice && docker build -f Dockerfile -t shippingservice:latest . && minikube image load shippingservice:latest && cd ../.. && cd kubernetes-manifests && kubectl create --filename shippingservice.yaml")
    
def doEmailservice():
    os.system("cd src/emailservice && docker build -f Dockerfile -t emailservice:latest . && minikube image load emailservice:latest && cd ../.. && cd kubernetes-manifests && kubectl create --filename emailservice.yaml")

print("Starting manual deployment process")

print("Productcatalogservice deployment")
doProductcatalogservice()
print("Paymentservice deployment")
doPaymentservice()
print("Shippingservice deployment")
doShippingservice()
print("Emailservice deployment")
doEmailservice()

print("Manual process finished")

