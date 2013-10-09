class manage_user {

   user { "leah2":
         ensure => "present",
         managehome => true,

        }

    user { "lifang":

        ensure => absent

         }

}
