# Architecture

[Previous](Vocabulary.md) | [Table of contents](README.md) | [Next](Interface.md)
***

Architecture plays a very important role in enabling interoperability. It describes the organizational structure of concepts, processes, and assets,
including data and workflows. It comprises structural aspects of models and standards that govern the collection management, storage, arrangement,
integration, and use of data, and is the basis on which the interoperability of data and services is built on.

Following Architecture has impact on Interoperability:

1) Data Architecture
2) Metadata Architecture
3) Cloud Architecture
4) Publishing Architecture
5) Technologies

## Data Architecture

This section covers the core recommendations for data production, management, archiving and deletion.

The primary purpose of data archiving is to preserve data over time. Preserving data over time consists in holding data in repositories in a way
that enables data to be managed and accessed now and in the future. Data archiving is not only a complex, long-term process, with possibly many
partners: data providers supplying data to the archive, data users willing to use the archive, archive managers organizing the archive, other archives
with which interoperability may be sought. Data management and archiving should consider not just the storage of data, but also the access and usage
patterns of data.

The following list of recommendations describes the elements contributing to archive interoperability.

| **ID**      | **Recommendations**                                                                                                                                                                                                                                     |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **DATA#01** | Use a the CEOS Common Dictionary of terms and definitions applicable to data archiving.                                                                                                                                                                 |
| **DATA#02** | An archive system should comply with the Reference Model for an [“Open Archival Information System” (OAIS)](https://public.ccsds.org/pubs/650x0m2.pdf), and to the OAIS-Interoperability Framework to facilitate the interoperability between archives. |
| **DATA#03** | An archive should use a questionnaire to help archivists in appraising data that are candidates for archiving.                                                                                                                                          |
| **DATA#04** | CEOS agencies should use the purge alert service before data and information removal from archives.                                                                                                                                                     |
| **DATA#05** | Archives equipment should be kept in conformance with manufacturer recommendations.                                                                                                                                                                     |
| **DATA#06** | Pursue a harmonized approach within the Earth observation community for the future development of archiving systems to improve compatibility of services provided by different organizations.                                                           |
| **DATA#07** | Carry out data ingestion according to relevant standards with documented tailoring and definition derived from the generic activities described in the standards.                                                                                       |
| **DATA#08** | Perform periodically a migration of the archived data (“media refreshment”) to the most adequate proven technology for data storage ensuring long term data preservation.                                                                               |
| **DATA#09** | Maintain formal descriptions of data and information archiving formats.                                                                                                                                                                                 |
| **DATA#10** | Perform archived data and information repackaging and/or reformatting to comply with new standard formats and/or exchange formats to increase technical compatibility and to reduce diversity of formats and interfaces between archives.               |
| **DATA#11** | Carry out data preservation according to relevant standards and internationally recognized best practices with documented tailoring and definition derived from the generic activities described in the standards.                                      |
| **DATA#12** | Perform periodical technology trend analysis to better manage the migration of archive system relevant components to new hardware platforms.                                                                                                            |
| **DATA#13** | Periodically verify the integrity of the archive collection/content through integrity check on a representative set of the archived data.                                                                                                               |
| **DATA#14** | Ensure that the content of the archived data and associated information remains unchanged and, if changes are made, that these are documented and that this documentation is preserved and made available as well (provenance information).             |
| **DATA#15** | Apply the [FAIR principles](https://www.go-fair.org/fair-principles/) to pursue data and metadata interoperability                                                                                                                                      |
| **DATA#16** | Assign a Persistent Identifier to data archived and published to users and ensure the availability of all associated information in the relevant Landing Page.                                                                                          |
| **DATA#17** | Maintain at least two copies of at least the core data products, using a strategy like the [3-2-1 Backup Strategy](https://www.backblaze.com/blog/the-3-2-1-backup-strategy/)                                                                           |
| **DATA#18** | CEOS ARD Framework should be used as a starting point for development of Analysis Ready Data                                                                                                                                                            |
| **DATA#19** | CEOS Product Family Specifications (PFS) should be used for development of ARD products. In case if a new ARD is to be developed, use PFS template and submit to CEOS for approval                                                                      |
| **DATA#20** | CEOS ARD compliance of the product requires two level of assessments, first is self assessment (CEOS ARD Self Assessment Guide)  and second is peer review by CEOS Experts                                                                              |

