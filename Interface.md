# Interface (Accessibility)

[Previous](Architecture.md) | [Table of contents](README.md) | [Next](Quality.md)
***

Interfaces allow diversified resources within and across the organization to seamlessly communicate,
discover and exchange data. Interfaces are realized in the form of services and follow standards.
Interfaces enable data users to have easy and efficient ways of discovering and accessing data and associated
services through the exploitation of standard protocols and the harmonizing of search and data retrieval processes

## Data Discovery

| **ID** | **Recommendations** |
| :---- | :---- |
| **DISC\#1** | Collection and granule discovery interfaces should comply with the [CEOS STAC Collection and Granule Discovery Best Practices](https://github.com/ceos-org/stac-collection-and-granule-discovery-best-practices/tree/v1.0.0) (preferred) or [CEOS OpenSearch Best Practices](https://ceos.org/document_management/Working_Groups/WGISS/Documents/WGISS%20Best%20Practices/CEOS%20OpenSearch%20Best%20Practice.pdf). |
| **DISC\#2** | Service and tool discovery interfaces should comply with [CEOS Service Discovery Best Practice](https://ceos.org/document_management/Working_Groups/WGISS/Documents/WGISS%20Best%20Practices/CEOS-Service-Discovery-Best-Practices_V1.1.pdf). |
| **DISC\#3** | Collection and granule metadata obtained via the discovery interfaces should advertise the existence of the corresponding file-level online data access and subfile or pixel-based access services and endpoints (e.g., OGC WCS, WMTS, WCPS, OGC API Maps, OGC API Tiles, etc.). |
| **DISC\#4** | Granule metadata obtained via the discovery interfaces should include the online data access URL to the granule (in full resolution) and to a low resolution representation (i.e., quicklook or thumbnail).  The low resolution representation should be provided in Web-friendly format, e.g. JPEG or PNG, and may be a static file or an OGC WMS/WMTS or API Maps/Tiles response. |
| **DISC\#5** | Discovery interfaces should be accessible and return responses without requiring authentication. |
| **DISC\#6** | Collection and granule metadata obtained via the discovery interfaces should advertise the existence of the corresponding authentication endpoint for human and machine access to the data (if required). |
| **DISC\#7** | Resource metadata including keywords should link each keyword to its URI and to the appropriate thesaurus (i.e., controlled vocabularies). |
| **DISC\#8** | Keywords from controlled vocabularies that allow lookup of keyword information via [Linked Data principles](https://en.wikipedia.org/wiki/Linked_data), e.g., HTTP URI dereferencing or SPARQL interfaces are preferred. The use of GCMD controlled keywords is encouraged. |
| **DISC\#9** | Resource metadata should contain the persistent identifier (e.g., DOI) of the corresponding resource. |
| **DISC\#10** | Collection metadata should refer to the level of maturity with respect to the [WGISS Data Management and Stewardship Maturity Matrix](https://ceos.org/document_management/Working_Groups/WGISS/Interest_Groups/Data_Stewardship/White_Papers/WGISS%20Data%20Management%20and%20Stewardship%20Maturity%20Matrix.pdf). |
| **DISC\#11** | For facilitating discovery and access, data shall be organised in collections according to the principles outlined in the `WGISS Data Collections Management Practices White Paper`. |

## Data Access

| **ID** | **Recommendations** |
| :---- | :---- |
| **DACC\#1** |  Granule data stored in the cloud should be accessible directly via a web-based protocol, for example the S3 (Simple Storage Service) and HTTP(S). |
| **DACC\#2** |  Data access should support file-level access and subfile or pixel-based access. Data download interfaces over HTTPS should support [`Range Requests`](https://en.wikipedia.org/wiki/Byte_serving) to allow clients to request a portion of a file.  Typical use case: access to a portion of a [Cloud-Optimized GeoTIFF (COG)](https://en.wikipedia.org/wiki/GeoTIFF) file.|
| **DACC\#3** |  In case a granule consists of many individual assets (files), it shall be possible to access each asset individually and it is recommended to provide access to all subcomponents of a granule with a single request. |

## Authentication and Authorization

| **ID** | **Recommendations** |
| :---- | :---- |
| **AUTH\#1** | Authorization should be available at a file level for both human and machine-to-machine access. |
| **AUTH\#2** | Authentication interfaces should comply with open standards, such as the [OpenID Connect](https://openid.net/developers/how-connect-works/) protocol. |
| **AUTH\#3** | HTTPS requests for data access that require authorisation will support well known methods for both human and machine-to-machine interface, such as those specified in the [OpenAPI 3.0](https://swagger.io/docs/specification/v3_0/authentication/). |

***
[Previous](Architecture.md) | [Table of contents](README.md) | [Next](Quality.md)
