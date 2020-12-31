#!/bin/bash
echo 'running terrafrom '
cd ~/KUBE_AUTO/projects/api/kubespray/inventory/eks-automated-cluster/
terraform init ../../contrib/terraform/openstack
terraform apply -auto-approve -var-file=cluster.tfvars ../../contrib/terraform/openstack
terraform output -json > ips.json
