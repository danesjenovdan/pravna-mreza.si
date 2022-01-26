# How to migrate from PVC to S3 storage

- [x] Update secrets.
- [x] Deploy.
- [x] After deployment is finished you won't see any user-uploaded images.
- [x] Sync old media files by editing lines 6 and 7 and then running `./syncmedia.sh`.
- [x] Remove the PVC volumeMount from the deployment.
- [x] Remove nginx container, service and ingress.
- [x] Tripple check that everything works.
- [x] Delete the PVC.
