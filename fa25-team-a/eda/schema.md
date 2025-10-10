# Team A Act on MASS Database Schema

In order to properly achieve the goal of creating visualizations that a user can interact with and track a particular representative's voting patterns, the following database schemas have been defined.

**Note**: This document outlines an ideal scenario for building a fully fleshed out version of the project. There is always the possibility that due to constraints of the semester or data availability that we may not be able to complete everything. This document serves to outline the initial plans and further documentation will record decision making along the way based on progression of the project.

## Entities

To build a relational database, it is important to define the entities and their relationships that are contained in the data. This data set consists of the following entities:

* Representatives (House and Senate)
* Bills

## Relationships between entities

With entities clearly defined, the following relationships can be established:

* Representatives to bills - Many to many. A bill is voted on by many representatives and a representative votes on many different bills. This relationship functions as a Junction table in our schema so that a bill can be easily mapped to multiple representative by their ids and votes can be stored in a single table.

## Proposed Tables

First, the primary tables containing critical information about each entity is created

### Representative

```sql
CREATE TABLE Representatives(
    rep_id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(50) NOT NULL,
    party_affiliation VARCHAR(50) NOT NULL,
    branch VARCHAR(20) NOT NULL,
    district VARCHAR(50),
    begin_year INT NOT NULL,
    end_year INT
);
```

### Bill

```sql
CREATE TABLE Bill(
    bill_id INT PRIMARY KEY AUTO_INCREMENT,
    bill_name VARCHAR(100) NOT NULL
);
```

### Category

These categories were arbitrarily designed by our team to classify bills in a way that can be used to sort bills by topic. In doing this, we are able to create visualizations that a user can use to not only track how a representative voted generally, but also by topics of interest.

```sql
CREATE TABLE Categories(
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(50)
)
```

### Bill-Category Junction Table

Because bills and categories have a many-to-many relationship, a junction table is used to map the categories a bill is classified as.

```sql
CREATE TABLE BillCategory(
    bill_id INT NOT NULL,
    category_id INT NOT NULL,
    CONSTRAINT PK_BillCategory PRIMARY KEY (bill_id, category_id),
    FOREIGN KEY (bill_id) REFERENCES Bill (bill_id),
    FOREIGN KEY (category_id) REFERENCES Category (category_id)
)
```

[US Congress](https://www.congress.gov/help/find-bills-by-subject) uses the following categories for classifying bills:

* Agriculture and Food
* Animals
* Armed Forces and National Security
* Arts, Culture, Religion
* Civil Rights and Liberties, Minority Issues
* Commerce
* Congress
* Crime and Law Enforcement
* Economics and Public Finance
* Education
* Emergency Management
* Energy
* Environmental Protection
* Families
* Finance and Financial Sector
* Foreign Trade and International Finance
* Government Operations and Politics
* Health
* Housing and Community Development
* Immigration
* International Affairs
* Labor and Employment
* Law
* Native Americans
* Public Lands and Natural Resources
* Science, Technology, Communications
* Social Welfare
* Sports and Recreation
* Taxation
* Transportation and Public Works
* Water Resources Development

Since this list is extensive and some categories do not apply at the state level, the list of categories will be pared down by the team. Additionally, categorization of bills is a stretch goal beyond the scope of the initial minimally viable product so this work will be held until later in the project lifecycle for now.

### Vote Types Enum Table

A simple enum table is added to store the types of votes made by each representative. While not necessary, it is preferable to use an integer to store the vote type instead of the repeated strings such as "Not Voting" or "Present", especially given the expected length of the Votes table.

```sql
CREATE TABLE Enum_Vote_Types(
    id INT PRIMARY KEY AUTO_INCREMENT,
    vote_name VARCHAR(20) UNIQUE NOT NULL
)
```

### Votes Junction Table

The many-to-many relationship between representatives and bills is mapped in the Votes table. Beyond the composite primary key made of bill_id and rep_id, additional data is stored with each vote to track

```sql
CREATE TABLE Votes(
    bill_id INT NOT NULL,
    rep_id INT NOT NULL,
    vote_id INT NOT NULL,
    after_vote BIT NOT NULL DEFAULT 0,
    CONSTRAINT PK_BillRepresentative PRIMARY KEY (bill_id, rep_id),
    FOREIGN KEY (bill_id) REFERENCES Bill (bill_id),
    FOREIGN KEY (rep_di) REFERENCES Representative(rep_id),
    FOREIGN KEY (vote_id) REFERENCES Enum_Vote_Types(id)
);
```

