    (venv) [ansible@controller 04]$ ansible-playbook 04_03_wordpress/main.yaml
    ...
    RUNNING HANDLER [nginx : SYSTEMD | Restart Nginx] ******************************
    changed: [node1]

    RUNNING HANDLER [Restart php-fpm] **********************************************
    changed: [node1]

    TASK [HTTP | Check web site from control server | TLS] *************************
    ok: [node1]

    TASK [HTTP | Check web site from control server | No TLS] **********************
    ok: [node1]

    PLAY RECAP *********************************************************************
    node1                      : ok=44   changed=36   unreachable=0    failed=0    skipped=3    rescued=0    ignored=0
