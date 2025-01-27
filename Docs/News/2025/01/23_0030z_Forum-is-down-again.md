# KSP's Forum Preservation Project :: News :: 2025-0123T1030z

Aaaaand... Forum is down **AGAIN**... 😁

This is what's happening:

1. A few hours ago, I could reach Forum on my Mobile network.
2. Now I can't on my cable-tv network

All of this strongly suggests it's again a DNS problem.

So, let's dig:

```
> dig forum.kerbalspaceprogram.com

; <<>> DiG 9.20.3 <<>> forum.kerbalspaceprogram.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN, id: 50028
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 1, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;forum.kerbalspaceprogram.com.	IN	A

;; ANSWER SECTION:
forum.kerbalspaceprogram.com. 3600 IN	CNAME	sp-forum-elb-2033387385.us-west-2.elb.amazonaws.com.

;; AUTHORITY SECTION:
us-west-2.elb.amazonaws.com. 60	IN	SOA	ns-332.awsdns-41.com. awsdns-hostmaster.amazon.com. 1 7200 900 1209600 60

;; Query time: 118 msec
;; SERVER: 192.168.200.1#53(192.168.200.1) (UDP)
;; WHEN: Thu Jan 23 11:39:33 -03 2025
;; MSG SIZE  rcvd: 197
```
and then

```
> dig sp-forum-elb-2033387385.us-west-2.elb.amazonaws.com

; <<>> DiG 9.20.3 <<>> sp-forum-elb-2033387385.us-west-2.elb.amazonaws.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN, id: 27398
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1280
;; QUESTION SECTION:
;sp-forum-elb-2033387385.us-west-2.elb.amazonaws.com. IN	A

;; Query time: 0 msec
;; SERVER: 192.168.200.1#53(192.168.200.1) (UDP)
;; WHEN: Thu Jan 23 11:40:11 -03 2025
;; MSG SIZE  rcvd: 80
```

Oukey, no `ANSWER SECTION`. The entry was deleted. Since I had did a dig this afternoon and registered the data: 

```
> dig forum.kerbalspaceprogram.com

; <<>> DiG 9.20.3 <<>> forum.kerbalspaceprogram.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 29233
;; flags: qr rd ra; QUERY: 1, ANSWER: 3, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;forum.kerbalspaceprogram.com.    IN    A

;; ANSWER SECTION:
forum.kerbalspaceprogram.com. 3515 IN    CNAME    forum.kerbalspaceprogram.com.cdn.cloudflare.net.
forum.kerbalspaceprogram.com.cdn.cloudflare.net. 300 IN    A 172.64.145.232
forum.kerbalspaceprogram.com.cdn.cloudflare.net. 300 IN    A 104.18.42.24

;; Query time: 16 msec
;; SERVER: 192.168.200.1#53(192.168.200.1) (UDP)
;; WHEN: Wed Jan 22 17:49:50 -03 2025
;; MSG SIZE  rcvd: 150
```


It ends up that I know the Cloudflare IPs serving Forum. So I edited my `/etc/hosts` file :

```
##
# Host Database
#
# localhost is used to configure the loopback interface
# when the system is booting.  Do not change this entry.
##
127.0.0.1.      localhost
255.255.255.255 broadcasthost
::1             localhost

172.64.145.232  forum.kerbalspaceprogram.com
```

[And here I am!!!](https://forum.kerbalspaceprogram.com/topic/226141-so-we-had-some-kind-of-technical-problem/?do=findComment&comment=4438588) 😄

Not being satisfied, I did another dig on a different network: 

```
> dig forum.kerbalspaceprogram.com.

; <<>> DiG 9.16.12 <<>> forum.kerbalspaceprogram.com.
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN, id: 52563
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 1, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;forum.kerbalspaceprogram.com.	IN	A

;; ANSWER SECTION:
forum.kerbalspaceprogram.com. 300 IN	CNAME	sp-forum-elb-2033387385.us-west-2.elb.amazonaws.com.

;; AUTHORITY SECTION:
us-west-2.elb.amazonaws.com. 8	IN	SOA	ns-332.awsdns-41.com. awsdns-hostmaster.amazon.com. 1 7200 900 1209600 60

;; Query time: 9 msec
;; SERVER: 10.0.0.2#53(10.0.0.2)
;; WHEN: Thu Jan 23 00:10:45 UTC 2025
;; MSG SIZE  rcvd: 197
```


And voilà... The new owners are moving ~~Forum to AWS~~ ditching Cloudflare, and using AWS Elastic Load Balancer instead.

In a few hours the new DNS entry will propagate and fix everything.
