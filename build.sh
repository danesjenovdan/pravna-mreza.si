#!/bin/bash

sudo docker login rg.fr-par.scw.cloud/djnd -u nologin -p $SCW_SECRET_TOKEN

# BUILD AND PUBLISH PRAVNA MREZA
sudo docker build -f pravna-mreza.si/Dockerfile -t pravna-mreza.si:latest pravna-mreza.si
sudo docker tag pravna-mreza.si:latest rg.fr-par.scw.cloud/djnd/pravna-mreza.si:latest
sudo docker push rg.fr-par.scw.cloud/djnd/pravna-mreza.si:latest
