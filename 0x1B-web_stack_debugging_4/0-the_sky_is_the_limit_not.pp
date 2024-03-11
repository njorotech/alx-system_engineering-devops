# Fixing failed requests on a nginx server
exec {'increase-ulimit':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',

}

# Restart nginx after increasing ulimit
exec {'Restart-nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/',
}
