# KSP's Forum Preservation Project :: News :: 2025-0123T2200z

Nothing really changed today, other than the DNS entries.

At 14:35z approximately, I `dig`ed `forum.kerbalspaceprogram.com` and:

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


Furher `dig`ging `sp-forum-elb-2033387385.us-west-2.elb.amazonaws.com` I got:

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

(there's no ANSWER SECTION)

So apparently the new team is trying to move Forum into an Elastic Load Balance on AWS, but until this moment no DNS entry for it was registered.

In time, [Wiki](https://wiki.kerbalspaceprogram.com/) has being working all this time.

Oh, well... Still waiting so.
