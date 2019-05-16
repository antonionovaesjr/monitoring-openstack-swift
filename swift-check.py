#!/usr/bin/python
# Desenvolvido por Antonio Novaes antonionovaesjr@gmail.com
import json, urllib
import ConfigParser, os, sys
import time

config = ConfigParser.ConfigParser()
config.readfp(open("/srv/script/zabbix/swift-check.conf"))

host_ip = config.get('DEFAULT','host')
host_port = config.get('DEFAULT','port')

tamanho_sysargs = len(sys.argv)

if tamanho_sysargs == 3:
    servico = sys.argv[1]
    item = sys.argv[2]
    atributo = sys.argv[2]
    url = "http://" + str(host_ip) + ":" + str(host_port) + "/recon/" + str(servico)

if tamanho_sysargs == 4:
    servico = sys.argv[1]
    item = sys.argv[2]
    atributo = sys.argv[3]
    url = "http://" + str(host_ip) + ":" + str(host_port) + "/recon/" + str(servico) + "/" +str(item)
#url = "http://" + str(host_ip) + ":" + str(host_port) + "/recon/" + str(servico) + "/" +str(item)
jsonurl = urllib.urlopen(url)
resposta_json = json.load(jsonurl)

#print(respota_json)

if servico == "quarantined":
    print(resposta_json[str(item)])

if servico == "replication":
    if item == "object":
        if atributo == "replication_last":
            valor_timestamp = resposta_json["replication_last"]
            readable = time.ctime(valor_timestamp)
            print(readable)
#            print(resposta_json["replication_last"])
        elif atributo == "replication_time":
            print(resposta_json["replication_time"])
        elif atributo == "object_replication_time":
            valor_timestamp = resposta_json["object_replication_time"]
            readable = time.ctime(valor_timestamp)
            print(readable)
#            print(resposta_json["object_replication_time"])
        elif atributo == "replication_last":
	    valor_timestamp = resposta_json["replication_last"]
            readable = time.ctime(valor_timestamp)
            print(readable)
#            print(resposta_json["replication_last"])
        else:
            print(resposta_json["replication_stats"][str(atributo)])
    
    if item == "account":
        if atributo == "replication_last":
            valor_timestamp = resposta_json["replication_last"]
            readable = time.ctime(valor_timestamp)
            print(readable)
#            print(resposta_json["replication_last"])
        elif atributo == "replication_time":
            print(resposta_json["replication_time"])
        else:
            print(resposta_json["replication_stats"][str(atributo)])
    
    if item == "container":
        if atributo == "replication_last":
            valor_timestamp = resposta_json["replication_last"]
            readable = time.ctime(valor_timestamp)
            print(readable)
#            print(resposta_json["replication_last"])
        elif atributo == "replication_time":
            print(resposta_json["replication_time"])
        else:
            print(resposta_json["replication_stats"][str(atributo)])


if servico == "auditor":
    if item == "object":
        print(resposta_json["object_auditor_stats_ALL"][str(atributo)])
        
    if item == "account":
        print(resposta_json[str(atributo)])
