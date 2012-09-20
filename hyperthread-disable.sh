#!/bin/sh

# Note: This script will disable all cpu's that are virtual hyperthreading cpus.
# put this in your /etc/rc.d/rc.local file to disable at boot. The commented out
# lines below can be uncommented if you only want hyperthreaded cpus to be disabled
# if the `noht` option is added to grub.conf.  

# grep noht /proc/cmdline >& /dev/null
# if [ $? -eq 0 ] ; then # disable hyperthreading
  cat `find /sys/devices/system/cpu -name thread_siblings_list` | sort | uniq > /tmp/thread_siblings_list
  for sibs in `cat /tmp/thread_siblings_list` ; do
    echo $sibs | grep ',' >& /dev/null # if there is a comma (','), then need to disable 2nd
    if [ $? -eq 0 ] ; then
      x=`echo $sibs | cut -f 2 -d ','`
      echo Disabling CPU $x
      echo 0 > /sys/devices/system/node/node0/cpu$x/online
      echo 0 > /sys/devices/system/node/node1/cpu$x/online
    fi
  done
# fi
