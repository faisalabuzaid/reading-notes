
<h2>Database normalization</h2>
<p>
  Database Normalization is a process and it should be carried out for every database you design. The process of taking a database design, and apply a set of formal criteria and rules, is called Normal Forms.
</p>
<p>
  The database normalization process is further categorized into the following types:
</p><ol><li>
  First Normal Form (1 NF)
</li><li>
  Second Normal Form (2 NF)
</li><li>
  Third Normal Form (3 NF)
</li><li>
  Boyce Codd Normal Form or Fourth Normal Form ( BCNF or 4 NF)
</li><li>
  Fifth Normal Form (5 NF)
</li><li>
  Sixth Normal Form (6 NF)
</li></ol>

 ![image1](https://www.sqlshack.com/wp-content/uploads/2018/11/word-image-374.png)
<p>
  One of the driving forces behind database normalization&nbsp;is to streamline data by reducing redundant data.&nbsp;Redundancy of data means there are&nbsp;multiple copies of the same information spread over multiple locations in the same database.&nbsp;
</p>
<p>
  The drawbacks of data redundancy include:
</p><ol><li>
  Data maintenance becomes tedious – data deletion and data updates become problematic
</li><li>
  It creates data inconsistencies 
</li><li>
  Insert, Update and Delete anomalies become frequent. An update anomaly, for example, means that the versions of the same record, duplicated in different places in the database, will all need to be updated to keep the record consistent
</li><li>
  Redundant data inflates the size of a database and takes up an inordinate amount of space on disk
</li></ol><h2>Normal Forms</h2>
<p>
  This article is an effort to provide fundamental details of database normalization. The concept of normalization is a vast subject and the scope of this article is to provide enough information to be able to understand the first three forms of database normalization.
</p><ol><li>
  First Normal Form (1 NF)
</li><li>
  Second Normal Form (2 NF)
</li><li>
  Third Normal Form (3 NF)
</li></ol>
<p>
  A database is considered third normal form if it meets the requirements of the first 3 normal forms.
</p><h3>First Normal Form (1NF):</h3>
<p>
  The first normal form requires that a table satisfies the following conditions:
</p><ol><li>
  Rows are not ordered
</li><li>
  Columns are not ordered
</li><li>
  There is duplicated data
</li><li>
  Row-and-column intersections always have a unique value
</li><li>
  All columns are “regular” with no hidden values
</li></ol>
<p>
  In the following example, the first table clearly violates the 1 NF. It contains more than one value for the Dept column. So, what we might do then is go back to the original way and instead start adding new columns, so, Dept1, Dept2, and so on. This is what’s called a repeating group, and there should be no repeating groups. In order to bring this First Normal Form, split the table into the two tables. Let’s take the department data out of the table and put it in the dept table. This has the one-to-many relationship to the employee table.
</p>
<p>
  Let’s take a look at the employee table:
</p>

  ![image](https://www.sqlshack.com/wp-content/uploads/2018/11/word-image-375.png)
<p>
  Now, after normalization, the normalized tables Dept and Employee looks like below:
</p>

  ![image3](https://www.sqlshack.com/wp-content/uploads/2018/11/word-image-376.png)

<p>
  Second Normal Form and Third Normal Form are all about the relationship between the columns that are the keys and the other columns that aren’t the key columns.
</p><h3>Second Normal Form (2NF):</h3>
<p>
  An entity is in a second normal form if all of its attributes depend on the whole primary key. So this means that the values in the different columns have a dependency on the other columns.
</p><div class="mailmunch-forms-in-post-middle" style="display: none !important;"></div><ol><li>
  The table must be already in 1 NF and all non-key columns of the tables must depend on the PRIMARY KEY
</li><li>
  The partial dependencies are removed and placed in a separate table
</li></ol>
<p>
  Note:  Second Normal Form (2 NF) is only ever a problem&nbsp;when we’re using a composite primary key.&nbsp;That is, a primary key made of two or more columns.
</p>
<p>
  The following example, the relationship is established between the Employee and Department tables.
</p>
