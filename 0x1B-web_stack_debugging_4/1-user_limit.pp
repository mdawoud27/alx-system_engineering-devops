# User Limit Task.

exec { 'increase-hard-file':
  command => 'sed -i "/holberton hard/s/5/4096/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'increase-soft-file':
  command => 'sed -i "/holberton soft/s/4/4096/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
