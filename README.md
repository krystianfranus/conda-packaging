Super simple example of building and installing own python package in conda
### Prerequisites
- Installed conda

### Building and installing locally
```
conda create --name my-env
conda activate my-env
conda build recipe/  # built package will be placed in ~/anaconda3/conda-bld/<platform>/
conda install --use-local my-package
```
Example \<platform\>: linux-64

### Testing a package in python interpreter
```
(my-env)$ python
>>> import my_package
>>> import numpy as np
>>> my_package.inc(np.array([1, 2]))
array([2, 3])
```

### Testing a script in cli
```
(my-env)$ my-command
Fancy calculations ...
Random numbers: [1.89999105 1.60328891 1.51856524 1.13193159 1.73525164]
```

___

### Extra
#### Converting a package for use on all platforms
```
conda convert --platform all ~/anaconda3/conda-bld/<platform>/<package_name>.tar.bz2 -o outputdir/
```

#### Uploading to Anaconda.org
Requires *anaconda-client* and account on Anaconda.org
```
anaconda login
anaconda upload ~/anaconda3/conda-bld/<platform>/<package_name>.tar.bz2
```

#### Installing a package locally with pip
```
pip install -e .
```

#### Commands
```
conda build purge-all  # Removing ALL builts in ~/anaconda3/conda-bld/
```

