Product | Feature | fog | php-opencloud | jclouds | pyrax | pkgcloud | openstack.net | gorax | gophercloud
--------|---------|-----|---------------|---------|-------|----------|---------------|-------|------------
% for group_name, group in features['feature_groups'].iteritems():
	% for feature_name, feature in group['features'].iteritems():
	<% pyrax_status = Feature(group_name, feature_name, feature).determine_status('pyrax') %>
${group_name}|${feature_name}|${pyrax_status}
${type(feature)}
	% endfor
% endfor