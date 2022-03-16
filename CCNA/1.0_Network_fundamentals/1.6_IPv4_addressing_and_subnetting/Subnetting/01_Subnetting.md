# Subnetting

**Subnetting** is the practice of dividing a network into two or more smaller networks.
It increases routing efficiency, enhances security and reduces the size of the broadcast domain.

<img src="https://www.dropbox.com/s/o7j6hhf6tfzzil7/subnetting1.jpg?dl=1" alt="subnetting1" class="inline" />

On the above example we have a huge network: **10.0.0.0/24**<br>

All hosts on the network are in the same subnet, which has disadvantages:

- **Single broadcast domain** – all hosts are in the same broadcast domain<br>
  A broadcast sent by any device will be processed by all hosts, creating a lots of unnecessary traffic.

- **Network security** – each device can reach any other device on the network, which can present security problems<br>
  Example: A server containing sensitive information shouldn't be in the same network as the user's workstations.

- **Organizational problems** – In large networks, different departments are usually grouped into different subnets.

The above network could be subnetted like this:

<img src="https://www.dropbox.com/s/mhw7w8y90k7k0pe/subnetting2.jpg?dl=1" alt="subnetting1" class="inline" />

In the example two subnets are created for the two departments.<br>
Devices in each subnet are now in a different broadcast domain.
This will reduce the amount of traffic flowing on the network and allows us to implement packet filtering on the router.

[[Study CCNA](https://study-ccna.com/subnetting-explained/)]

## Resources

[[Google Drive - TCM's subnetting cheatsheet](https://docs.google.com/spreadsheets/d/1Bcl8rzfd_2VgBsBx-kzXq406avIIOCqLTN9fvCt063Y/edit?usp=sharing)]

[[David Bombal's Subnet Quiz](https://davidbombal.com/subnet-quiz/)]
