# Architecture

[Previous](Vocabulary.md) | [Table of contents](README.md) | [Next](Interface.md)
***

Architecture plays a very important role in enabling interoperability. It describes the organizational structure of concepts, processes, and assets,
including data and workflows. It comprises structural aspects of models and standards that govern the collection management, archiving, storage,
documentation and publishing of data, and is the basis on which the interoperability of data and services is built on.

The Architecture factor has been divided into the following sections:

1) Preservation Architecture
2) Data and Metadata Architecture
3) Publishing Architecture

## Preservation Architecture

The following list of recommendations describes the elements contributing to archive interoperability.

The primary purpose of data archiving is to preserve data over time. Preserving data over time consists in holding data in repositories in a
way that enables data to be managed and accessed now and in the future. Data archiving is a complex, long-term process, with possibly
many partners, including data providers supplying data to the archive, data users willing to use the archive, archive managers organizing the
archive and other archives with which interoperability may be sought. Data management and archiving should consider not just the storage of data, but
also the access and usage patterns of data.

| **ID**      | **Recommendations**                                                                                                                                                                                                                                     |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **DPRES\#1** | Archival systems should comply with the Reference Model for an [Open Archival Information System](https://public.ccsds.org/pubs/650x0m2.pdf) (OAIS) and with the forthcoming “OAIS-Interoperability Framework” to facilitate interoperability between archives. |
| **DPRES\#2** | Data should be appraised and properly documented before ingestion in the archives following the [CEOS Data Appraisal Procedure](https://ceos.org/ourwork/workinggroups/wgiss/documents/). |
| **DPRES\#3** | Data and associated information should be ingested, archived and preserved following internationally recognised standards and best practices (e.g., those produced by [WGISS](https://ceos.org/ourwork/workinggroups/wgiss/documents/) and [Producer-Archive Interface Methodology Abstract Standard](https://public.ccsds.org/Pubs/651x0m1.pdf) ) with any tailoring documented. |
| **DPRES\#4** |  Periodically perform archival system/media upgrade to the most adequate proven technology to ensure data and information long term preservation. Perform migration, with an integrity check, of archived data from old to new systems.|
| **DPRES\#5** | Archive and preserve the information, code and software needed to handle the archived data, following the [CEOS guidelines](https://ceos.org/ourwork/workinggroups/wgiss/documents/).|
| **DPRES\#6** | When performing archived data and information repackaging and/or reformatting, for example to comply with new standard formats and/or exchange formats, properly document changes made to the archived data and ensure data integrity.  |
| **DPRES\#7** | Periodically verify the integrity of the archive collection/content through integrity check on a representative set of the archived data.|
| **DPRES\#8** | Manage evolution of archived data collections according to the [Shared Collection Lifecycle Management Principles for EO Data](https://ceos.org/ourwork/workinggroups/wgiss/documents/) best practice.  |
| **DPRES\#9** | Keep archives equipment (hardware and software) up-to-date and in conformance with vendor recommendations to preserve data and associated information integrity and facilitate interoperability between archives.|

## Data and Metadata Architecture

This section covers the core recommendations for collection management functions including data production, management, packaging and documentation.

| **ID**      | **Recommendations**                                                                                                                                                                                                                                     |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **DATA#1** | [CEOS-ARD Framework](https://ceos.org/ard) should be used as a starting point for development of Analysis Ready Data. |
| **DATA#2** | CEOS-ARD Product Family Specifications (PFS) should be used for development and assessment of ARD products, including both self-assessments and peer review. |
| **DATA#4** | The ISO 19115 series of standards (or similar) should be used to produce geospatial metadata. |
| **DATA#5** | A Collection of data should have all granules packaged consistently and produced with consistent quality. |
| **DATA#6** | Collection-specific metadata formats may be used, but packaging must also include STAC documents at the Collection and Granule/Item level. Refer to the [CEOS EO collection and granule discovery best practices with STAC](https://github.com/ceos-org/stac-collection-and-granule-discovery-best-practices). |
| **DATA#7** | Checksums for all files in a packaged granule should be available, to ensure integrity. |
| **DATA#8** | Where pixel-level metadata is avaliable, such as scene quality masks, these should be clearly documented with a reference to lookup tables. |
| **DATA#9** | File names and folder or path structures should be consistent and include appropriate information to distinguish the specific granule. This could include the platform, time and date of aquisition, band(s), and product version. |
| **DATA#10** | Assign a Persistent Identifier to data archived and published to users and ensure the availability of all associated information in the relevant Landing Page following the [CEOS Persistent Identifiers Best Practice](https://ceos.org/ourwork/workinggroups/wgiss/documents/). |
| **DATA#11** | The CEOS supported [Open Data Cube](https://opendatacube.org) family of software can be taken as a reference Datacube implementation. |

## Publishing Architecture

Publishing recommendations involve the final stage in making data accessible to external organizations or individuals. These recommendations are aimed at facilitating both access to data as well as maintaining a replica of part or all of a collection of data, including to be used when managing data for interoperability on the cloud.

| **ID**         | **Recommendations**                                                                                                                                                                                                                     |
| :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **PUBLISH\#1** | Each data collection that is published as a publicly-accessible product should include a public granule-level notification including for when a granule is added, updated and deleted/archived. This supports management and maintenance of replicas collections. |
| **PUBLISH\#2** | A collection should have a full listing of all available granules in a standard format, preferably cloud optimized. For example, [STAC-geoparquet](https://stac-utils.github.io/stac-geoparquet/latest/) is used by some providers. |
| **PUBLISH\#3** |  Granule data stored in the cloud should be accessible in cloud-optimized formats, e.g., [Zarr](https://en.wikipedia.org/wiki/Zarr_(data_format)) or [Cloud-Optimized GeoTIFF (COG)](https://en.wikipedia.org/wiki/GeoTIFF).|
| **PUBLISH\#4** | Granules should not be zipped when stored in the cloud, so that cloud optimized data formats can be leveraged. |
| **PUBLISH\#5** | Where possible, cloud providers' standard interfaces should be used in preference to self-developed solutions, enabling interoperability of tools that work with that cloud provider. |

***
[Previous](Vocabulary.md) | [Table of contents](README.md) | [Next](Interface.md)
