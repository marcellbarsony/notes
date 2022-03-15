# DNS Structure

## Domain Name Space

The **Domain Name Space** consists of a tree data structure: each node or leaf in the tree has a _label_ and zero or more _resource records (RR)_, which hol dinformation associated with the domain name.
The domain name itself consists of the label, concatenated whit the name of its parent node on the right, separated by a dot.
