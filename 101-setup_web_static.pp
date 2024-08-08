$nginx_conf ="server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html index.htm;
    }
}"

# Install Nginx if it's not already installed
package { 'nginx':
  ensure => present,
}

# Create the necessary directories
file { ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/shared', '/data/web_static/releases/test']:
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

# Create the fake HTML file
file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => 'Hello Airbnb!',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
}

# Create the symbolic link
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test/',
}

# Update the Nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure => file,
  content => template('nginx/default.conf.erb'),
  notify  => Service['nginx'],
}

# Restart Nginx
service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
}
