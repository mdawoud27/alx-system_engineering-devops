# User limit task

exec { 'increasing hard file':
  command => 'sed -i "/holberton hard/s/5/4096" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'increasing soft file':
  command => 'sed -i "/holberton soft/s/4/4096" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
