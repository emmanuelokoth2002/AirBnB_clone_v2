exec { 'apt-update':
  command => '/usr/bin/apt-get -y update',
  path    => '/usr/bin',
  before  => Package['nginx'],
}

package { 'nginx':
  ensure => installed,
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}

file { '/data/web_static/':
  ensure => directory,
}

file { '/data/web_static/releases/test/':
  ensure => directory,
}

file { '/data/web_static/shared/':
  ensure => directory,
}

file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => 'Hello Holberton School!',
}

file { '/var/www/html/custom_404.html':
  ensure  => file,
  content => "Ceci n'est pas une page\n",
}

file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
}

exec { 'chown-ubuntu':
  command => 'chown -R ubuntu:ubuntu /data/',
  path    => '/usr/bin',
}

file_line { 'nginx-location':
  path    => '/etc/nginx/sites-available/default',
  line    => '  location /hbnb_static {',
  match   => '  location / {',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

exec { 'nginx-restart':
  command     => 'service nginx restart',
  path        => '/usr/bin',
  refreshonly => true,
  subscribe   => File_line['nginx-location'],
}
