# Add a custom HTTP header with Puppet
exec {'update':
  command => '/usr/bin/ sudo apt-get -y update',
}

package {'nginx':
  ensure => installed,
  name   => 'nginx'
}

file { '/var/www/html/index.html':
  ensure  => present,
  path    => '/var/www/html/index.html',
  content => 'Holberton School'
}

file_line { 'redirect':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=wDjeBNv6ip0 permanent;'
}

file_line {'header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $HOSTNAME;'
}

service { 'service nginx':
  ensure     => running,
  require    => Package['nginx'],
  hasrestart => true
}
