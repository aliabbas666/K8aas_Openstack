import configparser
import os
import json 

def inventory_generator(jsonstring):
    content = jsonstring

    total_master = int(content['cluster']['number_of_master'])
    total_worker = int(content['cluster']['number_of_worker'])

    project_dir = os.getcwd()+'/kubespray/inventory/eks-automated-cluster/'
    f = open(project_dir+'ips.json',) 
    data = json.load(f) 
    node_ip = data['k8s_nodes_no-fips']['value']  
    master_ip =  data['k8s_master_no-fips']['value']
    f.close()


    total_nodes_ip = node_ip + master_ip
    print ('Total nodes master + worker ips are '+str(total_nodes_ip))  


    config = configparser.ConfigParser(delimiters=(' '),allow_no_value=True)
    config.read(project_dir+'/inventory.ini')
    
    for idx, ip in enumerate(total_nodes_ip):
        config.set('all', 'node'+str(idx), 'ansible_host='+ip+'  ' + ' #ip='+ip+ ' etcd_member_name='+'etcd'+str(idx))
        config.set('etcd', 'node'+str(idx))

    i=0
    while i < total_master:
        config.set('kube-master', 'node'+str(i))
        i += 1

    while i < total_worker+total_master:
        config.set('kube-node', 'node'+str(i))
        i += 1

    #config.set('k8s-cluster:children', 'node'+str(idx))
    with open(project_dir+'/inventory.ini', 'w') as configfile:
        config.write(configfile)

