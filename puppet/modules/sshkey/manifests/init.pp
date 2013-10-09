class sshkey{

ssh_authorized_key {
        "kate":
                ensure  => absent,
                user    => root,
                type    => "ssh-rsa",
                key     => "AAAA......j";
        "root":
                ensure  => present,
                user    => root,
                type    => "ssh-rsa",
                key     => "AAAAB.......";
}
}
