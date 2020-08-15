#  Add a custom HTTP header with Puppet
exec { 'update':
    command => 'sudo apt-get update',
    path    => ['/usr/bin', '/bin'],
}

package { 'nginx web server':
  ensure => installed,
  name   => 'nginx'
}

file_line { 'custom_header':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => "add_header X-Served-By ${hostname};",
  require => Package['nginx'],
}
service { 'nginx':
    ensure     => running,
    require    => Package['nginx'],
    hasrestart => true
}
