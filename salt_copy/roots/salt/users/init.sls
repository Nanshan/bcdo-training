test:
  group:
    - present
    - gid: 50173
  user:
    - present
    - fullname: Test User
    - shell: /bin/bash
    - home: /home/test
    - require:
      - group: test 
