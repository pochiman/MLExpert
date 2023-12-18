# Data Support

# 2 - Data Ingestion

In order to do anything with a machine-learning system, you first need to feed it 
some inputs. In this first video of the series, we'll look at technologies you can 
use to ingest data into your systems and review some considerations you can make 
throughout this process.

Let's dive in!

# Key Terms

# [Clickstream]
An ordered series of interactions that users have with some interface. In the 
traditional sense, this can be literal clicks of a mouse on a desktop browser. 
Interactions can also come from touchscreens and conversational user interfaces.

# [Change_Data_Capture]
  The process of recording changes in the data within a database system. For
  instance, if a user cancels their Netflix subscription, then the row in some
  table will change to indicate that they're no longer a subscriber.

  The change in this row can be recorded and referenced later for analysis or
  audit purposes.

# [Apache_Kafka] ϟ
  An open-source software platform which provides a way to handle real-time data
  streaming.

# [Amazon_Kinesis] ϟ
  An AWS product that provides a way to handle real-time data streaming.

# [Zookeeper] ϟ
  A service designed to reliably coordinate distributed systems via naming
  service, configuration management, data synchronization, leader election,
  message queuing, or notification systems.

# [Database]
  A tool used to collect and organize data. Typically, database management
  systems allow users to interact with the database.

# [OLTP]

  Online transaction processing. A system that handles (near) real-time business
  processes. For example, a database that maintains a table of the users
  subscribed to Netflix and which is then used to enable successful log-ins
  would be considered OLTP. This is opposed to OLAP.

# [OLAP]

  Online analytical processing. A system that handles the analytical processes
  of a business, including reporting, auditing, and business intelligence. For
  example, this may be a Hadoop cluster which maintains user subscription
  history for Netflix. This is opposed to OLTP.

# [Availability_Zone_(AZ)]

  Typically a single data center within a region which has two or more data
  centers. The term "multi-AZ" implies that an application or software resource
  is present across more than one AZ within a region. This strategy allows the
  software resource to continue operating even if a data center becomes
  unavailable.
