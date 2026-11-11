CREATE VIEW [gold].[ss] AS select [_].[OrderDate] as [OrderDate],
    [_].[StockDate] as [StockDate],
    lower([_].[OrderNumber]) as [OrderNumber],
    [_].[ProductKey] as [ProductKey],
    [_].[CustomerKey] as [CustomerKey],
    [_].[TerritoryKey] as [TerritoryKey],
    [_].[OrderLineItem] as [OrderLineItem],
    [_].[OrderQuantity] as [OrderQuantity]
from [Warehouse1].[gold].[fact_sales] as [_]

GO