## Provision
Run `sudo sh script/provision.sh` on a fresh installation of Jessie.

Enable the I2C bus using `sudo raspi-config` and restart the pi.

## Start the application
Run `sudo sh script/start.sh` to spawn the python process. Go to `http://localhost:8888` to view the gathered data in Chronograf.
