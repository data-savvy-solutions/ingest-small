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

    definitions[f"{schema}_ProductVendor"] = f"""
        CREATE TABLE [{schema}].[ProductVendor](
               [ProductID] [int] NOT NULL
               ,[BusinessEntityID] [int] NOT NULL
               ,[AverageLeadTime] [int] NOT NULL
               ,[StandardPrice] [money] NOT NULL
               ,[LastReceiptCost] [money] NULL
               ,[LastReceiptDate] [datetime] NULL
               ,[MinOrderQty] [int] NOT NULL
               ,[MaxOrderQty] [int] NOT NULL
               ,[OnOrderQty] [int] NULL
               ,[UnitMeasureCode] [nchar](3) NOT NULL
               ,[ModifiedDate] [datetime] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_PurchaseOrderDetail"] = f"""
        CREATE TABLE [{schema}].[PurchaseOrderDetail](
               [PurchaseOrderID] [int] NOT NULL
               ,[PurchaseOrderDetailID] [int] NOT NULL
               ,[DueDate] [datetime] NOT NULL
               ,[OrderQty] [smallint] NOT NULL
               ,[ProductID] [int] NOT NULL
               ,[UnitPrice] [money] NOT NULL
               ,[LineTotal] [money] NOT NULL
               ,[ReceivedQty] [decimal](8,2) NOT NULL
               ,[RejectedQty] [decimal](8,2) NOT NULL
               ,[StockedQty] [decimal](8,2) NOT NULL
               ,[ModifiedDate] [datetime] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_PurchaseOrderHeader"] = f"""
        CREATE TABLE [{schema}].[PurchaseOrderHeader](
               [PurchaseOrderID] [int] NOT NULL
               ,[RevisionNumber] [tinyint] NOT NULL
               ,[Status] [tinyint] NOT NULL
               ,[EmployeeID] [int] NOT NULL
               ,[VendorID] [int] NOT NULL
               ,[ShipMethodID] [int] NOT NULL
               ,[OrderDate] [datetime] NOT NULL
               ,[ShipDate] [datetime] NULL
               ,[SubTotal] [money] NOT NULL
               ,[TaxAmt] [money] NOT NULL
               ,[Freight] [money] NOT NULL
               ,[TotalDue] [money] NOT NULL
               ,[ModifiedDate] [datetime] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_ShipMethod"] = f"""
        CREATE TABLE [{schema}].[ShipMethod](
               [ShipMethodID] [int] NOT NULL
               ,[Name] [CHAR](256) NOT NULL
               ,[ShipBase] [money] NOT NULL
               ,[ShipRate] [money] NOT NULL
               ,[rowguid] [uniqueidentifier] NOT NULL
               ,[ModifiedDate] [datetime] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_Vendor"] = f"""
        CREATE TABLE [{schema}].[Vendor](
               [BusinessEntityID] [int] NOT NULL
               ,[AccountNumber] [CHAR](256) NOT NULL
               ,[Name] [CHAR](256) NOT NULL
               ,[CreditRating] [tinyint] NOT NULL
               ,[PreferredVendorStatus] [BIT] NOT NULL
               ,[ActiveFlag] [BIT] NOT NULL
               ,[PurchasingWebServiceURL] [nvarchar](1024) NULL
               ,[ModifiedDate] [datetime] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    return definitions
