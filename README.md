# Install my PC

Not the most useful or the most advanced project ever done, not the best technology to do it, it's mostly about playing with ansible.

```
# Install ansible
chmod u+x setup.sh
./1-setup.sh
# Install my tools, enter the sudo password
ansible-playbook 2-install.yaml --ask-become-pass
```
