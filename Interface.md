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
| **DISC\#3** | Collection and granule metadata obtained via the discovery interfaces should advertise the existence of the corresponding file-level online data access and subfile or pixel-based access services and endpoints (e.g. OGC WCS, WMTS, WCPS, OGC API Maps, OGC API Tiles, etc.). |
| **DISC\#4** | Granule metadata obtained via the discovery interfaces should include the online data access URL to the granule in native format and to a low resolution representation (i.e. quicklook or thumbnail) in Web-friendly format, e.g. JPEG or PNG.  The low-resolution representation may be a static file or an OGC WMS/WMTS or API Maps/Tiles response.|
| **DISC\#5** | Collection and granule metadata obtained via the discovery interfaces should advertise the existence of the corresponding authentication endpoint for access to the data (if any). |
| **DISC\#6** | Resource metadata including keywords should link each keyword to its HTTP URI and to the appropriate thesaurus (i.e. controlled vocabularies). |
| **DISC\#7** | Keywords from controlled vocabularies that allow lookup of keyword information via [Linked Data principles](https://en.wikipedia.org/wiki/Linked_data), e.g. HTTP URI dereferencing or SPARQL interfaces are preferred. The use of GCMD controlled keywords is encouraged.|
| **DISC\#8** | Resource metadata shall include the Persistent Identifier (e.g. DOI) of the corresponding resource (if available).   See also [CEOS Persistent Identifier Best Practices](https://ceos.org/document_management/Working_Groups/WGISS/Documents/WGISS%20Best%20Practices/CEOS%20Persistent%20Identifier%20Best%20Practice.pdf).|
| **DISC\#9** | Collection metadata should refer to quality information about the collection, e.g. expressed as [WGISS Data Management and Stewardship Maturity Matrix](https://ceos.org/document_management/Working_Groups/WGISS/Interest_Groups/Data_Stewardship/White_Papers/WGISS%20Data%20Management%20and%20Stewardship%20Maturity%20Matrix.pdf).|
| **DISC\#10** | Discovery interfaces should be accessible and return responses without requiring authentication. |
| **DISC\#11** | For facilitating discovery and access, data shall be organised in `collections` according to the principles outlined in the forthcoming `WGISS Data Collections Management Practices White Paper`. |

## Data Access

| **ID** | **Recommendations** |
| :---- | :---- |
| **DACC\#1** |  Granule data stored in the cloud should be accessible via the S3 (Simple Storage Service) and HTTP(S) protocols. |
| **DACC\#2** |  Granule data stored in the cloud should preferably be accessible in cloud-optimized formats, e.g. [Zarr](https://en.wikipedia.org/wiki/Zarr_(data_format)) or [Cloud-Optimized GeoTIFF (COG)](https://en.wikipedia.org/wiki/GeoTIFF).|
| **DACC\#3** |  Data access should support file-level access and subfile or pixel-based access.|
| **DACC\#4** |  Data download interfaces over HTTP should support [`Range Requests`](https://en.wikipedia.org/wiki/Byte_serving) to allow clients to request a portion of a file.  Typical use case: access to a portion of a [Cloud-Optimized GeoTIFF (COG)](https://en.wikipedia.org/wiki/GeoTIFF) file.|
| **DACC\#5** |  In case a granule consists of many individual assets (files), it shall be possible to access each asset individually or access all subcomponents of a granule with a single request.|

## Authentication and Authorization

| **ID** | **Recommendations** |
| :---- | :---- |
| **AUTH\#1** |  Authentication interfaces should support the [OpenID Connect](https://openid.net/developers/how-connect-works/) Protocol. |
| **AUTH\#2** |  HTTP requests (e.g. for data access) subject to authorization shall include the user token with `claims` in [JWT](https://datatracker.ietf.org/doc/html/rfc7519) format returned by the Authentication interface with every API request as a bearer token in the HTTP authorization header. |

***
[Previous](Architecture.md) | [Table of contents](README.md) | [Next](Quality.md)
