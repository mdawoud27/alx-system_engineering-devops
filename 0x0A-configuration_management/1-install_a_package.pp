# install flask from pip3.
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Ensure Werkzeug V2.1.1
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}
