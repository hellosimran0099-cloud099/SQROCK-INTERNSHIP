SQL Injection Overview

SQL Injection is an application-security problem in which untrusted input can interfere with the intended structure of a SQL statement when the application constructs queries unsafely.

For the Day 18 defensive lab, the objective is to detect indicators in access logs, rather than perform an SQL Injection attack. The supplied lab identifies patterns such as ', --, #, UNION SELECT, and logical expressions such as OR 1=1 as signatures that can be searched for in logs.

Unparameterized SQL

An unparameterized query may conceptually construct SQL by combining the SQL statement with user input:

For example, conceptually:

The important issue is that data and SQL syntax are not reliably separated.

If an application treats untrusted input as part of the SQL statement, specially crafted input can potentially affect the interpretation of the query.

Execution concept
Security concern

The database may interpret parts of the supplied input as SQL syntax rather than simply as data.

Secure Prepared Statements

A Prepared Statement separates the SQL statement from the values supplied by the user.

Conceptually:

Instead of constructing one SQL string containing everything, the application defines the SQL structure and supplies user input as a parameter.

Execution concept

The key security principle is:

SQL code and user-supplied data are treated separately.

This is why Prepared Statements are the secure approach discussed in the Day 18 deliverable.

 Execution Difference
Feature	Unparameterized SQL	Prepared Statement
Query construction	SQL + input combined	SQL structure + parameter separated
User input	Can become part of SQL syntax	Treated as a parameter/value
Query structure	Can be affected by unsafe input	Remains defined separately
SQL Injection risk	Higher when input is concatenated unsafely	Designed to prevent input from changing query structure
Security approach	Unsafe for untrusted input	Recommended approach
Main principle	String construction	Parameter binding
 Practical Difference
Unparameterized approach

The problem is that the input is incorporated directly into the SQL statement.

Prepared Statement approach

The query structure is established separately from the user-provided value.

Relationship Between Log Detection and Prepared Statements

These are two different defensive layers.

Prepared Statements

Prevent SQL Injection at the application/database interaction layer.

Log Detection

Detects suspicious patterns at the monitoring/log-analysis layer.

Therefore, a secure application should not rely only on log detection. Prepared Statements help prevent unsafe query construction, while log analysis provides monitoring and detection capabilities.
