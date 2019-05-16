# Monitoramento do Openstack Swift - Storage

Desenvolvi um script em python para coletar estatisticas do object storage, simples de configurar e com informações importantes.

## Configuração no Servidor

Configurar o arquivo em cada servidor (que tenha a função de armazenamento de objetos) já com o IP do servidor inserido no arquivo swift-check.conf

```sh
mkdir -p /srv/script/zabbix/
cp -pav swift-check.* /srv/script/zabbix/
cp -pav userparameter_swift.conf /etc/zabbix/zabbix_agentd/
systemctl restart zabbix-agent
```


## Configuração no Zabbix

Importar o template template_object_storage_swift.xml no zabbix e configurar no host monitorado
