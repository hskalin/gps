
## Running GeoS in Singularity

### Install Singularity

Install Singularity using [these](https://sylabs.io/guides/3.5/user-guide/quick_start.html#quick-installation-steps) instructions (compiled from source). The following combination is known to work :

* Ubuntu/Kubuntu 20.04
* Go 1.18
* Singularity 3.9.8 

### Singularity Definition File

Save the below code as `geosing.def`. 

```
Bootstrap: docker
From: ubuntu:20.04


%post -c /bin/bash
    apt -y update; apt-get -y install wget python python-pip vim git
	  
    git clone https://github.com/seominjoon/geoserver.git
    git clone https://github.com/seominjoon/geosolver.git
    git clone https://github.com/allenai/EquationTree.git


%environment
    export PYTHONPATH=$PYTHONPATH:/root/EquationTree/equationtree
    export PYTHONPATH=$PYTHONPATH:/root/geoserver/geoserver
    export PYTHONPATH=$PYTHONPATH:/root/geosolver/geosolver
    export LC_ALL=C

```

### Building Container

Run the following command after saving the `def` file:

```
sudo singularity build --sandbox geosing.sif geosing.def
```

(if the build fails contact me)

Run the container using the following code:

```
sudo singularity run --writable geosing.sif
```

you can run this in multiple terminals and they will be connected to the same instance of the Singularity container.

This sets up the environment, follow rest from [here](https://github.com/seominjoon/geoserver/blob/master/README.md)
