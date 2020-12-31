import flask
from flask import request, jsonify
from pathlib import Path
import os
import shutil
#from python_terraform import *
import re
from cluster_play import *
import subprocess
from config_generator import * 


app = flask.Flask(__name__)
app.config["DEBUG"] = True


def str_replace(fname, pat, s_after):
  with open(fname) as f:
        out_fname = fname + ".tmp"
        out = open(out_fname, "w")
        for line in f:
            out.write(re.sub(pat, s_after, line))
        out.close()
        os.rename(out_fname, fname)


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"






@app.route('/api/v1/resources/books', methods=['GET'])
def api_filter():
    query_parameters = request.args
    content = request.json
    print (content['cluster']['cluster_name'])
    kubespray_base_path = os.getcwd()+'/kubespray'
    print(kubespray_base_path)
       #Path(kubespray_base_path +'/inventory/'+content['cluster']['cluster_name']).mkdir(parents=True, exist_ok=False)
#    destination = shutil.copytree(kubespray_base_path +'/contrib/terraform/openstack/sample-inventory', kubespray_base_path+'/inventory/'+content['cluster']['cluster_name']+'/')
#    print (destination)
#    os.symlink(kubespray_base_path+'/contrib/terraform/openstack/hosts',kubespray_base_path +'/inventory/'+content['cluster']['cluster_name']+'/hosts' )
#    os.symlink(kubespray_base_path+'/contrib',kubespray_base_path +'/inventory/'+content['cluster']['cluster_name']+'/contrib' )

#    code block for replacing variables in cluster.tfvars file

    filename = kubespray_base_path+'/inventory/'+content['cluster']['cluster_name']+'/'+'cluster.tfvars'
    pattern = '\s*=\s*([\S\s]+)'
#    str_replace(filename, 'cluster_name' +pattern , 'cluster_name = '+ '"'+ content['cluster']['cluster_name']+'"'+'\n')
#    str_replace(filename, 'number_of_k8s_nodes' +pattern , 'number_of_k8s_nodes = '+ content['cluster']['number_of_worker']+'\n')
#    str_replace(filename, 'number_of_k8s_masters' +pattern , 'number_of_k8s_masters = '+ content['cluster']['number_of_master']+'\n')
#    str_replace(filename, 'network_name' +pattern , 'network_name = '+'"'+content['cluster']['network_name']+'"'+'\n')
#    str_replace(filename, 'floatingip_pool' +pattern , 'floatingip_pool = '+'"'+content['cluster']['floatingip_pool']+'"'+'\n')
#    str_replace(filename, 'subnet_cidr' +pattern , 'subnet_cidr = '+'"'+ content['cluster']['subnet_cidr']+'"'+'\n')
    str_replace(filename, 'auth_token' +pattern , 'auth_token = '+'"'+ content['cluster']['auth_token']+'"'+'\n')



#   code block for runnig terraform from backend

#    os.chdir(kubespray_base_path+'/inventory/'+content['cluster']['cluster_name']+'/')
#    print ("After changing working directory: " + os.getcwd())
#    terraform_working_dir= kubespray_base_path +'/contrib/terraform/openstack'
#    print (terraform_working_dir)
#    tf = Terraform(working_dir=terraform_working_dir)
#    tf.init(capture_output=False)
#    tf.apply(input=True,skip_plan=True, no_color=IsFlagged, refresh=False , capture_output=False , var_file=kubespray_base_path+'/inventory/'+content['cluster']['cluster_name']+'/'+'cluster.tfvars')

#    code block end terraform
    
    
     
#    code block for running terraform using bash script
    rc = subprocess.call("./create_stack_tf.sh",shell=True)    
    inventory_generator(content)


#    code for running playbook for making cluster configuration
#    rc = subprocess.call("./export.sh",shell=True)
#    cluster_playbook_executer()

#    id = query_parameters.get('id')
#   published = query_parameters.get('published')
#    author = query_parameters.get('author')


    
    return jsonify(content)
app.run(host= '0.0.0.0')
