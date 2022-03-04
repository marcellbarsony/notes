# E-mail Header (by Microsoft)

[[Microsoft Support - View internet message headers in Outlook](https://support.microsoft.com/en-us/office/view-internet-message-headers-in-outlook-cd039382-dc6e-4264-ac74-c048563d212c)]

## E-mail Header in Outlook

An email message internet header provides a list of technical details about the message, such as who sent it, the software used to compose it, and the email servers that it passed through on its way to the recipient.
Most of the time, only an administrator will need to view internet headers for a message.
If you want to add a header to your email message, see Apply stationery, backgrounds, or themes to email messages.

Some senders use spoofing to disguise their email address.
By checking the header, you can find out if the email address is different than it appears, and add it to your blocked senders list.

1. Double-click an email message to open it outside of the Reading Pane.

2. Click **File** > **Properties**.

3. Header information appears in the Internet headers box.

## Contents of email headers

Consider an email exchange between two people, Anton Kirilov and Kelly J. Weadock.
Anton's email address is anton@proseware.com and Kelly's address is kelly@litwareinc.com.
Kelly uses Microsoft Office Outlook 2007.
The Internet header associated with Kelly's message to Anton looks as follows:

```
Microsoft Mail Internet Headers Version 2.0Received: from mail.litwareinc.com ([10.54.108.101]) by mail.proseware.com with Microsoft SMTPSVC(6.0.3790.0);Wed, 12 Dec 2007 13:39:22 -0800Received: from mail ([10.54.108.23] RDNS failed) by mail.litware.com with Microsoft SMTPSVC(6.0.3790.0);Wed, 12 Dec 2007 13:38:49 -0800From: "Kelly J. Weadock" <kelly@litware.com>To: <anton@proseware.com>Cc: <tim@cpandl.com>Subject: Review of staff assignmentsDate: Wed, 12 Dec 2007 13:38:31 -0800MIME-Version: 1.0Content-Type: multipart/mixed;X-Mailer: Microsoft Office Outlook, Build 12.0.4210X-MimeOLE: Produced By Microsoft MimeOLE V6.00.2800.1165Thread-Index: AcON3CInEwkfLOQsQGeK8VCv3M+ipA==Return-Path: kelly@litware.comMessage-ID: <MAILbbnewS5TqCRL00000013@mail.litware.com>X-OriginalArrivalTime: 12 Dec 2007 21:38:50.0145 (UTC)
```

> **Note:** The sample header might not contain all items found in your email headers. These are the most common entries.

When Kelly sends an email message to anton@proseware.com, she composes it from her computer, which is identified as (i101-177.nv.litwareinc.com).
The composed text is passed from her computer to the email server, mail.litwareinc.com.
This is the last that Kelly will see of her email message, because further processing is handled by email servers with no intervention from her.
When Kelly's email server receives the message for anton@proseware.com, it contacts Proseware's email server and delivers the message to it.
The message is stored on the proseware.com server until Anton checks his Proseware email messages.

## Interpreting email headers

The following is an explanation of the common email header fields.

Header added by Outlook.

```
Microsoft Mail Internet Headers Version 2.0
```

```
Received: from mail.litwareinc.com ([10.54.108.101]) by mail.proseware.com with Microsoft SMTPSVC(6.0.3790.0);
Tue, 12 Dec 2017 13:39:22 -0800
```

This information says that the message transfer occurred on Tuesday, December 12, 2017, at 13:39:22 (1:39:22 in the afternoon) Pacific Standard Time (which is 8 hours later than Coordinated Universal Time (Greenwich Mean Time); thus the "–0800").

```
Received: from mail ([10.54.108.23] RDNS failed) by mail.litware.com with Microsoft SMTPSVC(6.0.3790.0);
Tue, 12 Dec 2017 13:38:49 -0800
```

This message transfer occurred on Tuesday, December 12, 2017, at 13:38:49 (1:38:49 in the afternoon) Pacific Standard Time (which is 8 hours later than Coordinated Universal Time (UTC); thus the "–0800").

```
From: "Kelly J. Weadock" <kelly@litware.com>
```

This message was sent by Kelly J. Weadock from the email address kelly@litware.com.

```
To: <anton@proseware.com>
```

This is the person to whom the email message is addressed.

```
Cc: <tim@cpandl.com>
```

These are the person or persons who receive carbon copies of the message.

> **Note:** Recipients of blind carbon copies (Bcc) do not appear in the header.

```
Subject: Review of staff assignments
```

This is the subject of the email message.

```
Date: Tue, 12 Dec 2017 13:38:31 -0800
```

This indicates the date and time that the email message was sent, based upon the computer clock on the sender's computer.

```
MIME-Version: 1.0
```

This parameter specifies the version of the MIME protocol that was used by the sender.

```
Content-Type: multipart/mixed;
```

This is an additional MIME header. It tells MIME-compliant email programs about the type of content to expect in the message.

```
X-Mailer: Microsoft Office Outlook, Build 12.0.4210
```

This information indicates that the message was sent by using Microsoft Office Outlook with a build version of 12.0.4210.

```
X-MimeOLE: Produced By Microsoft MimeOLE V6.00.2800.1165
```

This entry indicates the email software (MIME OLE software) used by the sender.

```
Thread-Index: AcON3CInEwkfLOQsQGeK8VCv3M+ipA==
```

This header is used to associate multiple messages with a similar thread. For example, in Outlook, the conversation view uses this information to find messages from the same conversation thread.

```
Return-Path: kelly@litware.com
```

This entry specifies how to reach the message sender.

```
Message-ID: <MAILbbnewS5TqCRL00000013@mail.litware.com>
```

The message has been assigned this number by mail.litware.com for identification purposes. This ID will always be associated with the message.

```
X-OriginalArrivalTime: 12 Dec 2017 21:38:50.0145 (UTC)
```

This is a time stamp placed on the message when it first passes through a server running Microsoft Exchange.
