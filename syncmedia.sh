#!/bin/bash

#################################
# set these up before you begin #
#################################
FROM_POD_NAME="pravnamreza-986bc9cf7-rx5bx"
NAMESPACE="pravnamreza"

echo "WARNING! If you did not update the code, don't bother running this. Update the code on production first!"
read -p "Are you sure you want to migrate storage to S3? [y/N]" -n 1 -r
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    echo
    echo "Exiting ..."
    [[ "$0" = "$BASH_SOURCE" ]] && exit 1 || return 1 # handle exits from shell or function but don't exit interactive shell
fi

echo

#################################
# user confirmed, let's do this #
#################################
echo "Downloading FROM -> localhost"
# copy FROM to localhost
kubectl cp $NAMESPACE/$FROM_POD_NAME:/pvc/media ./backup/pvc/media/
echo "Done downloading FROM -> localhost"

echo "I will now attempt to upload files to S3."
read -p "Are you sure you want to upload files to S3? [y/N]" -n 1 -r
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    echo
    echo "Exiting ..."
    [[ "$0" = "$BASH_SOURCE" ]] && exit 1 || return 1 # handle exits from shell or function but don't exit interactive shell
fi
aws s3 sync ./backup/pvc/media s3://djnd/pravnamreza --acl public-read

echo "All done. Now go and check if it worked correctly."
