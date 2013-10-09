class manage_content {
  
  file { '/etc/sudoers':
       ower => root,
       group => root,
       mode => 440, 
       content => template("manage_content/sudoers.erb"),
       }
}
