# AI Orbit Data Ingestion Pipeline

A production-grade, Python-based bulk data ingestion pipeline designed to aggregate, normalize, structure, deduplicate, classify, validate, and map relationships across the global AI ecosystem.

The project is designed around an **API-first data engineering approach**, prioritizing data integrity, entity resolution, relationship mapping, and high-quality representative data over high-volume brute-force scraping.

---

## 1. Project Overview

AI Orbit requires structured information from multiple areas of the global AI ecosystem.

This project builds a modular ingestion engine that discovers information from diverse sources, extracts relevant data, cleans and normalizes it, removes duplicates, classifies entities, identifies relationships, and validates the final dataset.

### Core Pipeline

```text
Discovery
    ↓
Extraction
    ↓
Cleaning
    ↓
Normalization
    ↓
Deduplication
    ↓
Classification
    ↓
Relationship Mapping
    ↓
Validation
```

The pipeline is designed to be modular, reusable, scalable, and resilient against incomplete or unreliable source data.

---

## 2. Project Goals

The primary objectives are:

* Aggregate AI ecosystem data from multiple sources.
* Build a high-quality representative dataset.
* Normalize data into a consistent structure.
* Resolve duplicate entities.
* Canonicalize variations of entity names.
* Classify entities into meaningful categories.
* Extract relationships between entities.
* Validate the resulting dataset.
* Handle missing fields and network failures gracefully.
* Produce structured JSON outputs.
* Maintain source information for collected data.

The target dataset size is approximately **250–300 high-quality records**.

---

## 3. Data Sources

The ingestion pipeline is designed to leverage multiple sources.

### GitHub

Used for:

* Open-source repositories
* MCP servers

### Hugging Face

Used for:

* AI/ML models
* Datasets

### YouTube

Used for:

* Technical tutorials
* Demonstrations
* Reviews

### News / RSS

Used for:

* Industry announcements
* Press releases
* AI news

### Official Product Websites

Used for:

* Product specifications
* Company information
* Tool information

### AI Directories

Used for:

* AI resource listings
* Metadata
* Cross-referencing

The project follows an **API-first mindset**, favoring structured APIs and reliable sources over brute-force scraping.

---

## 4. Data Categories

The final dataset covers the following AI ecosystem categories:

| Category             | Description                         |
| -------------------- | ----------------------------------- |
| Tools                | AI applications and tools           |
| Tasks                | Things users can accomplish with AI |
| Companies            | AI startups and companies           |
| News                 | AI news and announcements           |
| Videos               | AI-related videos                   |
| Robots               | AI and robotics systems             |
| Devices              | AI hardware and devices             |
| Models               | AI/ML models                        |
| Repositories         | GitHub/open-source projects         |
| MCP                  | MCP servers and tools               |
| Collections          | Curated groups of AI resources      |
| Personal             | Personal AI assistants              |
| Creative             | Creative-generation tools           |
| New / Recently Added | Recently added entities             |

---

## 5. Data Schema

Every entity follows a common schema.

```json
{
  "id": "stable-generated-uuid",
  "entity_type": "string",
  "name": "string",
  "description": "string",
  "url": "string",
  "categories": [
    "string"
  ],
  "source": {
    "name": "string",
    "url": "string"
  }
}
```

### Common Fields

#### `id`

A stable generated UUID identifying the entity.

#### `entity_type`

Defines the type of entity.

Examples:

```text
tool
task
company
news
video
robot
device
model
repository
mcp
collection
personal
creative
```

#### `name`

The entity's canonical name.

#### `description`

A cleaned description of the entity.

#### `url`

The normalized URL associated with the entity.

#### `categories`

One or more classifications associated with the entity.

#### `source`

Contains the source name and source URL from which the information was obtained.

---

## 6. Specialized Metadata

Different entity types require additional domain-specific information.

### Models

Models should contain:

* License
* Modalities
* Provider details

### Repositories

Repositories should contain:

* Stars
* Primary programming language
* Last updated timestamp

### MCP Servers

MCP servers should contain:

* Installation methods
* Runtime requirements

### Companies

Companies should contain:

* Founding year
* Industry sector
* Headquarters

Specialized metadata should enrich the common entity schema where applicable.

---

## 7. Relationship Extraction

AI Orbit is designed to represent the AI ecosystem as an interconnected system rather than a collection of isolated records.

The pipeline therefore extracts relationships between entities.

The resulting relationship information must be stored in:

```text
relationships.json
```

### Required Relationship Types

#### Company develops Tool

```text
Company
    ↓ develops
Tool
```

#### Company develops Model

```text
Company
    ↓ develops
Model
```

#### Tool solves Task

```text
Tool
    ↓ solves
Task
```

#### MCP integrates with Tool

```text
MCP
    ↓ integrates with
Tool
```

#### Device runs Model

```text
Device
    ↓ runs
Model
```

These relationships allow the resulting dataset to represent the interconnectedness of the AI ecosystem.

---

## 8. Entity Resolution

Entity resolution is an important part of the pipeline.

Different sources may represent the same entity using slightly different names.

For example:

```text
OpenAI
```

and

```text
Open AI
```

may refer to the same entity.

The pipeline should canonicalize such variations and prevent the creation of unnecessary duplicate records.

---

## 9. URL Normalization

