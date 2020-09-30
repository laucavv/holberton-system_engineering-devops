# fixes error 500
exec { 'fix line':
  onlyif   => 'test -e /var/www/html/wp-settings.php',
  provider => shell,
  path     => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  command  => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
}
