class hosts {
  host { "localhostadmin":
          ensure => present, 
          ip => '10.0.0.0',
          comment => "add a new entry to /etc/hosts",
          target => '/etc/hosts'
       }
}

