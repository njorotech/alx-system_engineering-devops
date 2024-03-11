# Create a file
file { 'school':
  path    => '/tmp/school',
  content => 'I love Puppet',
  mode    => '0744',
  group   => 'www-data',
  owner   => 'www-data'
}