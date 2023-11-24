# Create a manifest that kills a process named killmenow.
exec { 'kill MeNow':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin'],
}
