#!/bin/bash -x
export MONO_PATH=$PWD/pkgs/
mono --runtime=v4.0.30319 NuGet.exe install openstack.net -o pkgs/
