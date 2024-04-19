# This manifest is about create a file at /tmp
file { '/tmp/school':
    ensure  => 'file',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet',
}
