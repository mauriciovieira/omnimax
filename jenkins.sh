#!/bin/bash
pip install -q -r requirements.txt

# Rackspace credentials
source /private/devopsy/rackspace_cloud_credentials &> /dev/null

# Node
curl -s -o use-node https://repository-cloudbees.forge.cloudbees.com/distributions/ci-addons/node/use-node
NODE_VERSION=0.10.4 . ./use-node

# Python
virtualenv --distribute DEV
source DEV/bin/activate

# Ruby
curl -s -o use-ruby https://repository-cloudbees.forge.cloudbees.com/distributions/ci-addons/ruby/use-ruby
RUBY_VERSION=1.9.3-p327 \
   source ./use-ruby
gem install --conservative bundler

# PHP
# wget -q https://repository-cloudbees.forge.cloudbees.com/distributions/ci-addons/php/use-php
#PHP_VERSION=5.4.17 . ./use-php

# Go
wget -q https://gist.github.com/maxlinc/6058390/raw/2b84597900298ef8337d7b180a8682ca162e35de/use-go
GOLANG_VERSION=1.1.1 \
    source ./use-go

# .NET

# Run it!
python setup.py install
cd demo
omnimax-cli.py test --behave_opts="-k --tags ~openstacknet --tags ~gophercloud --junit"

