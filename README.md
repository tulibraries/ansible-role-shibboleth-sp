TU Libraries Shibboleth Service Provider Role
=========

Installs the Shibboleth 2 Service Provider background daemon and Apache httpd module.

Requirements
------------

Expects Apache httpd to already be installed. 

Role Variables
--------------

You must define the following variables (example values provided)
```yaml
shibboleth_sp_idp_metadata_file: idp-metadata.xml # file name for metadata provided by your Identity Provider. You must also create this file in the files directory of your playbook
shibboleth_sp_entity_id: https://my-service.domain.tld/sp/shibboleth # an unique identifier for your servie provider. Often needs to be a URI, though not necessarily the same sa your FQDN
shibboleth_sp_idp_entity_id: https://some-idp.domain.tld/idp/shibboleth # THe identifer provided by your Identity Provider
shibboleth_sp_protected_path: /users/auth/shibboleth/callback # relative path served by Apache httpd that will by initiate Shibboleth authenticaiton workflow when requested.
shibboleth_sp_certificate_file: shib-sp.crt # Shibboleth uses a cert and key to sign metadata. It will create them non-deterministically if they do not exist on process startup. You need to create your own cert / key pair and store the in the files directory of your playbook. 
shibboleth_sp_key_file: shib-sp.crt # used with the crt above.
```

If you want to install a specific version of shibboleth, you can also define that in the following variable:

```yaml
shibboleth_sp_shibboleth_package_name: shibboleth-3.0.4
```


Dependencies
------------

Shibboleth installation for this role tightly coupled with Apache httpd. You are expected to install Apache httpd before this role is run.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - ansible-role-shibboleth-sp
      vars:
        shibboleth_sp_idp_metadata_file: idp-metadata.xml
        shibboleth_sp_entity_id: https://example.entity.sp
        shibboleth_sp_idp_entity_id: https://example.entity.sp
        shibboleth_sp_protected_path: /users/auth/shibboleth/callback
        shibboleth_sp_certificate_file: shib-sp.crt
        shibboleth_sp_key_file: shib-sp.key
 
License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a
website (HTML is not allowed).