URLs collected from different sources should be normalized.

The system should handle:

* Consistent URL formatting
* Redirect resolution
* Duplicate URLs
* Different URL representations referring to the same resource

The objective is to maintain reliable and consistent URLs in the final dataset.

---

## 10. Data Cleaning and Sanitization

Raw source information should not be placed directly into the final dataset.

The cleaning stage should process extracted content and remove unnecessary formatting or unwanted source artifacts.

This includes:

* HTML cleanup
* RSS content sanitization
* Text cleaning
* Formatting normalization
* Handling malformed content

The resulting text should be clean and suitable for downstream use by the AI Orbit platform.

---

## 11. Deduplication

The pipeline must detect duplicate records across different sources.

Deduplication should consider information such as:

* Entity names
* Canonical names
* URLs
* Entity types
* Other available identifying metadata

The objective is to maintain one reliable canonical representation of an entity wherever possible.

---

## 12. Classification

Entities should be classified into the appropriate AI ecosystem categories.

Examples include:

```text
Tools
Models
Companies
Repositories
MCP
Devices
Robots
Videos
News
Tasks
Collections
Personal
Creative
New / Recently Added
```

Classification should occur before final validation and storage.

---

## 13. Validation

The final dataset must pass a validation stage.

Validation should verify that records are:

* Structurally valid
* Properly normalized
* Correctly categorized
* Not unnecessarily duplicated
* Associated with source information
* Suitable for the final JSON output

Relationship mappings should also be checked for consistency.

---

## 14. Error Handling and Resilience

The ingestion system must gracefully handle unreliable data sources.

Potential failures include:

* Network failures
* Missing fields
* Invalid responses
* Incomplete records
* Unexpected data formats
* Source/API failures

The pipeline should avoid failing completely because of a single bad record or unavailable field.

Failures should be logged appropriately while allowing the remaining ingestion process to continue where possible.

---

## 15. Repository Structure

The project should use a structured repository.

```text
ai-orbit-data-ingestion/
│
├── src/
│   ├── discovery/
│   ├── extraction/
│   ├── cleaning/
│   ├── normalization/
│   ├── deduplication/
│   ├── classification/
│   ├── relationships/
│   ├── validation/
│   ├── models/
│   └── utils/
│
├── data/
│   ├── entities.json
│   └── relationships.json
│
├── run.py
│
├── README.md
│
└── requirements.txt
```

The exact internal module organization may evolve during implementation, but the architecture should remain modular and reusable.

---

## 16. Pipeline Execution

The complete pipeline should be executable through:

```bash
python run.py
```

The execution process should perform the major ingestion stages:

```text
1. Discover sources
2. Extract data
3. Clean raw information
4. Normalize entities
5. Deduplicate entities
6. Classify entities
7. Extract relationships
8. Validate data
9. Write JSON outputs
```

---

## 17. Output

The pipeline should produce a high-quality representative dataset containing approximately:

```text
250–300 records
```

The final data should be stored under:

```text
data/
```

The relationship graph should be stored as:

```text
data/relationships.json
```

The final dataset should contain rich metadata and maintain source information for traceability.

---

## 18. Engineering Principles

The implementation follows these principles:

### API First

Prefer structured APIs and reliable sources over brute-force scraping.

### Data Integrity

Prioritize accurate, clean, standardized information.

### Entity Resolution

Recognize different representations of the same entity.

### Deduplication

Prevent unnecessary duplicate records.

### Normalization

Maintain consistent data and URLs.

### Modularity

Separate pipeline responsibilities into reusable components.

### Scalability

Design the system so additional sources and entity types can be introduced without rewriting the entire pipeline.

### Resilience

Handle missing data and network failures gracefully.

### Traceability

Maintain source information for collected entities.

---

## 19. Evaluation Criteria

The project is evaluated across the following areas:

| Focus Area        | Weight |
| ----------------- | -----: |
| Data Quality      |    25% |
| Architecture      |    20% |
| Discovery         |    15% |
| Entity Resolution |    15% |
| Relationships     |    10% |
| Error Handling    |    10% |
| Documentation     |     5% |

### Data Quality — 25%

The dataset should contain clean, standardized, and rich metadata.

### Architecture — 20%

The implementation should be modular, reusable, and scalable.

### Discovery — 15%

The system should demonstrate intelligent API usage rather than brute-force scraping.

### Entity Resolution — 15%

The implementation should demonstrate sophisticated deduplication and entity linking.

### Relationships — 10%

The extracted relationships should accurately represent connections within the AI ecosystem.

### Error Handling — 10%

The pipeline should remain resilient against network and data failures.

### Documentation — 5%

The repository should clearly explain setup instructions and technical decisions.

---

## 20. Expected Result

The final project should demonstrate a complete data engineering pipeline capable of transforming heterogeneous AI ecosystem information into a structured and interconnected dataset.

The finished system should provide:

* Approximately 250–300 high-quality AI ecosystem records
* Multiple data categories
* Clean and normalized entities
* Duplicate detection and entity resolution
* Specialized metadata
* Source information
* Relationship mappings
* JSON outputs
* Modular Python architecture
* Validation
* Error handling
* Reproducible execution
* Clear technical documentation

The ultimate purpose is to provide AI Orbit with structured information representing both **AI entities and the relationships between those entities**.
