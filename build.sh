#!/bin/bash

pushd external

cmake -S raylib/ -B bin/ -DBUILD_SHARED_LIBS=ON

pushd bin

make

popd
popd

bash generate_binding.sh