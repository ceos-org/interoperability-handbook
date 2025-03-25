# Vocabulary (Semantics)

[Previous](Framework.md) | [Table of contents](README.md) | [Next](Architecture.md)
***
Interoperability relies on the ability of diverse entities to communicate and exchange information seamlessly. At its core, semantics and vocabularies play a fundamental role in ensuring that data, messages, and services are not only transmitted but also correctly understood across different stakeholders. Without a shared understanding of terms, concepts, and relationships, interoperability remains limited, hampered by inconsistencies, misunderstandings, and other integration challenges.

Semantics deal with general aspects of meaning and relationships between terms and concepts in a domain, ensuring that communication is structured and interpreted consistently. As an important part of such communication, vocabularies, including thesauri, glossaries, terminologies, ontologies, taxonomies, and controlled vocabularies, provide standardized definitions that facilitate common understanding. In the context of geospatial interoperability, standardized vocabularies enable diverse entities to describe, classify, and relate data and services in a way that is human and machine-readable and reusable across the whole domain.

This section highlights the essential role of semantics and vocabularies in the CEOS Interoperability Framework. It outlines key standards, best practices for implementing semantic interoperability, and methods for aligning domain-specific vocabularies. By establishing a shared semantic foundation, stakeholders can improve data exchange, integration, service compatibility, and automated reasoning, ensuring more effective collaboration in an increasingly interconnected digital geospatial ecosystem.

| **ID** | **Semantic Recommendations**                                                                                                       |
| :----- | :--------------------------------------------------------------------------------------------------------------------------------- |
| **SEM\#1** | Terms and definitions should be collected into an open Earth observation thesaurus, such as that provided by KCEO/CEOS through GitHub. |
| **SEM\#2** | Capability should be provided to enable public comment and discussion on existing and new terms and definitions. |
| **SEM\#3** | Enable version control and change management at the individual term level and link to historical and alternative definitions. |
| **SEM\#4** | Use of project or document specific vocabularies should be discouraged e.g. in the form of ‘terms and definitions’ chapters. Source (via weblink), maintain, and develop all terms that serve or might serve in more than one context in the online, shared repository. |
| **SEM\#5** | Community members should promote the common thesaurus, including through ISO/TC 211, OGC, WMO, GEO and other stakeholders in Earth System Sciences, to strive for domain wide adoption. |
| **SEM\#6** | Common online repositories for abbreviations and acronyms should be used. Agreed metadata fields with unified and binding lists of options should be included. Keywords from controlled vocabularies that allow lookup of keyword information via Linked Data principles, e.g. HTTP URI dereferencing or SPARQL interfaces are preferred. The use of GCMD controlled keywords is encouraged. |

Of central importance for increasing the interoperability within CEOS and across the entire geospatial domain, will be a more harmonised and structured terminology. Providers and users of EO data and services will largely benefit if the definition and interpretation of terms is no longer re-negotiated and amended each time projects are started, or new documents are drafted. A key finding of the terminology task force was that vocabularies should be developed as much as possible in an open and participatory way across the whole domain they are intended for.One of the main lessons learned by the CEOS terminology task force was that usability and acceptance of unified vocabularies will largely depend on consistent and comprehensive principles shared by all stakeholders and guiding their development.

| **ID** | **Thesaurus Recommendations** |
| :---- | :---- |
| **THES\#1** | The terms used in the thesaurus should be consistent and divided into classes such as Base, Core, Controversial and High Impact. The ‘Base Terms’ should have cross community agreement and should not have circular or ambiguous definitions. The ‘Core Term’ should be using the ‘Base Term’ consistently and can be allowed to have minor tweaks with approval from the identified committee. The ‘Controversial Term’ should have qualifiers attached to them with links to discussions, which led to the association of the qualifier. The ‘High Impact Term’ should be approved by a specialist committee and should be linked to a document providing details of the term. |
| **THES\#2** | The definition of a term may not contain the term itself nor other circular definitions (e.g., where term A is defined using term B and term B is defined using term A). A clear set of base terms should be used.  |
| **THES\#3** | The terms used in the thesaurus should have clear and mappable relationships with other terms (parent, sibling, child). Overlaps between terms that are supposed to delineate more generic concepts (siblings) should be avoided or minimized. |
| **THES\#4** | Definitions have to be kept unambiguous and short, and written in a form such that they can replace the term in a sentence. |
| **THES\#5** | Explanations should be given in a separate ‘Notes’ sections, and Examples in a separate 'Examples' section. Both complement the definition, and should not be included as part of the main definition. |
| **THES\#6** | Every definition should have an accompanying 'Sources' section, where all source documents are listed, wherever possible as weblinks. |
| **THES\#7** | Thesaurus terms should be version controlled at the individual term level.|
| **THES\#8** | Where a term is deemed ‘controversial’ then contradictory definitions can be provided, but only with clear links to alternative definitions and explanations as to what context a term is used in.|

***
[Previous](Framework.md) | [Table of contents](README.md) | [Next](Architecture.md)
