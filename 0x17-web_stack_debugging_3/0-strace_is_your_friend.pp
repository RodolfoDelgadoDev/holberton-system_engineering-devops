# setting
exec {'Correct Setting':
command => "/bin/sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
}
exec { 'Restart Apache2':
require => Exec['Correct Setting'],
command => '/usr/bin/service apache2 restart',
}