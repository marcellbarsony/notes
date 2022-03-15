# DNS Server Types

There are 4 DNS servers involved in loading a webpage:

- **DNS Recursor** — The **DNS Recursive Resolver** is a server designed to receive queries from client machines through applications (such as web browsers).
  The **DNS Recursor** is then responsible for making additional requests in order to satisfy the Client's DNS query.

- **Root nameserver** — The **Root Nameserver** is the first step in translating (resolving) human readable host names into IP addresses.
  It can be thought of like an index in a library that points to different racks of books - typically it serves as a reference to other more specific locations.

- **TLD nameserver** — The **Top Level Domain Server (TLD)** is the next in the search for a specific IP address, and it hosts the last portion of a hostname (e.g. in _example.com_ the TLD server is "com")

- **Authoritative nameserver** — The **Authoritative Nameserver** is the last stop in the nameserver query.
  If the authoritative name server has access to the requested record, it will return the IP address for the requested hostname back to the **DNS Recursor** that made the initial request.

<img src="https://www.dropbox.com/s/ofqlg9qz3x2tro2/dns_servers.png?dl=1" alt="dns_servers" class="inline" />

[[Cloudflare - DNS Server Types](https://www.cloudflare.com/learning/dns/dns-server-types)]

## 01. DNS Recursive Resolver

A **Recursive Resolver** (also known as a DNS recursor) is the first stop in a DNS query.<br>
The **Recursive Resolver** acts as a middleman between a client and a DNS nameserver:

1. After receiving a DNS query from a web client, a **Recursive Resolver** will either:

- Respond with cached data or
- Send a request to a **Root nameserver**

  - Followed by another request to a **TLD nameserver**
  - Then one last request to an **Authoritative nameserver**

2. After receiving a response from the **Authoritative nameserver** containing the requested IP address, the **Recursive Resolver** then sends a response to the client.

During this process, the **Recursive resolver** will cache information received from **Authoritative name** servers:<br>
When a client requests the IP address of a domain name that was recently requested by another client, the **Recursive Resolver** can circumvent the process of communicating with the nameservers, and just deliver the client the requested record from its cache.

Most internet users use a **Recursive Resolver** provided by their ISP, but there are other options available; for example [Cloudflare's 1.1.1.1](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1/).

### What is recursive DNS?

A **Recursive DNS Lookup** us where one DNS Server communicates with several other DNS servers to hunt down an IP address and return it to the client.<br>
This is in contrast to an **Iterative DNS Query**, where the client communicates directly with each DNS server involved in the lookup.

**Recursive DNS queries** generally tend to resolve faster than Iterative queries, due to caching:
A recursive DNS server caches the final answer to every query it performs and saves that for a certain amount of time (known as Time-To-Live).

Allowing **Recursive DNS Queries** on open DNS servers creates a security vulnerability, as this configuration can enable attackers to perform [DNS amplification attacks](https://www.cloudflare.com/learning/ddos/dns-amplification-ddos-attack/) and [DNS cache poisoning](https://www.cloudflare.com/learning/dns/dns-cache-poisoning/).

[[Cloudflare - What is recursive DNS?](https://www.cloudflare.com/learning/dns/what-is-recursive-dns/)]

### Recursion vs. Iteration

**Recursion** and **Iteration** are computer science terms that describe two different methods to solve a problem:

- In **Recursion**, a program repeatedly calls itself until a condition is met.
- In **Iteration**, a set of instructions is repeated until a condition is met.

[[Wikipedia - Public recursive name server](https://en.wikipedia.org/wiki/Public_recursive_name_server)]

## 02. DNS Root Nameserver

A [DNS Root Name Server](https://en.wikipedia.org/wiki/Root_name_server) is a [name server](https://en.wikipedia.org/wiki/Name_server) for the [root zone](https://en.wikipedia.org/wiki/DNS_root_zone) of the Domain Name System of the Internet.
It directly answers requests for records in the root zone and answers other requests by returning a list of the authoritative name servers for the appropriate top-level domain.
The **DNS Root Name Server**s are critical part of the Internet infrastructure as they are the first step in resolving human-readable host names into IP addresses.

The 13 logical **DNS Root Nameserver**s are known to every Recursive Resolver, and they are the first stop in a Recursive Resolver's quest for DNS records:

1. A **Root Nameserver** accepts a Recursive Resolver's query which includes a domain name.
2. The **Root Nameserver** responds by directing the Recursive Resolver to a TLD Nameserver, based on the extension (.com, .net, .org, etc.) of that domain.

The **Root Nameserver**s are overseen by a nonprofit called the [Internet Corporation for Assigned Names and Numbers (ICANN)](https://www.icann.org/).

### Root domain

The [Root Domain](https://en.wikipedia.org/wiki/DNS_root_zone) contains all top-level domains of the Internet.

The DNS is a hierarchical naming system for computer, services, or any other resource participating in the Internet.
The top of that hierarchy is the **Root Domain**.
The **Root Domain** does not have a formal name and its label in the DNS hierarchy is an empty string.
All [fully qualified domain names (FQDNs)](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) on the Internet can be regarded as ending with this empty string for the **Root Domain**, and therefore ending in a full stop character (the label delimiter), e.g. "www.example.com".
This is generally implied rather than explicit, as modern DNS software does not actually require that the terminating dot be included when attempting to translate a domain name to an IP address.

## 03. TLD Nameserver

A **[TLD Nameserver](https://en.wikipedia.org/wiki/Top-level_domain)** is one of the domains at the highest level in the hierarchical Domain Name System of the Internet after the Root domain.
The top-level domain names are installed in the [root zone](https://en.wikipedia.org/wiki/DNS_root_zone) of the name space.
A **TLD Namerserver** maintains information for all the domain names that share a common domain extension (e.g. .com, .net, etc.).

Management of the **TLD Nameservers** if handled by IANA, which is a branch of ICANN.<br>
IANA breaks up the TLD servers into two main groups:

- **Generic top-level domains**: These are domains that are not country specific: _.com, .org, .net, .edu, and .gov_
- **Country code top-level domains**: These include any domains that are specific to a country or state: _.uk, .hu, .pl, and .jp_

## 04. Authoritative Nameserver

An **Authoritative Nameserver** is the authority for its zone.<br>
It queries and is queried by other name servers in the DNS, and then caches the received data.

There are two types of authoritative servers: master (primary) and secondary.
Each zone must have only one master name server, and it should have at least one secondary name server for backup purposes.

When a Recursive Resolver receives a response from a TLD Nameserver, that response will direct the Resolver to an **Authoritative Nameserver**.
The **Authoritative Nameserver** is usually the Resolver's last step in the journey for an IP address.

- The **Authoritative Nameserver** contains information specific to the domain name it serves (e.g. google.com) and it can provide a Recursive Resolver with the IP address of that server found in the [DNS A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/).

- If the domain has a [CNAME record](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/) (alias) it will provide the Recursive Resolver with an alias domain, at which point the Recursive Resolver will have to perform a whole new DNS lookup.

[[IBM - Authoritative servers](https://www.ibm.com/docs/en/zos/2.4.0?topic=servers-authoritative)]<br>
[[IBM - Master server](https://www.ibm.com/docs/en/zos/2.4.0?topic=servers-master-name)]<br>
[[IBM - Secondary server](https://www.ibm.com/docs/en/zos/2.4.0?topic=servers-secondary-name)]
