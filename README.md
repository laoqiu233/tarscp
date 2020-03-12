# TARScP
## Sends your code to a remote server in one command

## Why?
I get tired of tar-ing and SCP-ing a project to a remote 
server just to see that I've written 50 more bugs. The time 
used for command typing could be used to write even more bugs. 
So I've written these scripts to help you quickly deploy your code
onto a server.

## Usage
### Client
Put the script in the folder your project folder is in, and run 
the script everytime you want to deploy the code.
Before you run the script, you need to do some configurations inside 
the script:
**folder** - The name of the folder your code is in.
**host** - The address of the remote server.
**username** - Your username on the remote server.
**path** - The path you want to deploy you code in.

Please consider adding your *SSH public key* to your remote server 
for password-less login, thus avoiding typing your password 
everytime you run the script.

### Server
Just run the script where you specified your **path** in the client.