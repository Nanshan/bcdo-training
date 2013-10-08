class manage_group {
   group { "devops":
            ensure => present
         }
   group { "sysadmin_gods"
            ensure => adsent
         }

}
