# HBase_ETL_happybase
Simple python program inserting data - text doc - into Hbase using happybase. Happybase provides a user-friendly framework for *Extracting, Transforming & Loading* (ETL) data. 

# Requirements
In order to use or replicate this example, you need access to an *hadoop* stack. **Horton Works** - who recently merged with **Cloudera** provides a free *VM*. To download this *VM* first download the oracle virtual box 6.0 (at the time of this doc) [here](https://www.virtualbox.org/) & install the version that suites your need - this step will enable you to run a linux virtual box on your PC.The next step item that's needed is an image of *hadoop* - to download this follow [this] (https://www.cloudera.com/downloads.html) & select **Hortonworks Sandbox** then select **Hortonworks HDP** then choose **VirtualBox** under installation type & hit **lets go**. WARNING: The installation may take a while depending on your PC. I recommend installing version **2.5.0** rather than more recent versions - the latter is more reliable & requires less resources. The quirk associated with **2.5.0** version however is that its more painfull installing *Python* libraries. Once the installation is complete, you will have an instance running - to start the virtual machine, click on the green arrow button.

# How this works
