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

    definitions[f"{schema}_Department"] = f"""
        CREATE TABLE [{schema}].[Department](
               [DepartmentID] [SMALLINT] NOT NULL
               ,[Name] [VARCHAR](256) NOT NULL
               ,[GroupName] [VARCHAR](256) NOT NULL
               ,[ModifiedDate] [DATETIME] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
        );"""

    definitions[f"{schema}_Employee"] = f"""
        CREATE TABLE [{schema}].[Employee](
               [BusinessEntityID] [INT] NOT NULL
               ,[NationalIDNumber] [NVARCHAR](15) NOT NULL
               ,[LoginID] [NVARCHAR](256) NOT NULL
               ,[OrganizationNode] [HIERARCHYID] NULL
               ,[OrganizationLevel] [SMALLINT] NULL
               ,[JobTitle] [NVARCHAR](50) NOT NULL
               ,[BirthDate] [DATE] NOT NULL
               ,[MaritalStatus] [NCHAR](1) NOT NULL
               ,[Gender] [NCHAR](1) NOT NULL
               ,[HireDate] [DATE] NOT NULL
               ,[SalariedFlag] [BIT] NOT NULL
               ,[VacationHours] [SMALLINT] NOT NULL
               ,[SickLeaveHours] [SMALLINT] NOT NULL
               ,[CurrentFlag] [BIT] NOT NULL
               ,[rowguid] [UNIQUEIDENTIFIER] NOT NULL
               ,[ModifiedDate] [DATETIME] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
        );"""

    definitions[f"{schema}_EmployeeDepartmentHistory"] = f"""
        CREATE TABLE [{schema}].[EmployeeDepartmentHistory](
               [BusinessEntityID] [INT] NOT NULL
               ,[DepartmentID] [SMALLINT] NOT NULL
               ,[ShiftID] [TINYINT] NOT NULL
               ,[StartDate] [DATE] NOT NULL
               ,[EndDate] [DATE] NULL
               ,[ModifiedDate] [DATETIME] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
        );"""

    definitions[f"{schema}_EmployeePayHistory"] = f"""
        CREATE TABLE [{schema}].[EmployeePayHistory](
               [BusinessEntityID] [INT] NOT NULL
               ,[RateChangeDate] [DATETIME] NOT NULL
               ,[Rate] [MONEY] NOT NULL
               ,[PayFrequency] [TINYINT] NOT NULL
               ,[ModifiedDate] [DATETIME] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
        );"""

    definitions[f"{schema}_JobCandidate"] = f"""
        CREATE TABLE [{schema}].[JobCandidate](
               [JobCandidateID] [INT] NOT NULL
               ,[BusinessEntityID] [INT] NULL
               ,[Resume] [XML] NULL
               ,[ModifiedDate] [DATETIME] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
        );"""

    definitions[f"{schema}_Shift"] = f"""
        CREATE TABLE [{schema}].[Shift](
               [ShiftID] [TINYINT] NOT NULL
               ,[Name] [CHAR](7) NOT NULL
               ,[StartTime] [TIME] NOT NULL
               ,[EndTime] [TIME] NOT NULL
               ,[ModifiedDate] [DATETIME] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
        );"""

    return definitions
