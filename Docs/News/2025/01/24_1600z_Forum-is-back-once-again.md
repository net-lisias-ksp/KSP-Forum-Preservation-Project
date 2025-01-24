# KSP's Forum Preservation Project :: News :: 2025-0124T1600z

Forum is back online. Yet another time. 😅

```
> dig forum.kerbalspaceprogram.com

; <<>> DiG 9.20.3 <<>> forum.kerbalspaceprogram.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 49764
;; flags: qr rd ra; QUERY: 1, ANSWER: 3, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;forum.kerbalspaceprogram.com.	IN	A

;; ANSWER SECTION:
forum.kerbalspaceprogram.com. 3600 IN	CNAME	ksp-forum-elb-2033387385.us-west-2.elb.amazonaws.com.
ksp-forum-elb-2033387385.us-west-2.elb.amazonaws.com. 60 IN A 44.240.13.95
ksp-forum-elb-2033387385.us-west-2.elb.amazonaws.com. 60 IN A 35.155.205.25

;; Query time: 154 msec
;; SERVER: 192.168.200.1#53(192.168.200.1) (UDP)
;; WHEN: Fri Jan 24 13:06:41 -03 2025
;; MSG SIZE  rcvd: 152
```

and 

```
> dig ksp-forum-elb-2033387385.us-west-2.elb.amazonaws.com

; <<>> DiG 9.20.3 <<>> ksp-forum-elb-2033387385.us-west-2.elb.amazonaws.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 62
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
; COOKIE: 483ba604585cf5a8d71619f06793bae8b5f73d99084e4d41 (good)
;; QUESTION SECTION:
;ksp-forum-elb-2033387385.us-west-2.elb.amazonaws.com. IN A

;; ANSWER SECTION:
ksp-forum-elb-2033387385.us-west-2.elb.amazonaws.com. 60 IN A 44.240.13.95
ksp-forum-elb-2033387385.us-west-2.elb.amazonaws.com. 60 IN A 35.155.205.25

;; Query time: 14 msec
;; SERVER: 192.168.200.1#53(192.168.200.1) (UDP)
;; WHEN: Fri Jan 24 13:08:11 -03 2025
;; MSG SIZE  rcvd: 141
```

And just because:

```
> ping forum.kerbalspaceprogram.com
PING ksp-forum-elb-2033387385.us-west-2.elb.amazonaws.com (44.240.13.95): 56 data bytes
--- ksp-forum-elb-2033387385.us-west-2.elb.amazonaws.com ping statistics ---
5 packets transmitted, 0 packets received, 100% packet loss
```
