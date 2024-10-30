# RethinkDNS

- [DNSleaktest](https://www.dnsleaktest.com/)

## [Reddit - Configure App for Optimal Use](https://www.reddit.com/r/rethinkdns/comments/12ta9zo/configure_app_for_optimal_use/)

### Bypass DNS & Firewall vs Exclude

- **Bypasss DNS & Firewall** would let you continue to monitor the app's traffic
  and also apply some app-specific rules (global / universal rules won't apply).
  And example of when you'd use this setting is, say if you've blocked Google
  IPs and domains globally / universally but want to be able to use the Google
  Search app. And would like to still monitor its internet traffic.

- **Bypass Universal** makes the immune to all Universal (aka global) firewall
  rules (but still subject to DNS rules and app-specific rules).

Bypass Universal bypasses only Universal (global) firewall rules (including
trust or block IPs / domains) for a given app.

- **Exclude** is when the app simply won't work with Rethink (like VLC Screen
  Mirroring) and you'd like Rethink to leave it alone and not even monitor its
  internet traffic. Excluding an app puts the app outside of the VPN tunnel
  Rethink creates. It can connect over the underlying network (usually, wifi or
  3g/4g/5g) as if the VPN didn't exist.

Exclude removes the app from Rethink's network namespace (tunnel) and so the
app's requests are not monitored nor mucked with by Rethink at all. For example,
some Chromecast apps don't like Rethink's tunnel... and need to be Excluded to
work.

### If so, what should I toggle on for apps, bypass or exclude?

Apps that break, bypass them first; use exclude as a last resort.

### Isolate

Isolate: That's an advanced security-focused setting for when you'd want to
block an installed app from contacting ALL domains / IPs except the ones you
explicitly trust (allow). Useful for critical apps like WhatsApp, say, which you
know shouldn't contact any domain / IP apart from WhatsApp or Facebook domains /
IPs. As above, this requires a keen eye and a constant investment to make sure
the app keeps working across app updates.

## [Reddit - Simplest way to block Samsung telemetry on a Samsung phone?](https://www.reddit.com/r/rethinkdns/comments/12ej5nb/simplest_way_to_block_samsung_telemetry_on_a/)

Go to Stats page (check the bottom navigation bar in the app) and look for
outgoing connections from apps you never use. These must show up after your
regular apps.

Tap on the entry and rdns should show a "report card" of sorts for the app
detailing all IPs and domains the app has connected to in the past 7 days.

Tap on those entries, then either block individual domains or IPs, or firewall /
isolate the app altogether.

I'm not aware but there could be online resources on all Samsung related
telemetry domains that you can then add to universal DND rules blocklist /
denylist.

RDNS+ (the resolver) has a rudimentary Samsung Blocklist that you can enable if
you use RDNS+: https://sky.rethinkdns.com/1:IAAAAg==<br>
In the app, tap on RDNS+ chip on the homescreen, then tap on Advanced (shown at
the top of the screen). Then, search for "samsung" and select it to add it to
your RDNS+ blocklist.

Btw, since Samsung is the OEM (they control the hardware, firmware, software),
there's really no running away from their grasp, because there's no knowing what
else they run besides Android that could potentially be eavesdropping on you.

## FAQ

- Private DNS is neat, but Rethink also bundles in its own DNS cache which
  updates popular DNS queries in the background. I've been told this reduces
  ping time in Games.

- There's no visibility in to what Private DNS is doing (ie, there is no UI to
  view outgoing DNS queries and watch its incoming responses). A particularly
  important thing if you worry about data exfiltration or misappropriation of
  the DNS protocol.

- Rethink can capture (if Prevent DNS leaks setting is turned ON) ALL traffic on
  port 53 to trap any app trying to connect to preset DNS servers (Signal does
  this, preset to 1.1.1.1).

- Rethink can detect and block ALL traffic to IPs that were not resolved by a
  user-preferred DNS resolver; for example in cases where a DNS-over-HTTPS
  resolver is embed within apps (like Telegram).

- The DNS Logs in Rethink show exactly which blocklists have blocked a
  particular domain.

- Rethink lets user allow any blocked domain through (an on-device allowlist,
  if you will).

- In Rethink, one could put an app in Isolate mode so that it only connects to
  domains / IPs the user has explicitly allowed.

- Or, block connections when device is locked, or block just UDP connections, or
  block just newly installed apps, and so on...

- If Rethink is put in VPN Lockdown mode (ie, Block connection without VPN
turned ON), Android guarantees that Rethink is free from ANY traffic leaks (ie,
no traffic going out without going through Rethink's VPN tunnel).

## VPN

[Wireguard](https://www.reddit.com/r/rethinkdns/comments/161xkt7/how_to_make_wireguard_work_with_rethinkdns/)
