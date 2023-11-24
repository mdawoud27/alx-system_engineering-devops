# Create a manifest that kills a process named killmenow.
exec { 'killMeNow':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin'],
}
