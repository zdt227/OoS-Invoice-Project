# OoS-Invoice-Project

There is a lot of spaghetti code at this moment, but the core functionality is being built.

Completed Tasks:
* Create an object to hold invoice objects
* Create an array which can hold the invoices
* Transfer contents of invoice array into an excel spreadsheet and properly format parameters
* Implement Google Document API to access invoice processser for sysco branded invoices
* Output invoice contents to text file
* Properly format the text file and extract invoice items into the array

To-do:
* Modify invoice parsing code so it can work with pdfs which span multiple pages
* Fine-tune invoice processor for sysco
* Develop invoice processors for all other brands used by Lehigh
* Optimize code where possible to bring performance closer to O(N) rather than O(N^2)
