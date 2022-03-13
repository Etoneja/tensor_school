    (venv) [ansible@controller 03_01_roles_and_tags]$ ansible-playbook main.yaml --list-tags
    
    playbook: main.yaml
    
      play #1 (nodes): Install and configure Nginx webserver with SSL termination and MariaDB       TAGS: []
          TASK TAGS: [crt, mariadb, nginx]

