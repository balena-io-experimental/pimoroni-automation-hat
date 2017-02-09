# Resin.io + Pimoroni Automation Hat

This is a project to get you started with the [Pimoroni Automation Hat][automation-hat] and its awesome [python library][py-automation-hat] on resinOS and resin.io.

## Usage

### For resin.io Managed Devices

1. Provision a device in your application following this [Getting Started Guide][resin-get-started].
2. Clone this repository locally and add the `resin git remote` to the repo.
3. Run `git push resin master` and wait for the code to be deployed. The code will build and run, you will hear the relay clicking every 5 seconds.

### For Unmanaged ResinOS devices

1. Follow the [ResinOS Getting Started Guide][resinos-get-started] and get your device set up. Make sure you are familiar with [`rdt`][rdt-link] and can push a basic container.
2. Once your resinOS device is showing on the local network, ssh into it doing `rdt ssh --host`. On the host load up the i2c kernel module by running: `modprobe i2c-dev`
3. Clone this repository locally and run `rdt push resin.local -s .` from the root of the repository folder. The code will build and run, you will hear the relay clicking every 5 seconds.


[automation-hat]:https://shop.pimoroni.com/products/automation-hat
[py-automation-hat]:https://github.com/pimoroni/automation-hat
[resin-get-started]:https://docs.resin.io/raspberrypi3/python/getting-started/
[resinos-get-started]:https://resinos.io/docs/raspberrypi3/gettingstarted/
[rdt-link]:https://www.npmjs.com/package/resin-device-toolbox
