#!/usr/bin/env ruby

# This example demonstrates creating a server with the Rackpace Open Cloud

require 'rubygems' #required for Ruby 1.8.x
require 'fog'
require "base64" #required to encode files for personality functionality

# create Next Generation Cloud Server service
service = Fog::Compute.new({
    :connection_options => {
        :proxy => ENV['https_proxy'],
        :ssl_verify_peer => false
    },
    :provider             => 'rackspace',
    :rackspace_username   => ENV['RAX_USERNAME'],
    :rackspace_api_key    => ENV['RAX_API_KEY'],
    :version => :v2,  # Use Next Gen Cloud Servers
    # :rackspace_region => :ord #Use Chicago Region
})
# puts service.proxy

puts "Authenticated"