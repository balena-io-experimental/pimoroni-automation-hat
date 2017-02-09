# Install a Debian (Jessie) OS with Python 2.7 and Pip installed
FROM resin/raspberrypi3-python:2.7

# use apt-get if you need to install dependencies,
RUN apt-get update && apt-get install -yq --no-install-recommends \
	  python-smbus=3.1.1+svn-2 && \
   	apt-get clean && rm -rf /var/lib/apt/lists/*

# Define our working directory in the container
WORKDIR /usr/src/app

# Copy requirements.txt first for better cache on later pushes
COPY ./requirements.txt requirements.txt
# pip install python deps from requirements.txt
RUN pip install -r requirements.txt

# Copy all our project into /usr/src/app/ folder in the container.
COPY . .
# So in our container we should now have:
# /usr/src/app/
#           |── Dockerfile
#           |── requirements.txt
#           └── project
#               └── main.py

# Load up the i2c module and launch our project
CMD modprobe i2c-dev && python -u project/main.py
