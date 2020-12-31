output "k8s_master_ips" {
  value = openstack_compute_instance_v2.k8s_master[*].access_ip_v4
}

output "k8s_master_no-fips" {
  value = openstack_compute_instance_v2.k8s_master_no_floating_ip[*].access_ip_v4
}

output "k8s_node_ips" {
  value = openstack_compute_instance_v2.k8s_node[*].access_ip_v4
}

output "k8s_nodes_ips" {
 # value = openstack_compute_instance_v2.k8s_nodes[*].access_ip_v4
   value = "you have to do nothing with this  var"
}

output "k8s_nodes_no-fips" {
  value = openstack_compute_instance_v2.k8s_node_no_floating_ip[*].access_ip_v4
}


