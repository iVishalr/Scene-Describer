# Scene Describer

## Requirements

1. LuaJit
2. Torch
3. Luarocks
4. h5py
5. Loadcaffe
6. torch-hdf5
7. image,nn,nngraph

## Instructions to install all the dependencies

#### Installing Torch

##### Requirements

1. CMake

```bash
$ git clone https://github.com/torch/distro.git ~/torch --recursive
$ cd ~/torch; bash install-deps;
$ ./install.sh
$ source ~/.bashrc
```

*Note: Henceforth use luarocks from torch and not the from sudo apt install luarocks*
#### Installing Loadcaffe 

```bash
$ sudo apt-get install libprotobuf-dev protobuf-compiler
$ luarocks install loadcaffe
```

#### Installing Torch-HDF5

```bash
$ sudo apt-get install libhdf5-serial-dev
$ luarocks install hdf5
```

#### Installing h5py

```bash
$ pip install h5py
```

#### Additional Lua rock files,

```bash
$ luarocks install nn
$ luarocks install nngraph
$ luarocks install image
```

If you have GPU, 

Please download CUDA ToolKit from here https://developer.nvidia.com/cuda-toolkit

You will need to download additional files,

```bash
$ luarocks install cutorch
$ luarocks install cunn
```

#### After Installing all the libraries,

Note : If any of the installation commands fail, please follow the procedure given in the terminal. Also some of the dependencies require CMake for it to build.

Finally, there is a small modification in the source code that needs to be done.

Open hdf5/ffi.lua in editor  # File Path - Users//torch/install/share/lua/5.2/hdf5/ffi.lua

change

"if maj[0] ~= 1 or min[0] ~= 8 then"

to

"if maj[0] ~= 1 or min[0] ~= 10 then"

### Finally, to caption images,

If you have only CPU in your system, download the weights from http://cs.stanford.edu/people/karpathy/neuraltalk2/checkpoint_v1_cpu.zip and place the file in the project directory.

If you have a GPU, download the weights from http://cs.stanford.edu/people/karpathy/neuraltalk2/checkpoint_v1.zip and place the file in the project directory.

Rename the weights you just downloaded to model.t7

For CPU,

```bash
$ th eval.lua -model /path/to/model -image_folder /path/to/image/folder -num_images 10 -gpuid -1 -dump_path 0 -dump_images 0
```

For GPU,

```bash
$ th eval.lua -model /path/to/model -image_folder /path/to/image/folder -num_images 10 -dump_path 0 -dump_images 0
```
