    (venv) [ansible@controller 04]$ ansible-playbook 04_02_custom_module/main.yaml 

    PLAY [Example play] ************************************************************

    TASK [PY | Check web-addr status codes] ****************************************
    ok: [localhost] => (item={'addr': 'www.ru', 'tls': False})
    ok: [localhost] => (item={'addr': 'ya.ru'})

    TASK [PY | Print healthcheck_py results] ***************************************
    ok: [localhost] => (item={'changed': False, 'failed': False, 'result_str': 200, 'rc': 0, 'msg': 'Task executed successfully!', 'invocation': {'module_args': {'addr': 'www.ru', 'tls': False}}, 'test_case': {'addr': 'www.ru', 'tls': False}, 'ansible_loop_var': 'test_case'}) => {
        "msg": "www.ru: result=200, rc=0, msg=Task executed successfully!\n"
    }
    ok: [localhost] => (item={'changed': False, 'failed': False, 'result_str': 200, 'rc': 0, 'msg': 'Task executed successfully!', 'invocation': {'module_args': {'addr': 'ya.ru', 'tls': True}}, 'test_case': {'addr': 'ya.ru'}, 'ansible_loop_var': 'test_case'}) => {
        "msg": "ya.ru: result=200, rc=0, msg=Task executed successfully!\n"
    }

    TASK [SH | Check web-addr status codes] ****************************************
    ok: [localhost] => (item={'addr': 'www.ru', 'tls': False})
    ok: [localhost] => (item={'addr': 'ya.ru'})

    TASK [SH | Print healthcheck_sh results] ***************************************
    ok: [localhost] => (item={'rc': 0, 'failed': False, 'result_str': '200', 'msg': 'Task executed successfully!', 'changed': False, 'test_case': {'addr': 'www.ru', 'tls': False}, 'ansible_loop_var': 'test_case'}) => {
        "msg": "www.ru: result=200, rc=0, msg=Task executed successfully!\n"
    }
    ok: [localhost] => (item={'rc': 0, 'failed': False, 'result_str': '200', 'msg': 'Task executed successfully!', 'changed': False, 'test_case': {'addr': 'ya.ru'}, 'ansible_loop_var': 'test_case'}) => {
        "msg": "ya.ru: result=200, rc=0, msg=Task executed successfully!\n"
    }

    PLAY RECAP *********************************************************************
    localhost                  : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
