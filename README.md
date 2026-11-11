# Microsoft Fabric Learning Project

This repository is a hands-on collection of Microsoft Fabric assets built around the AdventureWorks sample data. It explores the broader Fabric workload areas of Data Factory (pipelines and dataflows), Data Engineering (lakehouse processing with Spark and Delta), Data Science (an introductory AutoML workflow), and Data Analysis (warehousing and semantic modeling).

## What you'll learn

- Ingest files into a Fabric lakehouse with data pipelines.
- Use a Dataflow Gen2 transformation to join and clean product category data.
- Explore raw data and process it with PySpark notebooks and Delta tables.
- Organize analytics data across bronze and silver lakehouses, then model gold warehouse tables.
- Build a Direct Lake semantic model.
- Train and use an AutoML model to predict sales order quantities.

## Project structure

```text
Fabric/
├── Data/                  # AdventureWorks CSV files and pipeline metadata
├── Components/
│   ├── Dataflow/          # Category and subcategory transformation
│   ├── Lakehouse/         # Bronze and silver lakehouse definitions
│   ├── ML Model/          # AutoML notebook, experiment, and model
│   ├── Notebook/          # Data exploration and silver-layer processing
│   ├── Pipelines/         # ADLS, dataflow, ForEach, parameterized, parent,
│   │                      # and static pipeline examples
│   ├── Semantic Model/    # Direct Lake model and table definitions
│   └── Warehouse/         # Gold SQL tables, views, and project
└── README.md
```

## Learning path

1. **Explore the source data.** The `Data/` folder contains AdventureWorks calendar, customer, product, product category, product subcategory, return, sales (2015–2017), and territory CSVs.
2. **Study ingestion patterns.** Review the pipeline examples in `Components/Pipelines/`. They demonstrate copying data from ADLS or HTTP sources, passing a URL parameter, iterating over a file list, refreshing a dataflow, and invoking child pipelines.
3. **Transform data.** The Dataflow Gen2 mashup joins product subcategories to categories, normalizes category names, and removes duplicate keys. The notebooks show reading source files and lakehouse data, creating Delta tables, and preparing product and sales data.
4. **Build the analytics layer.** Explore the warehouse SQL definitions under `Components/Warehouse/` and the Direct Lake tables and relationships under `Components/Semantic Model/`.
5. **Try the ML workflow.** The AutoML notebook uses the silver lakehouse sales table and `OrderQuantity` as its prediction target.

## Configure the project in a Fabric workspace

This project was authored in Microsoft Fabric. The repository contains exported Fabric item definitions and source data; it is not a local application that creates or configures a workspace automatically. When setting it up in another workspace, configure the workspace and item connections in Fabric before running the assets.

1. **Prepare the workspace.** Use a workspace on a Fabric-enabled capacity (or an eligible trial) and ensure your account has permission to create and run Fabric items. AutoML also requires a supported Fabric runtime: the generated notebook specifies Fabric Runtime 1.2+ or Spark 3.4+.
2. **Create or sync the Fabric items.** Use Fabric Git integration to connect the repository and sync the project items, or create/import the items in the workspace using the definitions under `Components/`. Confirm that all items are in the same workspace unless you intentionally update their cross-workspace references.
3. **Set up the lakehouses.** Create or sync `bronze_lakehouse` and `silver_lakehouse`. Use the bronze lakehouse for source and raw data and the silver lakehouse for processed Delta tables. Attach the appropriate lakehouse as each notebook's default lakehouse: the data exploration notebook uses bronze, while the silver processing and AutoML notebooks use silver.
4. **Place the source files.** Upload the required AdventureWorks CSVs from `Data/` to the lakehouse `Files` area, or configure the ingestion pipelines to copy them there. Preserve the folder and file names expected by the notebooks and dataflow, including `Raw_DataAdventureWorks_Products`, `Raw_DataAdventureWorks_Sales_2016`, `Raw_DataAdventureWorks_Sales_2017`, `Raw_DataAdventureWorks_Calendar`, `Raw_DataAdventureWorks_Territories`, `Raw_DataAdventureWorks_Product_Categories`, and `Raw_DataProduct_Subcategories`. The ADLS returns example expects `Raw_Data_ADLS/returns.csv`. Check the notebook and dataflow source paths if you choose a different layout.
5. **Configure connections and pipeline references.** In Fabric, authenticate and select the correct ADLS Gen2, HTTP, and lakehouse connections for the pipelines. Update source URLs, destination lakehouse/folder paths, pipeline parameters, and child-pipeline references as needed. The exported definitions include workspace, artifact, and connection IDs from the original authoring environment; do not assume those IDs or credentials will work in a different workspace.
6. **Configure the dataflow and analytics items.** Verify that the Dataflow Gen2 item reads from the intended lakehouse and writes its merged category data to the target table. Confirm that the warehouse project, semantic model, and ML experiment/model point to the lakehouse tables and workspace items available in your workspace.
7. **Run and validate in dependency order.** Ingest the raw files first, then run the dataflow and notebooks to create the lakehouse tables. Afterward validate the warehouse and semantic model, and run AutoML against the silver `sales` table with `OrderQuantity` as the target.

Fabric item definitions do not package workspace permissions, credentials, capacity, or external connections. Validate these settings in the Fabric UI, and check each item's source and destination before running it.
