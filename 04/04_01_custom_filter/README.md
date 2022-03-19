    (venv) [ansible@controller 04]$ ansible-playbook 04_01_custom_filter/main.yaml 

    PLAY [Example play] ************************************************************

    TASK [Normalize mac-addresses] *************************************************
    ok: [localhost] => (item=482056876429) => {
        "msg": "Normalized MAC-address: 48:20:56:87:64:29"
    }
    ok: [localhost] => (item=48:20:56:87:64:29) => {
        "msg": "Normalized MAC-address: 48:20:56:87:64:29"
    }
    ok: [localhost] => (item=6b-17-4f-5B-fc-52) => {
        "msg": "Normalized MAC-address: 6B:17:4F:5B:FC:52"
    }
    ok: [localhost] => (item=fae3.fe59.3cb1) => {
        "msg": "Normalized MAC-address: FA:E3:FE:59:3C:B1"
    }
    ok: [localhost] => (item=[6e:4e:c1:b3:98:58]**) => {
        "msg": "Normalized MAC-address: 6E:4E:C1:B3:98:58"
    }
    ok: [localhost] => (item=74:37:52:bb:6e:9d    ) => {
        "msg": "Normalized MAC-address: 74:37:52:BB:6E:9D"
    }

    PLAY RECAP *********************************************************************
    localhost                  : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
