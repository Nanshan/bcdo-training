class manage_service {
  service { 'ssh':
     ensure => running,
     enable => true,
     restart => true,
     subscribe => File['/etc/ssh/sshd_config'],
     }
}
