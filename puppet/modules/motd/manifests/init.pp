class motd {
  File { owner => 0, group => 0, mode => 0644 }
  file { '/etc/motd.tail':
    content => "Welcome to Vagrant Managed by Puppet. \n"
       }
}
