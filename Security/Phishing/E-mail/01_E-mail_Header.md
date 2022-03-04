# E-mail header

Internet e-mail messages consists of two sections:

- Header
- Body

RFC 5322 specifies the syntax of the **email header**.
Each email message has a header section, comprising a number of header fields.
Each field has a name ("field name" or "header field name"), followed by the separator character ":", and a value ("field body" or "header field body").

## Header fields

E-mail header fields

The message header must include at least the following fields:

- **From:** The email address, and, optionally, the name of the author(s). Some email clients are changeable through account settings.
- **Date:** The local time and date the message was written. Like the From: field, many email clients fill this in automatically before sending.
  The recipient's client may display the time in the format and time zone local to them.

RFC 3864 describes registration procedures for message header fields at the IANA; it provides for permanent and provisional field names, including also fields defined for MIME, netnews, and HTTP, and referencing relevant RFCs. Common header fields for email include:

- **To:** The email address(es), and optionally name(s) of the message's recipient(s). Indicates primary recipients (multiple allowed), for secondary recipients see Cc: and Bcc: below.
- **Subject:** A brief summary of the topic of the message. Certain abbreviations are commonly used in the subject, including "RE:" and "FW:".
- **Cc:** Carbon copy; Many email clients mark email in one's inbox differently depending on whether they are in the To: or Cc: list.
- **Bcc:** Blind carbon copy; addresses are usually only specified during SMTP delivery, and not usually listed in the message header.
- **Content-Type:** Information about how the message is to be displayed, usually a MIME type.
- **Precedence:** commonly with values "bulk", "junk", or "list"; used to indicate automated "vacation" or "out of office" responses should not be returned for this mail, e.g. to prevent vacation notices from sent to all other subscribers of a mailing list.
  Sendmail uses this field to affect prioritization of queued email, with "Precedence: special-delivery" messages delivered sooner.
  With modern high-bandwidth networks, delivery priority is less of an issue than it was.
  Microsoft Exchange respects a fine-grained automatic response suppression mechanism, the X-Auto-Response-Suppress field.
- **Message-ID:** Also an automatic-generated field to prevent multiple deliveries and for reference in In-Reply-To: (see below).
- **In-Reply-To:** Message-ID of the message this is a reply to. Used to link related messages together. This field only applies to reply messages.
- **References:** Message-ID of the message this is a reply to, and the message-id of the message the previous reply was a reply to, etc.
- **Reply-To:** Address should be used to reply to the message.
- **Sender:** Address of the sender acting on behalf of the author listed in the From: field (secretary, list manager, etc.).
- **Archived-At:** A direct link to the archived form of an individual email message.

The To: field may be unrelated to the addresses to which the message is delivered. The delivery list is supplied separately to the transport protocol, SMTP, which may be extracted from the header content. The "To:" field is similar to the addressing at the top of a conventional letter delivered according to the address on the outer envelope. In the same way, the "From:" field may not be the sender. Some mail servers apply email authentication systems to messages relayed. Data pertaining to the server's activity is also part of the header, as defined below.

SMTP defines the trace information of a message saved in the header using the following two fields:

- **Received:** after an SMTP server accepts a message, it inserts this trace record at the top of the header (last to first).
- **Return-Path:** after the delivery SMTP server makes the final delivery of a message, it inserts this field at the top of the header.

Other fields added on top of the header by the receiving server may be called trace fields.

- **Authentication-Results:** after a server verifies authentication, it can save the results in this field for consumption by downstream agents.
- **Received-SPF:** stores results of SPF checks in more detail than Authentication-Results.
- **DKIM-Signature:** stores results of DomainKeys Identified Mail (DKIM) decryption to verify the message was not changed after it was sent.
- **Auto-Submitted:** is used to mark automatic-generated messages.
- **VBR-Info:** claims VBR whitelisting
