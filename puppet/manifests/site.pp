node default {
  include sshd_config  
  include motd
  include cronjob
  include manage_group
  include hosts
}
