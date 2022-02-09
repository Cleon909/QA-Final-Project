Academic Journal Database

Links to Jira and Risk assesment go here.

Contents



Brief
To create a web application that integrates with a database and demonstrates CRUD functionality.
-   database must contain two entities with some relationship

To utilise containers to host and deploy your application.
To create a continuous integration (CI)/continuous deployment (CD) pipeline that will automatically test, build and deploy your application.



Academic Journal Database

this is a many to many relational database, which as SQL doesn't accomdate contains a child table 

Academics class
contains first, and last name of academic and generates an ID(as a prinmary key)
also contains their current institution and field of study

papers class
contains title of the paper and an auto generated ID(as a primary key)
also the date published, the field of study, and impact(which is a measure of how often the paper has been cited by other papers, for the purposes of this the number is completely made up)

authors class
this is a child table with only two columns, both foreign keys. Academic_ID, and paper_ID. There's no need for a foreign key as the only way there could be duplicate lines is if the same author was put on the same paper more than once, so I woll control for that in code.


web app pages

home page will be the main read page. from here you will be able to search the database and filter your searches further. Will also contain links to an update/create and delete pages

searches should cover:

    -   search author, by pull down menu(or substring search) return all their jointly authored pages
    -   search paper, by pull down menu(or substring search) return all authors
    -   academic + academic returns any jointly authored papers
    -   field of study by pull down menu, either all academics in that field or all papers
    -   academic + field of study return all papers written by academic in that field
    -   institution pull down menu returns all academics in that institution, don't want to link that to papers, too messy (multiple academics from multiple institutions working on one paper)
    -   filter all searches on papers (i.e. papers + field of study, or papers + academic etc) by impact. search by the most or least impactful


create page

    -   academics can be created without any papers but papers must have at least one author (database design doen't mandate this so will have to be explicitle enforced)
    -   academics can have no institution of field of study (polymaths!) // stretch goals is to move field of study to another table and then academics could have multiple fields, papers could also have multiple (epics)
    -   when creating papers multiple authors will have to be selected and these id's will be added to the authors(child) table, along with the paper ids
    -   //stretch goal to add a institution table which would be one to one with academics. would allow use to create instition. otherwise ability to amend would just be to already selected institutions or typing new ones in which would lead to typos and duplicates

update function

    -   change academic name (maybe they are trans, got married etc)
    -   change academic's institution (type it in unless I have time for a seperate table, if so then must also be able to add to table)
    -   change academic's field of study
    
    -   change papers authors (from a pul down list, and it must also change the details in teh child table)
    -   change paper impact
    -   change papers title and field of study (shouldn't really be a need to do this, maybe do fix inputting errors?)

delete function

    -   delete academic, however if academic last author related to a paper the paper must be deleted as well. if not then just remove academic and any related objects in the child table
    -   delete paper and any related objects in child table




-requirements

Building the application

- project planning

- front end
-
testing
- test details go here

other stuff in due time
