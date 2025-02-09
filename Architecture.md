# Architecture

[Previous](Vocabulary.md) | [Table of contents](README.md) | [Next](Interface.md)
***

Architecture plays a very important role in enabling interoperability. It describes the organizational structure of concepts, processes, and assets, including data and workflows.
It comprises structural aspects of models and standards that govern the collection, storage, arrangement, integration, and use of data, based on which interoperability of data
and services are built on.

Following Architecture has impact on Interoperbility:

1) Data Architecture
2) Cloud Computing Architecture
3) Data Analytics Architecture

## Data Architecture

This section will talk about data and information archival and preservation.

The primary purpose of data archiving is to preserve data over time. Preserving data over time consists in holding data in repositories in a way which enables data to be available,
retrievable and usable even many years after the time it was produced. Data archiving is not only a long-term process, it is also a complex process with possibly many partners: data
providers supplying data to the archive, data users willing to use the archive, archive managers organizing the archive, other archives with which interoperability may be sought.

The following list of recommendations describes the elements contributing to archive interoperability.

| **ID**   | **Recommendations**                                                                                                                                                                                                                                                                                                                                                                   |
| :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| DSTOR#1  | Use a same glossary of terms and definitions applicable to data archiving.                                                                                                                                                                                                                                                                                                            |
| DSTOR#2  | An archive system should comply with the Reference Model for an [“Open Archival Information System” (OAIS)](https://public.ccsds.org/pubs/650x0m2.pdf), and to the OAIS-Interoperability Framework to facilitate the interoperability between archives.                                                                                                                               |
| DSTOR#3  | An archive should use a questionnaire to help archivists in appraising data that are candidates for archiving.                                                                                                                                                                                                                                                                        |
| DSTOR#4  | CEOS agencies should use the purge alert service before data and information removal from archives.                                                                                                                                                                                                                                                                                   |
| DSTOR#5  | Keep archives equipment in conformance with manufacturer recommendations.                                                                                                                                                                                                                                                                                                             |
| DSTOR#6  | Pursue a harmonised approach within the Earth Observation community for the future development of archiving systems to improve compatibility of services provided by different organisations.                                                                                                                                                                                         |
| DSTOR#7  | Carry out data ingestion according to relevant standards with documented tailoring and definition derived from the generic activities described in the standards.                                                                                                                                                                                                                     |
| DSTOR#8  | Perform periodically a migration of the archived data (“media refreshment”) to the most adequate proven technology for data storage ensuring long term data preservation.                                                                                                                                                                                                             |
| DSTOR#9  | Maintain formal descriptions of data and information archiving formats.                                                                                                                                                                                                                                                                                                               |
| DSTOR#10 | Perform archived data and information repackaging and/or reformatting to comply with new standard formats and/or exchange formats to increase technical compatibility and to reduce diversity of formats and interfaces between archives.                                                                                                                                             |
| DSTOR#11 | Carry out data preservation according to relevant standards and internationally recognised best practices with documented tailoring and definition derived from the generic activities described in the standards.                                                                                                                                                                    |
| DSTOR#12 | Perform periodical technology trend analysis to better manage the migration of archive system relevant components to new hardware platforms.                                                                                                                                                                                                                                          |
| DSTOR#13 | Periodically verify the integrity of the archive collection/content through integrity check on a representative set of the archived data.                                                                                                                                                                                                                                             |
| DSTOR#14 | Ensure that the content of the archived data and associated information remains unchanged and, if changes are made, that these are documented and that this documentation is preserved and made available as well (provenance information).                                                                                                                                           |
| DSTOR#15 | Apply the [FAIR principles](https://www.go-fair.org/fair-principles/ ) to pursue data and metadata interoperability:<br> - I1. (Meta)data use a formal, accessible, shared, and broadly applicable language for knowledge representation; <br> - I2. (Meta)data use vocabularies that follow FAIR principles; <br> - I3. (Meta)data include qualified references to other (meta)data. |
| DSTOR#16 | Confirm data archive and/or disposal at end-of-life at publication stage.                                                                                                                                                                                                                                                                                                             |
| DSTOR#17 | Assign a Persistent Identifier to data archived and published to users and ensure the availability of all associated information in the relevant Landing Page.                                                                                                                                                                                                                        |

## Cloud Computing Architecture

The Cloud computing architecture supports standardized API, protocols and provides capability for  publishing resources as services, this enables seamless integration of data and services irrespective of the underlying architecture and location

| **ID**       | **Recommendations**                                                                                                                                 |
| :----------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CLOUD\#1** | The data to be shared through cloud should be converted to cloud optimized formats for faster and interoperable access across multiple applications |
| **CLOUD\#2** |                                                                                                                                                     |
| **CLOUD\#3** |                                                                                                                                                     |
| **CLOUD\#4** |                                                                                                                                                     |
| **CLOUD\#5** |                                                                                                                                                     |
| **CLOUD\#6** |                                                                                                                                                     |

## Analytics Architecture

Data Analytics architecture in an organization provides capability to store, analyze and visualize the data. As a typical Earth Observation data analytics require a large volume of time series data and hence
it is necessary to support interoperability in the analytics architecture using following recommendations.

### Analysis Ready Data

Analysis Ready Data (ARD) are starting point for interoperability in analysis and hence Data Providers are encouraged to develop ARD.

#### ARD Recommendations

| **ID**     | **Recommendations**                                                                                                                                                                |
| :--------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **ARD\#1** | CEOS ARD Framework should be used as a starting point for development of Analysis Ready Data                                                                                       |
| **ARD\#2** | CEOS Product Family Specifications (PFS) should be used for development of ARD products. In case if a new ARD is to be developed, use PFS template and submit to CEOS for approval |
| **ARD\#3** | CEOS ARD compliance of the product requires two level of assessments, first is self assessment (CEOS ARD Self Assessment Guide)  and second is peer review by CEOS Experts         |
| **ARD\#4** |                                                                                                                                                                                    |
| **ARD\#5** |                                                                                                                                                                                    |

### Datacube

Data Cube provide capability to pack a collection of data and provide capability for fast access and analysis.

#### Datacube Recommendations

| **ID**       | **Recommendations**                                                                                                                                                                   |
| :----------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **DCUBE\#1** | The CEOS supported [Open Data Cube](https://opendatacube.org) can be taken as a reference for Datacube implementation                                                                 |
| **DCUBE\#2** | Data cubes should support spatial and/or temporal dimensions and capability for publishing available variables/properties as metadata                                                 |
| **DCUBE\#3** | Data cubes should abstract the underlying data storage architecture to support hybrid data cubes and interoperability among different types of data cubes                             |
| **DCUBE\#4** | Data cube may contain raw sensor data, analysis ready data or decision ready information. Analysis Reay Data  should be preferred to avoid pre-processing overheads and fast analysis |
| **DCUBE\#5** | Data cubes should be able to publish the supported pre-built analysis functions                                                                                                       |
| **DCUBE\#6** | Data Cubes should provide REST API and OGC web services based access for easy integration of end user applications                                                                    |

***
[Previous](Vocabulary.md) | [Table of contents](README.md) | [Next](Interface.md)
