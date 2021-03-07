# Scene Describer

## Requirements

1. Lua
2. Torch
3. Luarocks
4. Caffe
5. Loadcaffe
6. Lua-cjson
7. Torch-HDF5
8. h5py

### Instructions to install all the dependencies
___

##### Using HomeBrew,

```bash
brew install lua
brew install caffe
brew install luarocks
brew install NANOMSG
brew install hdf5
```

##### Installing Torch

```bash
$ curl -s https://raw.githubusercontent.com/torch/ezinstall/master/install-deps | bash
$ git clone https://github.com/torch/distro.git ~/torch --recursive
```

##### Installing Loadcaffe 

```bash
$ git clone https://github.com/szagoruyko/loadcaffe
$ cd loadcaffe
$ sudo luarocks make
```

##### Installing Lua-cjson

```bash
$ git clone https://github.com/mpx/lua-cjson.git
$ cd lua-cjson
$ sudo luarocks make
```

##### Installing Torch-HDF5

```bash
$ git clone https://github.com/deepmind/torch-hdf5
$ cd torch-hdf5
$ sudo luarocks make hdf5-0-0.rockspec
```

##### Installing h5py

```bash
$ pip install h5py
```

##### Additional Lua rock files,

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

##### After Installing all the libraries,

```bash
$ cd ~/torch;
$ ./install.sh # and enter "yes" when asked at the end to modify your bashrc
$ export PATH=$PATH:$HOME/torch/install/bin #add this to your bash profile as well.
$ source ~/.bashrc
```

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
