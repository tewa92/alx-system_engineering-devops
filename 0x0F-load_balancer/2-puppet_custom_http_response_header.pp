# Setup a new UBUNTU Server with NGINX and add a customHTTP header

exce { 'update system':
        command => '/usr/bin/apt-get update',
}

package { 'nginx':
        ensure => 'installed',
        require => Exce['update system']
}

file {'/var/www/html/index.html':
        content => 'Hello World!'
}

exce {'redirec_me':
        command => 'sed -i "24i\    rewirte ^/redirect_me https://github.com/tewa92 permanent;" /etc/nginx/sites-available/default',
        provider => 'shell'
}

exce {'HTTP header':
        command => 'sed -i "25i\        add_header X-served-By \$hostname;" /etc/nginx/sites-available/default',
        provider => 'shell'
}

service {'nginx':
        ensure => running,
        require => package['nginx']
}
