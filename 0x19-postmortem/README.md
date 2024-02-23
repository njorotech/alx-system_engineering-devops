## Postmortem

# Apache2 (incident #1)
## Date:
2023-09-29

## Authors:
Samuel Muchoki

## Status:
Complete, solved successfully

## Issue Summary
At approximately 7:30 pm (CST), the web server for the local pet shop, Spot’s Spot, went down due to a security risk from running the Nginx web server as the root user

Root Cause: The Nginx web server was being run by root, was replaced by another service and could no longer listen on post 8080..

## Timeline
* 7:37 PM: Web stack engineers check the currently running processes with ps auxff and find the Nginx web server is not running. They further investigate by running netstat -ldpn which gives them information about the processes running and their ports.

* 7:39 PM: Web stack engineers find apache2 is running on port 8080. They kill the process with pkill apache2 and use netstat -ldpn to confirm nothing is currently listening on port 8080.

* 7:41 PM: Engineers check the /etc/nginx directory to examine Nginx-specific files. They find the nginx.conf configuration file is owned by the user and group root, instead of nginx like all other nginx files, and does not contain any read, write, or execute privileges.

* 7:44 PM: Engineers change the owner and group to nginx with chown nginx:nginx nginx.conf and grant the user read, write, and execute privileges with chmod u+rwx nginx.conf.

* 7:46 PM: Engineers check that Nginx is able to run by restarting the service using sudo service nginx restart. Nginx briefly is running, but the site is listening on port 80 instead of port 8080.

* 7:52 PM: Engineers check through common nginx files and find in /etc/nginx/sites-available/default that the server is default listening on port 80. This is changed to port 8080 and the file is saved.

* 7:53 PM: After restarting the Nginx service, engineers find nginx is listening on port 8080. One problem is fixed.

* 7:54 PM: However, when engineers check the running systems again with ps auxff, they find nginx is still running as root, which leaves the server more vulnerable to attack.

* 7:56 PM: Engineers stop running the service with sudo, or the root user. They then start the service with service nginx start after switching to the nginx user with su nginx.

* 7:57 PM: Nginx is running under the user nginx and is listening on port 8080. The website for Spot’s Spot is back online and customers can access the site
## Root Cause
The root cause came from running the Nginx web server as the root user. This left the server vulnerable to attack and allowed a rival process, apache2, to take over (probably the doing of cats). This attack also removed nginx user privileges and changed the default port the server listens on.

## Corrective and Preventative Measures
1. run Nginx with a less-privileged user
2. check default settings in files
3. add monitoring system
