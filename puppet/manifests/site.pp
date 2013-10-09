node default {
  $myvar = "kate"
  include test
  include sshd_config  
  include motd
  include cronjob
  include manage_group
  include hosts
  include manage_user
  include manage_service
  include sshkey
  include installs
  include install2
}
