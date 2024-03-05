# Fixing the 500 error returned by apache which is caused by a typing error on extension "phpp" instead of "php"

exec {'fixing-500-error':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'

}
