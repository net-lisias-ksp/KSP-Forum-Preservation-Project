# KSP's Forum Preservation Project :: News :: 2025-0122T0600z

I was wrong on considering a problem on Cloudflare as the cause of the failure, so finally it may be the Krakens raining fire and suffering on us.

This is the current DNS entry for forum:

```
forum.kerbalspaceprogram.com	CNAME	2879		forum.kerbalspaceprogram.com.cdn.cloudflare.net
```

And digging it I got:

```
> dig @ns1.cloudflare.com forum.kerbalspaceprogram.com.cdn.cloudflare.net

; <<>> DiG 9.20.3 <<>> @ns1.cloudflare.com forum.kerbalspaceprogram.com.cdn.cloudflare.net
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 21761
;; flags: qr aa rd; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;forum.kerbalspaceprogram.com.cdn.cloudflare.net. IN A

;; AUTHORITY SECTION:
cloudflare.net.		1800	IN	SOA	ns1.cloudflare.net. dns.cloudflare.com. 2362068852 10000 2400 604800 1800

;; Query time: 11 msec
;; SERVER: 173.245.58.100#53(ns1.cloudflare.com) (UDP)
;; WHEN: Wed Jan 22 03:37:06 -03 2025
;; MSG SIZE  rcvd: 134
```

There's no `ANSWER SECTION`, so this entry is not present on the Name Servers. Since it was there yestesday (as we had Forum online), the entry was deleted.

It **WAS** my understanding that the lookup worked walking up the subdomains, so `test.mysite.net` would resolve as follows:

	. -> net. -> mysite.net. -> test.mysite.net.

So when `cdn.cloudflare.com` didn't resolved, I concluded something bad related to it had happened.

I was right about it once, but (as I had learnt the hard way) nowadays it doesn't works like that anymore. At least for CloudFlare.

Well, I stand corrected.
