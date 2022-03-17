# DNS Structure

The **DNS hierarchy** (so called **Domain Name Space**) is an inverted tree structure.<br>
The **DNS hierarchy** tree has a single domain at the top of the structure: the Root Domain.<br>
Below the Root Domain are the Top-Level Domains that divide the **DNS hierarchy** into segments containing Second-Level Domains, Subdomains, and Hosts.

### Root

The **DNS Root level** is the highest in the DNS hierarchy tree as it is the first step in the DNS resolution process.<br>
The **Root DNS Server** is the the DNS for the Root zone that handles requests for records in the Root zone and answers other requests by providing lists of authoritative name servers for the appropriate Top-Level Domain.

The **Root zone** consists of the

- **Organizational hierarchy** - e.g. `.com`, `.net`, `.org`, `.edu`.
- **Geographical hierarchy** - e.g. `.ca`, `.uk`, `.fr`, `.jp`.

Currently, there are 13 root name server specified, with logical names in the form `letter.root-servers.net`, where `letter` ranges from `A` to `M`.

### Top-Level Domains (TLDs)

There are over 1000 TLDs.<br>
**Top-Level Domains** are classified into two subcategories: **organization hierarchy** and **geographical hierarchy**.

### Second-Level Domains (SLDs)

A domain is a **Second-Level Domain** (SLD or 2LD) if it is contained within a top-level domain.
A **Second-Level Domain** is a label - usually, a name related to the website or the business that owns it - immediately to the left of the top-level domain, and separated by a dot.

In the DNS hierarchy, a **Second-level domain** is a domain that is directly below a Top-level domain.<br>
In the FQDN `myexample.com` the **Second-level domain** is `myexample`.

### Subdomains

A **Subdomain** (Third-level domain) - is related to the root domain and is denoted on the left as a Second-level domain.<br>
In the FQDN `blog.example.com` the Third-level domain is `blog.`.

### Hosts

The **Host** part of an FQDN is used to identify an individual device – usually a server.<br>
In the FQDN `server.example.com` the hostname would be `server`.
