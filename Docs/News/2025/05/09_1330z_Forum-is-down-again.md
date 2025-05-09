# Here we go again: Forum is down

At May 9th, 2025 aproximately 13:30 Zulu Forum is down for me.

![Forum Is Down](./forum-is-down-again.png]

By some reason, CloudFlare is answering the request (again).

```
> dig forum.kerbalspaceprogram.com

; <<>> DiG 9.20.8 <<>> forum.kerbalspaceprogram.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 24265
;; flags: qr rd ra; QUERY: 1, ANSWER: 4, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1400
;; QUESTION SECTION:
;forum.kerbalspaceprogram.com.	IN	A

;; ANSWER SECTION:
forum.kerbalspaceprogram.com. 3600 IN	CNAME	o334077.invisionservice.com.
o334077.invisionservice.com. 300 IN	CNAME	community.invisionsetup.com.
community.invisionsetup.com. 300 IN	A	162.159.141.105
community.invisionsetup.com. 300 IN	A	172.66.1.101

;; Query time: 46 msec
;; SERVER: 192.168.200.1#53(192.168.200.1) (UDP)
;; WHEN: Fri May 09 11:02:00 -03 2025
;; MSG SIZE  rcvd: 165
```

Don't have a clue about what could be happening at this moment.

- - -

* https://github.com/net-lisias-ksp/KSP-Forum-Preservation-Project
	+ https://archive.org/details/KSP-Forum-Preservation-Project
	+ https://archive.org/details/KSP-WIKI-Preservation-Project
