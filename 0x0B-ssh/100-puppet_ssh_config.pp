# Client configuration file (w/ Puppet)

# Ensure SSH Client Configuration Directory Exists
file { '/etc/ssh/ssh_config':
  ensure => 'present',
  owner  => 'root',
  group  => 'root',
  mode   => '0700',
}

# Turn Off Password Authentication
file_line { 'Turn off passwd auth':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  math   => '^#?PasswordAuthentication',
}

# Declare Identity File
file_line { 'Declare identity file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
  math   => '^#?IdentityFile',
}
