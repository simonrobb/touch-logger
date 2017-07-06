## Requirements
  - A Raspberry Pi 3 is strongly recommended if the Pi will be displaying the gathered data in Chronograf. Alternatively if the Pi is used as a headless web server, an older version may be used.
  - An I2C sensor on address 0x21
  - A pot plant 🌻

## Provision
Run `sudo sh script/provision.sh` on a fresh installation of Jessie.

Enable the I2C bus using `sudo raspi-config` and restart the pi.

## Start the application
Run `sudo sh script/start.sh` to spawn the python process. Go to `http://localhost:8888` to view the gathered data in Chronograf.

Alternatively view Chronograf on another machine using `http://<pi_address>:8888`.