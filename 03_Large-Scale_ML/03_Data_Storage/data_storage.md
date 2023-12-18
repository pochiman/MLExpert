# Data Support

# 3 - Data Storage

If you've gone through our Systems Design Fundamental series, then you know how 
important having a high-performing storage model is to any system.

And guess what? Massive, computationally-intense ML systems are certainly no 
exception!

# Key Terms

# [Hard_Disk_Drive_(HDD)]
A storage device which operates by setting bits on a spinning magnetic disk. The 
capacity and the read/write performance of the HDD are the main characteristics 
to consider when using an HDD within a particular system.

# [Data_Replication]
A strategy used to mitigate the potential of data loss in the event of a system 
or component failure. In the most basic form, it involves writing identical data 
to more than one device or location. More efficient techniques like erasure coding 
incorporate mathematics to recover lost data without referring to an explicit copy 
of the data. 
    
# [Hadoop_Distributed_File_System_(HDFS)]
An open-source Apache software product which provides a distributed storage 
framework.

# [Avro]
A row-oriented data serializer provided by Apache.

# [Parquet]
A column-oriented data storage format provided by Apache.
    
# [Exactly-once_Semantics]
Guarantees that an object within a distributed system is processed exactly once. 
Other semantics include maybe, at-least-once, and at-most-once
