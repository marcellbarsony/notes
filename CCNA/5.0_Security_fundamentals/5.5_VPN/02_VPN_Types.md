# VPN Types

## Remote access

A **Remote Access VPN** securely connect an endpoint device outside the corporate office resources.
Advances in VPN technology have allowed security check to be conducted on endpoint to make sure they meet certain posture before connecting.
Remote access VPN can use SSL, IKEv2, L2TP, and IPSec protocols.

The system administrator can choose between two modes to implement the remote access VPN:

- **Full Tunnel** – all the traffic that is coming out from the employee’s device will go directly to the firewall, and the firewall will forward it to the internet if necessary.
  This is a completely secured implementation as all the security services of the firewall will be applied to all the traffic coming out from the employee’s device.

- **Split Tunnel** – the traffic that will go to the internet like HTTP/HTTPS traffic will go to the typical internet connection such as broadband/LTE, while the VPN traffic will be used to access the internal resource of the company will use a VPN tunnel.
  The traffic will be split based on its purpose.

## Site-to-Site

A **Site-to-Site VPN** connects the corporate office to branch offices over the Internet.
Site-to-Site VPNs are used when distance makes it impractical to have direct network connections between these offices.
Dedicated equipment is used to establish and maintain connection.

When implementing **Site-to-Site VPN**, Phase 1 and Phase 2 VPN negotiations must be set up:

- **IKE Phase 1 negotiation** is where we create a secure encrypted channel or encrypted network connectivity for the two firewalls can start the Phase 2 negotiation.

- **In IKE Phase 2 negotiation**, the two firewalls will agree on the configured parameters that define what traffic can go via the VPN tunnel and how to authenticate and encrypt the traffic.
  The agreement is called Security Association.
  Both Phase 1 and Phase 2 should have the same parameters, such as pre-shared keys, authentication, encryption, and IKE version.

There are two ways to implement site-to-site VPN:

- **Intranet VPN** – it provides secured site-to-site connectivity within the company or internally.

- **Extranet VPN** – it provides secured site-to-site connectivity outside the company. For example, customers or partners can securely access the shared resources of the company.
