# DNS Servers - Part 2

## Stealth Server

A **Stealth Server** is a server that answers authoritatively for a zone, but is not listed in that zone's NS records.
**Stealth Servers** can be used as a way to centralize distribution of a zone, without having to edit the zone on a remote name server.
When the master file for a zone is on a **Stealth Server** in this way, it is often referred to as a hidden primary configuration.
**Stealth Servers** can also be a way to keep a local copy of a zone for rapid access to the zone's records, even if all official name servers for the zone are inaccessible.

[[IBM - Stealth Server](https://www.ibm.com/docs/en/zos/2.4.0?topic=servers-stealth-server)]

## Forwarders

Normally, name servers answer queries from cached data or, if that does not succeed, they attempt to contact other name servers identified in their data files as authoritative for certain domains.
However, name servers can also be configured to contact special servers called **forwarders** before contacting the name servers listed in their data files.
If a **forwarder** cannot process the query and if the local name server is not a forward-only name server, the local name server contacts the name servers in its data files.
A forward-only name server relies completely on its **forwarders**.
It does not try to contact other servers to find out information if the **forwarders** do not give it an answer.

The forwarding function is useful for reducing the number of queries to servers on the Internet and for creating a large cache of information on **forwarders**.
It is also a useful function for providing Internet access for local servers that, for one reason or another, do not have access themselves.

[[IBM - Forwarders](https://www.ibm.com/docs/en/zos/2.4.0?topic=servers-forwarders)]

## Caching-only Servers

All name servers cache (store) the data they receive in response to a query.
A **caching-only server**, however, is not authoritative for any domain.
Responses derived from cached information are flagged in the response.
When a **caching-only server** receives a query, it checks its cache for the requested information.
If it does not have the information, it queries a local name server or a root name server, passes the information to the client, and caches the answer for future queries.
The names and addresses of the root name servers are acquired from the servers listed in the hints file, the name and file path of which are specified in the name server's configuration file.

You can manually configure a name server to create a large cache of responses to queries that are frequently requested and reduce the number of queries made to master servers.
The name server that you configure as a **caching-only server** stores data for a period of time determined by the time-to-live (ttl) value, and the cached information is lost if the name server is restarted.

[[IBM - Caching-only servers](https://www.ibm.com/docs/en/zos/2.4.0?topic=servers-caching-only)]

## Difference between Authoritative DNS Server vs. Recursive DNS Resolver

Both concepts refer to servers (groups of servers) that are integral to the DNS infrastructure, but each performs a different role and lives in different locations inside the pipeline of a DNS query.
One way to think about the difference is the recursive resolver is at the beginning of the DNS query and the authoritative nameserver is at the end.

[[Cloudflare - What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/)]

### Authoritative DNS Server

Put simply, an authoritative DNS server is a server that actually holds, and is responsible for, DNS resource records.
This is the server at the bottom of the DNS lookup chain that will respond with the queried resource record, ultimately allowing the web browser making the request to reach the IP address needed to access a website or other web resources.
An authoritative nameserver can satisfy queries from its own data without needing to query another source, as it is the final source of truth for certain DNS records.

It’s worth mentioning that in instances where the query is for a subdomain such as foo.example.com or blog.cloudflare.com, an additional nameserver will be added to the sequence after the authoritative nameserver, which is responsible for storing the subdomain’s CNAME record.

There is a key difference between many DNS services and the one that Cloudflare provides.
Different DNS recursive resolvers such as Google DNS, OpenDNS, and providers like Comcast all maintain data center installations of DNS recursive resolvers.
These resolvers allow for quick and easy queries through optimized clusters of DNS-optimized computer systems, but they are fundamentally different than the nameservers hosted by Cloudflare.

Cloudflare maintains infrastructure-level nameservers that are integral to the functioning of the Internet.
One key example is the f-root server network which Cloudflare is partially responsible for hosting.
The F-root is one of the root level DNS nameserver infrastructure components responsible for the billions of Internet requests per day.
Our Anycast network puts us in a unique position to handle large volumes of DNS traffic without service interruption.

### Recursive DNS Resolver

The recursive resolver is the computer that responds to a recursive request from a client and takes the time to track down the DNS record.
It does this by making a series of requests until it reaches the authoritative DNS nameserver for the requested record (or times out or returns an error if no record is found).
Luckily, recursive DNS resolvers do not always need to make multiple requests in order to track down the records needed to respond to a client; caching is a data persistence process that helps short-circuit the necessary requests by serving the requested resource record earlier in the DNS lookup.
