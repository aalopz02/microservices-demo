import os
import pathlib
import subprocess
from git import Repo


def deleteAllServices():
	local_repo = Repo(path=pathlib.Path(__file__).parent.resolve())
	local_branch = local_repo.active_branch.name
	print("Deleting services from "+ str(local_branch) + " environment")
	if str(local_branch) == "main":
		local_branch = "prod"
	deleteDeployments(local_branch)
	deleteServices(local_branch)
    
def deleteServices(env):
	os.system("kubectl delete service adservice -n="+str(env))
	os.system("kubectl delete service cartservice -n="+str(env))
	os.system("kubectl delete service checkoutservice -n="+str(env))
	os.system("kubectl delete service currencyservice -n="+str(env))
	os.system("kubectl delete service emailservice -n="+str(env))
	os.system("kubectl delete service frontend -n="+str(env))
	os.system("kubectl delete service frontend-external -n="+str(env))
	os.system("kubectl delete service paymentservice -n="+str(env))
	os.system("kubectl delete service productcatalogservice -n="+str(env))
	os.system("kubectl delete service recommendationservice -n="+str(env))
	os.system("kubectl delete service redis-cart -n="+str(env))
	os.system("kubectl delete service shippingservice -n="+str(env))
	os.system("kubectl delete service paymentservice -n="+str(env))

def deleteDeployments(env):
	os.system("kubectl delete deployment adservice -n="+str(env))
	os.system("kubectl delete deployment cartservice -n="+str(env))
	os.system("kubectl delete deployment checkoutservice -n="+str(env))
	os.system("kubectl delete deployment currencyservice -n="+str(env))
	os.system("kubectl delete deployment emailservice -n="+str(env))
	os.system("kubectl delete deployment frontend -n="+str(env))
	os.system("kubectl delete deployment frontend-external -n="+str(env))
	os.system("kubectl delete deployment paymentservice -n="+str(env))
	os.system("kubectl delete deployment productcatalogservice -n="+str(env))
	os.system("kubectl delete deployment recommendationservice -n="+str(env))
	os.system("kubectl delete deployment redis-cart -n="+str(env))
	os.system("kubectl delete deployment shippingservice -n="+str(env))
	os.system("kubectl delete deployment paymentservice -n="+str(env))


deleteAllServices()

print("Delete Services finished")
