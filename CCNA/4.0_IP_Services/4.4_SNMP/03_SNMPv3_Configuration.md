# SNMP Configuration

Configure **SNMP View** in global configuration

```
R1(config)# snmp-server view <view_name> <mib/oid> included
```

Some of the MIB objects that can be used in `SNMP View`:

- ifIndex
- iso
- ifEntry
- system
- cisco

Now that we have configured the new view read and write, let us proceed in configuring the SNMP Group.

```
R1(config)# snmp-server group <group_name> v3 priv read <view_name>
```

Finally, we are now going to configure the last step, which is an SNMP User.

```
R1(config)# snmp-server user <username> <group_name> v3 auth {md5 | sha} <authentication_password> priv {3des | aes| des} {128 | 192 |256} <encryption_password>
```

[[Study CCNA - SNMPv3 Overview and Configuration](https://study-ccna.com/snmpv3-overview-configuration/)]
