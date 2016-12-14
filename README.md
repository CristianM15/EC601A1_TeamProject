# This README file is only intended to let any user/reviewer know that our Github is generally very disorganized (I'm not really too confident navigating Github yet so cleaning it up via CLI is very frightening and I'm not sure I can do it.)  As such, all our files exist in an organized fashion on our AWS branch, so you should check that out.

The only thing you should need from this master branch (againk, sorry I didn't know how to clean GitHub up) is the .pem file (called "EC601_GroupProject.pem".) With this .pem file, one can SSH onto our AWS instance using the following CLI command:

ssh -i ~/Desktop/School/EC601_Alshaykh/GroupProject_NASAFirePrediction/AWS/EC601_GroupProject.pem ec2-user@35.164.49.69

(Althogh in this case, the path name will change depending on where you store the .pem file on your local machine.