## Metadata Architecture

Metadata architecture covers the packaging (grouping of a granule/scene/STAC Item) of a single set of data, and the structure of the accompanying metadata
and other ancillary documents that help describe the granule. It also covers collection-level metadata.

| **ID**          | **Recommendations**                                                                                                                   |
| :-------------- | :------------------------------------------------------------------------------------------------------------------------------------ |
| **METADATA#01** | The ISO 19115 series of standards should be used for geospatial metadata at the collection level                                      |
| **METADATA#02** | A Collection of data should have all granules packaged consistently and produced with consistent quality.                             |
| **METADATA#03** | Collection-specific metadata formats may be used, but packaging must include STAC documents at the Collection and Granule/Item level  |
| **METADATA#04** | Hashes for all files in a packaged granule should be available, so that integrity checks can be run                                   |
| **METADATA#05** | Pixel-level metadata such as scene quality masks should be clearly documented with a reference to lookup tables                       |
| **METADATA#06** | File names and folder or path structures should be consistent and include appropriate information to distinguish the specific granule |

## Cloud Architecture

The Cloud architecture includes a range of recommendation to be used when managing data for interoperability on the cloud.

| **ID**       | **Recommendations**                                                                                                                                                                              |
| :----------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CLOUD\#1** | The data to be shared through cloud should be converted to cloud optimized formats for faster and interoperable access across multiple applications                                              |
| **CLOUD\#2** | Granules must not be zipped when shared via the cloud, so that cloud optimized data formats can be leveraged                                                                                     |
| **CLOUD\#3** | Where possible, cloud providers' standard as-a-service offerings should be used in preference to self-developed solutions, enabling interoperability of tools that work with that cloud provider |
| **CLOUD\#5** | Intermediation of a cloud provider's object store is discouraged, meaning that if possible, direct access using the service's APIs should be available                                           |
| **CLOUD\#6** | When possible, internal tooling and web services that are not a security of privacy risk should be made open source and openly accessible                                                        |

## Publishing Architecture

Publishing recommendations involve the final stage in making data accessible to external organizations or individuals. These recommendations
are aimed at facilitating both access to data as well as maintaining a replica of part or all of a collection of data.

| **ID**         | **Recommendations**                                                                                                                                                                                                                     |
| :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **PUBLISH\#1** | Granules should be available immediately and not through an on-demand service                                                                                                                                                           |
| **PUBLISH\#2** | Each data collection that is published as a publicly-accessible product should include a public granule-level notification including for when it is added, updated or deleted/archived. This should be able to be filtered by location. |
| **PUBLISH\#3** | A collection should have a full listing of all available granules in a standard format, preferably cloud optimized. [STAC-geoparquet](https://stac-utils.github.io/stac-geoparquet/latest/) is used by some providers currently         |
| **PUBLISH\#4** | Data licensing should be clear and adhere to national policies, with a strong preference for standard open licenses such as Creative Commons                                                                                            |

## Technologies

A range of specific technologies including software applications and service specifications are currently in wide use and can be used to
access collections of data that are published using them. The list below includes examples of these technologies.

| **ID**      | **Recommendations**                                                                                                                                                                |
| :---------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **TECH\#1** | The CEOS supported [Open Data Cube](https://opendatacube.org) can be taken as a reference Datacube implementation                                                                  |
| **TECH\#1** | Collection and Granule metadata should be accessible in a REST API that implements the OGC API for Features, such as the [STAC API](https://github.com/radiantearth/stac-api-spec) |
| **TECH\#2** | Datacubes can be created on the fly using client applications working against a REST API, for example, using [odc-stac](https://github.com/opendatacube/odc-stac)                  |
| **TECH\#4** | [OGC APIs](https://ogcapi.ogc.org/) should be used to publish web services for visualisation and data access                                                                       |

Requirement of Analytics Architecture is to be discussed

***
[Previous](Vocabulary.md) | [Table of contents](README.md) | [Next](Interface.md)
