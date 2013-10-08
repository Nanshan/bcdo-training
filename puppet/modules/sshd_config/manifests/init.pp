class sshd_config {
  file { '/etc/ssh/sshd_config':
    source => "puppet:///modules/sshd_config/sshd_config_file"       
    }

}
