#!/bin/bash

# Note: Put this file (e.g. ssh-agent.sh) in the /etc/profile.d/ directory (and make it executable via `chmod +x`) 
# to properly enable ssh-agent for all machines. Seems simple, but a pain in the neck to get this working properly.
# Compatibiity: Works fine on CentOS 6.X (6.3 as of my testing) and RHEL. YMMV.
# License: MIT License; Free as in beer. 

SSH_ENV="/tmp/ssh-agent_environment" # centralized file location. accessible to all users.

function start_agent {
     echo "SSH agent: Starting"
     /usr/bin/ssh-agent | sed "s/^echo/#echo/" > "${SSH_ENV}"
     echo "SSH agent: [OK]"
     chmod 666 "${SSH_ENV}" # make r/w for all users.
     . "${SSH_ENV}" > /dev/null
     /usr/bin/ssh-add;
}

# Source SSH settings, if applicable

if [ -f "${SSH_ENV}" ]; then
     . "${SSH_ENV}" > /dev/null
     ps -ef | grep ${SSH_AGENT_PID} | grep ssh-agent$ > /dev/null || {
         start_agent;
     }
else
     start_agent;
fi