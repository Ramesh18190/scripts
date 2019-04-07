#!/bin/bash
  
wget https://packages.wazuh.com/3.x/yum/wazuh-agent-3.7.2-1.x86_64.rpm
sudo rpm -vi wazuh-agent-3.7.2-1.x86_64.rpm
hostname=$(/bin/hostname)
/bin/cp /home/ec2-user/ossec.conf /var/ossec/etc/ossec.conf
/bin/cp /home/ec2-user/sslmanager.cert /var/ossec/etc/sslmanager.cert
/var/ossec/bin/agent-auth -m <wazuh-manager> -p 1515 -A $hostname
service wazuh-agent start
yum clean all
rm wazuh-agent-3.7.2-1.x86_64.rpm
