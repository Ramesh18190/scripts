#!/bin/bash
  
for line in $(cat hostname.txt)
 do
  scp -i /Users/username/.ssh/key.pem wazuh-agent.sh sslmanager.cert ossec.conf ec2-user@$line:/home/ec2-user/
done
for line in $(cat hostname.txt)
 do
    ssh -i /Users/username/.ssh/key.pem ec2-user@"$line" << EOF
    sudo su -
    mv /home/ec2-user/wazuh-agent.sh /root/
    chmod 700 wazuh-agent.sh
    ./wazuh-agent.sh
    sudo rm wazuh-agent.sh
exit
exit
EOF
done
