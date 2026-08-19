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






```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>AI Orbit — Data Ingestion Pipeline</title>

    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: Arial, Helvetica, sans-serif;
            background: #080d1a;
            color: #f5f7ff;
            min-height: 100vh;
        }

        header {
            padding: 35px 6%;
            background: #0e1628;
            border-bottom: 1px solid #263451;
        }

        header h1 {
            font-size: 34px;
            margin-bottom: 10px;
        }

        header p {
            color: #a8b3ca;
            max-width: 900px;
            line-height: 1.7;
        }

        .container {
            width: 88%;
            max-width: 1450px;
            margin: 30px auto;
        }

        .pipeline {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 30px;
        }

        .stage {
            background: #121d33;
            border: 1px solid #30405f;
            border-radius: 9px;
            padding: 11px 15px;
            color: #c9d3e9;
            font-size: 13px;
        }

        .stage::after {
            content: " →";
            color: #7185ff;
        }

        .stage:last-child::after {
            content: "";
        }

        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
            gap: 15px;
            margin-bottom: 25px;
        }

        .stat {
            background: #10192d;
            border: 1px solid #293754;
            border-radius: 13px;
            padding: 20px;
        }

        .stat-title {
            color: #8f9bb5;
            font-size: 13px;
            margin-bottom: 9px;
        }

        .stat-value {
            font-size: 28px;
            font-weight: bold;
        }

        .controls {
            display: grid;
            grid-template-columns: 2fr 1fr 1fr;
            gap: 12px;
            margin-bottom: 25px;
        }

        input,
        select {
            width: 100%;
            padding: 14px;
            border-radius: 10px;
            border: 1px solid #303e5d;
            background: #10182b;
            color: #ffffff;
            outline: none;
        }

        input:focus,
        select:focus {
            border-color: #7185ff;
        }

        .panel {
            background: #0f172a;
            border: 1px solid #283550;
            border-radius: 15px;
            margin-bottom: 25px;
            overflow: hidden;
        }

        .panel-header {
            padding: 20px;
            border-bottom: 1px solid #283550;
        }

        .panel-header h2 {
            font-size: 20px;
        }

        .entities {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(290px, 1fr));
            gap: 15px;
            padding: 20px;
        }

        .entity {
            background: #131e35;
            border: 1px solid #2b3a59;
            border-radius: 12px;
            padding: 18px;
        }

        .entity-type {
            font-size: 11px;
            color: #899bff;
            text-transform: uppercase;
            letter-spacing: 1.2px;
            margin-bottom: 8px;
        }

        .entity h3 {
            margin-bottom: 9px;
            font-size: 18px;
        }

        .entity-description {
            color: #aab5cb;
            line-height: 1.55;
            font-size: 14px;
            margin-bottom: 13px;
        }

        .badge {
            display: inline-block;
            border: 1px solid #364664;
            background: #1b2945;
            color: #cbd4e7;
            padding: 5px 8px;
            border-radius: 20px;
            margin: 2px;
            font-size: 11px;
        }

        .metadata {
            margin-top: 13px;
            padding-top: 12px;
            border-top: 1px solid #283550;
            color: #8794ad;
            font-size: 12px;
            line-height: 1.7;
        }

        .source {
            margin-top: 10px;
            color: #78869f;
            font-size: 12px;
        }

        .source a {
            color: #91a0ff;
            text-decoration: none;
        }

        .relationship {
            padding: 17px 20px;
            border-bottom: 1px solid #26334e;
        }

        .relationship:last-child {
            border-bottom: none;
        }

        .node {
            font-weight: bold;
        }

        .relation {
            color: #8e9eff;
            margin: 0 10px;
        }

        .empty {
            padding: 35px;
            text-align: center;
            color: #76839c;
        }

        footer {
            text-align: center;
            padding: 35px;
            color: #68748b;
            font-size: 12px;
        }

        @media(max-width: 800px) {
            .controls {
                grid-template-columns: 1fr;
            }

            .container {
                width: 94%;
            }

            header h1 {
                font-size: 27px;
            }
        }
    </style>
</head>

<body>

<header>

    <h1>AI Orbit Data Ingestion Pipeline</h1>

    <p>
        A unified AI ecosystem data platform for discovery,
        extraction, cleaning, normalization, deduplication,
        classification, relationship mapping and validation.
    </p>

</header>


<main class="container">

    <!-- PIPELINE -->

    <div class="pipeline">

        <div class="stage">Discovery</div>

        <div class="stage">Extraction</div>

        <div class="stage">Cleaning</div>

        <div class="stage">Normalization</div>

        <div class="stage">Deduplication</div>

        <div class="stage">Classification</div>

        <div class="stage">Relationship Mapping</div>

        <div class="stage">Validation</div>

    </div>


    <!-- STATISTICS -->

    <section class="stats">

        <div class="stat">
            <div class="stat-title">
                Total Entities
            </div>

            <div
                class="stat-value"
                id="totalEntities"
            >
                0
            </div>
        </div>


        <div class="stat">
            <div class="stat-title">
                Companies
            </div>

            <div
                class="stat-value"
                id="companies"
            >
                0
            </div>
        </div>


        <div class="stat">
            <div class="stat-title">
                Tools
            </div>

            <div
                class="stat-value"
                id="tools"
            >
                0
            </div>
        </div>


        <div class="stat">
            <div class="stat-title">
                Models
            </div>

            <div
                class="stat-value"
                id="models"
            >
                0
            </div>
        </div>


        <div class="stat">
            <div class="stat-title">
                Repositories
            </div>

            <div
                class="stat-value"
                id="repositories"
            >
                0
            </div>
        </div>


        <div class="stat">
            <div class="stat-title">
                Relationships
            </div>

            <div
                class="stat-value"
                id="relationshipsCount"
            >
                0
            </div>
        </div>

    </section>


    <!-- FILTERS -->

    <section class="controls">

        <input
            id="search"
            type="search"
            placeholder="Search AI ecosystem..."
        >

        <select id="typeFilter">

            <option value="all">
                All Entity Types
            </option>

        </select>


        <select id="categoryFilter">

            <option value="all">
                All Categories
            </option>

        </select>

    </section>


    <!-- ENTITIES -->

    <section class="panel">

        <div class="panel-header">

            <h2>
                AI Ecosystem Entities
            </h2>

        </div>


        <div
            class="entities"
            id="entities"
        ></div>

    </section>


    <!-- RELATIONSHIPS -->

    <section class="panel">

        <div class="panel-header">

            <h2>
                AI Ecosystem Relationships
            </h2>

        </div>


        <div id="relationshipList"></div>

    </section>

</main>


<footer>

    AI Orbit Data Ingestion Pipeline

</footer>


<!-- =====================================================
     EMBEDDED JSON DATA
     =====================================================

     The JSON is embedded directly into this HTML file.

     No external JSON file is required.
-->

<script type="application/json" id="ai-orbit-json">

{
    "project": {
        "name": "AI Orbit Data Ingestion Pipeline",
        "version": "1.0.0",
        "description": "AI ecosystem data ingestion and relationship mapping system",
        "target_records": "250-300",
        "pipeline": [
            "Discovery",
            "Extraction",
            "Cleaning",
            "Normalization",
            "Deduplication",
            "Classification",
            "Relationship Mapping",
            "Validation"
        ]
    },

    "entities": [

        {
            "id": "company-openai-001",
            "entity_type": "company",
            "name": "OpenAI",
            "description": "AI research and product organization.",
            "url": "https://openai.com",
            "categories": [
                "AI Company",
                "Generative AI"
            ],
            "source": {
                "name": "Official Product Site",
                "url": "https://openai.com"
            },
            "metadata": {
                "founding_year": 2015,
                "industry_sector": "Artificial Intelligence",
                "headquarters": ""
            }
        },


        {
            "id": "tool-example-001",
            "entity_type": "tool",
            "name": "Example AI Tool",
            "description": "Example AI application used to demonstrate the AI Orbit data schema.",
            "url": "https://example.com",
            "categories": [
                "AI Tool",
                "Productivity"
            ],
            "source": {
                "name": "Official Product Site",
                "url": "https://example.com"
            }
        },


        {
            "id": "task-text-generation-001",
            "entity_type": "task",
            "name": "Text Generation",
            "description": "A task that users can accomplish with generative AI.",
            "url": "",
            "categories": [
                "Generative AI",
                "Language"
            ],
            "source": {
                "name": "AI Orbit Dataset",
                "url": ""
            }
        },


        {
            "id": "model-example-001",
            "entity_type": "model",
            "name": "Example AI Model",
            "description": "Example AI/ML model demonstrating specialized model metadata.",
            "url": "https://example.com/model",
            "categories": [
                "AI Model",
                "Machine Learning"
            ],
            "source": {
                "name": "Hugging Face",
                "url": "https://huggingface.co"
            },
            "metadata": {
                "license": "Example License",
                "modalities": [
                    "text"
                ],
                "provider": "Example Provider"
            }
        },


        {
            "id": "repository-example-001",
            "entity_type": "repository",
            "name": "Example AI Repository",
            "description": "Example GitHub/open-source AI project.",
            "url": "https://github.com/example/example",
            "categories": [
                "Open Source",
                "AI"
            ],
            "source": {
                "name": "GitHub",
                "url": "https://github.com"
            },
            "metadata": {
                "stars": 100,
                "primary_language": "Python",
                "last_updated": "2026-08-19T00:00:00Z"
            }
        },


        {
            "id": "mcp-example-001",
            "entity_type": "mcp",
            "name": "Example MCP Server",
            "description": "Example MCP server demonstrating MCP-specific metadata.",
            "url": "https://example.com/mcp",
            "categories": [
                "MCP",
                "AI Infrastructure"
            ],
            "source": {
                "name": "GitHub",
                "url": "https://github.com"
            },
            "metadata": {
                "installation_methods": [
                    "npm",
                    "Docker"
                ],
                "runtime_requirements": [
                    "Node.js"
                ]
            }
        },


        {
            "id": "device-example-001",
            "entity_type": "device",
            "name": "Example AI Device",
            "description": "Example AI hardware device.",
            "url": "https://example.com/device",
            "categories": [
                "AI Hardware",
                "Device"
            ],
            "source": {
                "name": "Official Product Site",
                "url": "https://example.com"
            }
        },


        {
            "id": "robot-example-001",
            "entity_type": "robot",
            "name": "Example AI Robot",
            "description": "Example AI robotics system.",
            "url": "https://example.com/robot",
            "categories": [
                "Robotics",
                "AI"
            ],
            "source": {
                "name": "Official Product Site",
                "url": "https://example.com"
            }
        },


        {
            "id": "video-example-001",
            "entity_type": "video",
            "name": "Example AI Technical Demo",
            "description": "Example AI technical tutorial or demonstration.",
            "url": "https://youtube.com",
            "categories": [
                "AI Video",
                "Technical Demo"
            ],
            "source": {
                "name": "YouTube",
                "url": "https://youtube.com"
            }
        },


        {
            "id": "news-example-001",
            "entity_type": "news",
            "name": "Example AI Industry Announcement",
            "description": "Example AI industry announcement or press release.",
            "url": "https://example.com/news",
            "categories": [
                "AI News",
                "Announcement"
            ],
            "source": {
                "name": "News/RSS",
                "url": "https://example.com/rss"
            }
        },


        {
            "id": "collection-example-001",
            "entity_type": "collection",
            "name": "Example AI Collection",
            "description": "Curated group of AI resources.",
            "url": "https://example.com/collection",
            "categories": [
                "Collection",
                "AI Resources"
            ],
            "source": {
                "name": "AI Directory",
                "url": "https://example.com"
            }
        },


        {
            "id": "personal-example-001",
            "entity_type": "personal",
            "name": "Example Personal AI Assistant",
            "description": "Example personal AI assistant.",
            "url": "https://example.com/assistant",
            "categories": [
                "Personal AI",
                "Assistant"
            ],
            "source": {
                "name": "Official Product Site",
                "url": "https://example.com"
            }
        },


        {
            "id": "creative-example-001",
            "entity_type": "creative",
            "name": "Example Creative AI Tool",
            "description": "Example creative-generation AI tool.",
            "url": "https://example.com/creative",
            "categories": [
                "Creative AI",
                "Generation"
            ],
            "source": {
                "name": "Official Product Site",
                "url": "https://example.com"
            }
        }

    ],


    "relationships": [

        {
            "source": "company-openai-001",
            "relationship": "develops",
            "target": "tool-example-001"
        },

        {
            "source": "company-openai-001",
            "relationship": "develops",
            "target": "model-example-001"
        },

        {
            "source": "tool-example-001",
            "relationship": "solves",
            "target": "task-text-generation-001"
        },

        {
            "source": "mcp-example-001",
            "relationship": "integrates_with",
            "target": "tool-example-001"
        },

        {
            "source": "device-example-001",
            "relationship": "runs",
            "target": "model-example-001"
        }

    ]

}

</script>


<script>

/*
==========================================================
READ EMBEDDED JSON
==========================================================
*/

const jsonElement =
    document.getElementById("ai-orbit-json");

const data =
    JSON.parse(jsonElement.textContent);


/*
==========================================================
DOM REFERENCES
==========================================================
*/

const entitiesContainer =
    document.getElementById("entities");

const relationshipList =
    document.getElementById("relationshipList");

const search =
    document.getElementById("search");

const typeFilter =
    document.getElementById("typeFilter");

const categoryFilter =
    document.getElementById("categoryFilter");


/*
==========================================================
FILTER INITIALIZATION
==========================================================
*/

function initializeFilters() {

    const types =
        [...new Set(
            data.entities.map(
                entity => entity.entity_type
            )
        )].sort();


    const categories =
        [...new Set(
            data.entities.flatMap(
                entity => entity.categories || []
            )
        )].sort();


    types.forEach(type => {

        const option =
            document.createElement("option");

        option.value = type;
        option.textContent = type;

        typeFilter.appendChild(option);

    });


    categories.forEach(category => {

        const option =
            document.createElement("option");

        option.value = category;
        option.textContent = category;

        categoryFilter.appendChild(option);

    });

}


/*
==========================================================
STATISTICS
==========================================================
*/

function updateStatistics() {

    const entities =
        data.entities;


    document.getElementById("totalEntities")
        .textContent = entities.length;


    document.getElementById("companies")
        .textContent =
        entities.filter(
            entity =>
                entity.entity_type === "company"
        ).length;


    document.getElementById("tools")
        .textContent =
        entities.filter(
            entity =>
                entity.entity_type === "tool"
        ).length;


    document.getElementById("models")
        .textContent =
        entities.fi
