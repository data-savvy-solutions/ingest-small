def get_ddl() -> dict:
    """
    Returns a dictionary of data types.

    Returns a dictionary of dictionaries. Each nested dictionary represents a
    table, with the key representing a column header and the value a data type.

    Args:
        None

    Returns:
        Dictionary: a dictionary of dictionaries representing tables and their
            data types.
    """

    schema = "ods_adventureworks"

    definitions = {}

    definitions[f"{schema}_BillOfMaterials"] = f"""
        CREATE TABLE [{schema}].[BillOfMaterials](
               [BillOfMaterialsID] [INT] NOT NULL
               ,[ProductAssemblyID] [INT] NULL
               ,[ComponentID] [INT] NOT NULL
               ,[StartDate] [DATETIME] NOT NULL
               ,[EndDate] [DATETIME] NULL
               ,[UnitMeasureCode] [NCHAR](3) NOT NULL
               ,[BOMLevel] [SMALLINT] NOT NULL
               ,[PerAssemblyQty] [DECIMAL](8,2) NOT NULL
               ,[ModifiedDate] [DATETIME] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_Culture"] = f"""
        CREATE TABLE [{schema}].[Culture](
               [CultureID] [nchar](6) NOT NULL
               ,[Name] [char](256) NOT NULL
               ,[ModifiedDate] [datetime] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_Document"] = f"""
        CREATE TABLE [{schema}].[Document](
               [DocumentNode] [hierarchyid] NOT NULL
               ,[DocumentLevel] [smallint] NOT NULL
               ,[Title] [nvarchar](50) NOT NULL
               ,[Owner] [int] NOT NULL
               ,[FolderFlag] [bit] NOT NULL
               ,[FileName] [nvarchar](400) NOT NULL
               ,[FileExtension] [nvarchar](8) NOT NULL
               ,[Revision] [nchar](5) NOT NULL
               ,[ChangeNumber] [int] NOT NULL
               ,[Status] [tinyint] NOT NULL
               ,[DocumentSummary] [nvarchar](MAX) NULL
               ,[Document] [varbinary](MAX) NULL
               ,[rowguid] [uniqueidentifier] NOT NULL
               ,[ModifiedDate] [datetime] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_Illustration"] = f"""
        CREATE TABLE [{schema}].[Illustration](
               [IllustrationID] [int] NOT NULL
               ,[Diagram] [xml] NULL
               ,[ModifiedDate] [datetime] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_Location"] = f"""
        CREATE TABLE [{schema}].[Location](
               [LocationID] [smallint] NOT NULL
               ,[Name] [CHAR](256) NOT NULL
               ,[CostRate] [smallmoney] NOT NULL
               ,[Availability] [decimal](8,2) NOT NULL
               ,[ModifiedDate] [datetime] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_Product"] = f"""
        CREATE TABLE [{schema}].[Product](
               [ProductID] [int] NOT NULL
               ,[Name] [char](256) NOT NULL
               ,[ProductNumber] [nvarchar](25) NOT NULL
               ,[MakeFlag] [bit] NOT NULL
               ,[FinishedGoodsFlag] [bit] NOT NULL
               ,[Color] [nvarchar](15) NULL
               ,[SafetyStockLevel] [smallint] NOT NULL
               ,[ReorderPoint] [smallint] NOT NULL
               ,[StandardCost] [money] NOT NULL
               ,[ListPrice] [money] NOT NULL
               ,[Size] [nvarchar](5) NULL
               ,[SizeUnitMeasureCode] [nchar](3) NULL
               ,[WeightUnitMeasureCode] [nchar](3) NULL
               ,[Weight] [decimal](8,2) NULL
               ,[DaysToManufacture] [int] NOT NULL
               ,[ProductLine] [nchar](2) NULL
               ,[Class] [nchar](2) NULL
               ,[Style] [nchar](2) NULL
               ,[ProductSubcategoryID] [int] NULL
               ,[ProductModelID] [int] NULL
               ,[SellStartDate] [datetime] NOT NULL
               ,[SellEndDate] [datetime] NULL
               ,[DiscontinuedDate] [datetime] NULL
               ,[rowguid] [uniqueidentifier] NOT NULL
               ,[ModifiedDate] [datetime] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_ProductCategory"] = f"""
        CREATE TABLE [{schema}].[ProductCategory](
               [ProductCategoryID] [int] NOT NULL
               ,[Name] [char](256) NOT NULL
               ,[rowguid] [uniqueidentifier] NOT NULL
               ,[ModifiedDate] [datetime] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_ProductCostHistory"] = f"""
        CREATE TABLE [{schema}].[ProductCostHistory](
               [ProductID] [int] NOT NULL
               ,[StartDate] [datetime] NOT NULL
               ,[EndDate] [datetime] NULL
               ,[StandardCost] [money] NOT NULL
               ,[ModifiedDate] [datetime] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_ProductDescription"] = f"""
        CREATE TABLE [{schema}].[ProductDescription](
               [ProductDescriptionID] [int] NOT NULL
               ,[Description] [nvarchar](400) NOT NULL
               ,[rowguid] [uniqueidentifier] NOT NULL
               ,[ModifiedDate] [datetime] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_ProductDocument"] = f"""
        CREATE TABLE [{schema}].[ProductDocument](
               [ProductID] [int] NOT NULL
               ,[DocumentNode] [hierarchyid] NOT NULL
               ,[ModifiedDate] [datetime] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_ProductInventory"] = f"""
        CREATE TABLE [{schema}].[ProductInventory](
               [ProductID] [int] NOT NULL
               ,[LocationID] [smallint] NOT NULL
               ,[Shelf] [nvarchar](10) NOT NULL
               ,[Bin] [tinyint] NOT NULL
               ,[Quantity] [smallint] NOT NULL
               ,[rowguid] [uniqueidentifier] NOT NULL
               ,[ModifiedDate] [datetime] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_ProductListPriceHistory"] = f"""
        CREATE TABLE [{schema}].[ProductListPriceHistory](
               [ProductID] [int] NOT NULL
               ,[StartDate] [datetime] NOT NULL
               ,[EndDate] [datetime] NULL
               ,[ListPrice] [money] NOT NULL
               ,[ModifiedDate] [datetime] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_ProductModel"] = f"""
        CREATE TABLE [{schema}].[ProductModel](
               [ProductModelID] [int] NOT NULL
               ,[Name] [char](256) NOT NULL
               ,[CatalogDescription] [xml] NULL
               ,[Instructions] [xml] NULL
               ,[rowguid] [uniqueidentifier] NOT NULL
               ,[ModifiedDate] [datetime] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_ProductModelIllustration"] = f"""
        CREATE TABLE [{schema}].[ProductModelIllustration](
               [ProductModelID] [int] NOT NULL
               ,[IllustrationID] [int] NOT NULL
               ,[ModifiedDate] [datetime] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_ProductModelProductDescriptionCulture"] = f"""
        CREATE TABLE [{schema}].[ProductModelProductDescriptionCulture](
               [ProductModelID] [int] NOT NULL
               ,[ProductDescriptionID] [int] NOT NULL
               ,[CultureID] [nchar](6) NOT NULL
               ,[ModifiedDate] [datetime] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_ProductProductPhoto"] = f"""
        CREATE TABLE [{schema}].[ProductProductPhoto](
               [ProductID] [int] NOT NULL
               ,[ProductPhotoID] [int] NOT NULL
               ,[Primary] [bit] NOT NULL
               ,[ModifiedDate] [datetime] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_ProductReview"] = f"""
        CREATE TABLE [{schema}].[ProductReview](
               [ProductReviewID] [int] NOT NULL
               ,[ProductID] [int] NOT NULL
               ,[ReviewerName] [char](256) NOT NULL
               ,[ReviewDate] [datetime] NOT NULL
               ,[EmailAddress] [nvarchar](50) NOT NULL
               ,[Rating] [int] NOT NULL
               ,[Comments] [nvarchar](3850) NULL
               ,[ModifiedDate] [datetime] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_ProductSubcategory"] = f"""
        CREATE TABLE [{schema}].[ProductSubcategory](
               [ProductSubcategoryID] [int] NOT NULL
               ,[ProductCategoryID] [int] NOT NULL
               ,[Name] [char](256) NOT NULL
               ,[rowguid] [uniqueidentifier] NOT NULL
               ,[ModifiedDate] [datetime] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_ScrapReason"] = f"""
        CREATE TABLE [{schema}].[ScrapReason](
               [ScrapReasonID] [smallint] NOT NULL
               ,[Name] [char](256) NOT NULL
               ,[ModifiedDate] [datetime] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_TransactionHistory"] = f"""
        CREATE TABLE [{schema}].[TransactionHistory](
               [TransactionID] [int] NOT NULL
               ,[ProductID] [int] NOT NULL
               ,[ReferenceOrderID] [int] NOT NULL
               ,[ReferenceOrderLineID] [int] NOT NULL
               ,[TransactionDate] [datetime] NOT NULL
               ,[TransactionType] [nchar](1) NOT NULL
               ,[Quantity] [int] NOT NULL
               ,[ActualCost] [money] NOT NULL
               ,[ModifiedDate] [datetime] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_TransactionHistoryArchive"] = f"""
        CREATE TABLE [{schema}].[TransactionHistoryArchive](
               [TransactionID] [int] NOT NULL
               ,[ProductID] [int] NOT NULL
               ,[ReferenceOrderID] [int] NOT NULL
               ,[ReferenceOrderLineID] [int] NOT NULL
               ,[TransactionDate] [datetime] NOT NULL
               ,[TransactionType] [nchar](1) NOT NULL
               ,[Quantity] [int] NOT NULL
               ,[ActualCost] [money] NOT NULL
               ,[ModifiedDate] [datetime] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_UnitMeasure"] = f"""
        CREATE TABLE [{schema}].[UnitMeasure](
               [UnitMeasureCode] [nchar](3) NOT NULL
               ,[Name] [char](256) NOT NULL
               ,[ModifiedDate] [datetime] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_WorkOrder"] = f"""
        CREATE TABLE [{schema}].[WorkOrder](
               [WorkOrderID] [int] NOT NULL
               ,[ProductID] [int] NOT NULL
               ,[OrderQty] [int] NOT NULL
               ,[StockedQty] [int] NULL
               ,[ScrappedQty] [smallint] NOT NULL
               ,[StartDate] [datetime] NOT NULL
               ,[EndDate] [datetime] NULL
               ,[DueDate] [datetime] NOT NULL
               ,[ScrapReasonID] [smallint] NULL
               ,[ModifiedDate] [datetime] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_WorkOrderRouting"] = f"""
        CREATE TABLE [{schema}].[WorkOrderRouting](
               [WorkOrderID] [int] NOT NULL
               ,[ProductID] [int] NOT NULL
               ,[OperationSequence] [smallint] NOT NULL
               ,[LocationID] [smallint] NOT NULL
               ,[ScheduledStartDate] [datetime] NOT NULL
               ,[ScheduledEndDate] [datetime] NOT NULL
               ,[ActualStartDate] [datetime] NULL
               ,[ActualEndDate] [datetime] NULL
               ,[ActualResourceHrs] [decimal](9,4) NULL
               ,[PlannedCost] [money] NOT NULL
               ,[ActualCost] [money] NULL
               ,[ModifiedDate] [datetime] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    return definitions
