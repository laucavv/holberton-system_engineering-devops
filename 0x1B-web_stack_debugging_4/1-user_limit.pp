#  User limit
exec { 'fix limit':
  onlyif  => 'test -e /etc/security/limits.conf',
  command => 'sed -i "s/5/4096/; s/4/1024/;" /etc/security/limits.conf',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',

}
