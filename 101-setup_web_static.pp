# Install Nginx
package { 'nginx':
  ensure => installed,
}

# Create necessary directories
file { '/data':
  ensure => directory,
}

file { '/data/web_static':
  ensure => directory,
}

file { '/data/web_static/releases':
  ensure => directory,
}

file { '/data/web_static/shared':
  ensure => directory,
}

file { '/data/web_static/releases/test':
  ensure => directory,
}

# Create a sample HTML file
file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => '<html>\n<head>\n</head>\n<body>\n  Holberton School\n</body>\n</html>\n',
}

# Create a symbolic link
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
}

# Set ownership to the ubuntu user and group
file { '/data':
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}
