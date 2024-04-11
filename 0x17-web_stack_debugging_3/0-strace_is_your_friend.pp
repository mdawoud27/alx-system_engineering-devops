# Fixes "phpp" bug at the `/var/www/html/wp-settings.php` file

exec {'fix-phpp-word':
    command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    path    => '/usr/local/bin/:/bin/'
}