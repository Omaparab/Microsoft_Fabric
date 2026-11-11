[StagingDefinition = [Kind = "FastCopy"]]
section Section1;
shared Raw_DataAdventureWorks_Product_Categories = let
  Source = Lakehouse.Contents([HierarchicalNavigation = null, EnableVorder = true, OutputMetadataRefresh = true]),
  #"Navigation 1" = Source{[workspaceId = "d4e907ea-42ae-48ec-80ab-9dc1c38bdd65"]}[Data],
  #"Navigation 2" = #"Navigation 1"{[lakehouseId = "d8a912bd-d31a-462e-9cfe-7de913517d57"]}[Data],
  #"Navigation 3" = #"Navigation 2"{[Id = "Files", ItemKind = "Folder"]}[Data],
  #"Navigation 4" = #"Navigation 3"{[Name = "Raw_DataAdventureWorks_Product_Categories"]}[Content],
  Navigation = #"Navigation 4"{[Name = "AdventureWorks_Product_Categories.csv"]}[Content],
  #"Imported CSV" = Csv.Document(Navigation, [Delimiter = ",", Columns = 2, QuoteStyle = QuoteStyle.None]),
  #"Promoted headers" = Table.PromoteHeaders(#"Imported CSV", [PromoteAllScalars = true]),
  #"Changed column type" = Table.TransformColumnTypes(#"Promoted headers", {{"ProductCategoryKey", Int64.Type}, {"CategoryName", type text}}),
  #"Lowercased text" = Table.TransformColumns(#"Changed column type", {{"CategoryName", each Text.Lower(_), type nullable text}}),
  #"Removed duplicates" = Table.Distinct(#"Lowercased text", {"ProductCategoryKey"})
in
  #"Removed duplicates";
shared Raw_DataProduct_Subcategories = let
  Source = Lakehouse.Contents(null),
  Navigation = Source{[workspaceId = "d4e907ea-42ae-48ec-80ab-9dc1c38bdd65"]}[Data],
  #"Navigation 1" = Navigation{[lakehouseId = "d8a912bd-d31a-462e-9cfe-7de913517d57"]}[Data],
  #"Navigation 2" = #"Navigation 1"{[Id = "Files", ItemKind = "Folder"]}[Data],
  #"Navigation 3" = #"Navigation 2"{[Name = "Raw_DataProduct_Subcategories"]}[Content],
  #"Navigation 4" = #"Navigation 3"{[Name = "AdventureWorks_Product_Subcategories.csv"]}[Content],
  #"Imported CSV" = Csv.Document(#"Navigation 4", [Delimiter = ",", Columns = 3, QuoteStyle = QuoteStyle.None]),
  #"Promoted headers" = Table.PromoteHeaders(#"Imported CSV", [PromoteAllScalars = true]),
  #"Changed column type" = Table.TransformColumnTypes(#"Promoted headers", {{"ProductSubcategoryKey", Int64.Type}, {"SubcategoryName", type text}, {"ProductCategoryKey", Int64.Type}}),
  #"Removed duplicates" = Table.Distinct(#"Changed column type", {"ProductSubcategoryKey"})
in
  #"Removed duplicates";
[DataDestinations = {[Definition = [Kind = "Reference", QueryName = "Merge_DataDestination", IsNewTarget = true], Settings = [Kind = "Automatic", TypeSettings = [Kind = "Table"]]]}]
shared Merge = let
  Source = Table.NestedJoin(Raw_DataProduct_Subcategories, {"ProductCategoryKey"}, Raw_DataAdventureWorks_Product_Categories, {"ProductCategoryKey"}, "Raw_DataAdventureWorks_Product_Categories", JoinKind.LeftOuter),
  #"Expanded Raw_DataAdventureWorks_Product_Categories" = Table.ExpandTableColumn(Source, "Raw_DataAdventureWorks_Product_Categories", {"ProductCategoryKey", "CategoryName"}, {"ProductCategoryKey.1", "CategoryName"}),
  #"Inserted conditional column" = Table.AddColumn(#"Expanded Raw_DataAdventureWorks_Product_Categories", "customflag", each if [ProductSubcategoryKey] = 1 then "One" else if [ProductSubcategoryKey] = 2 then "Two" else "Three")
in
  #"Inserted conditional column";
shared Merge_DataDestination = let
  Pattern = Lakehouse.Contents([HierarchicalNavigation = true, EnableVorder = true, OutputMetadataRefresh = true, CreateNavigationProperties = false, EnableFolding = false]),
  Navigation_1 = Pattern{[workspaceId = "d4e907ea-42ae-48ec-80ab-9dc1c38bdd65"]}[Data],
  Navigation_2 = Navigation_1{[lakehouseId = "d8a912bd-d31a-462e-9cfe-7de913517d57"]}[Data],
  Navigation_3 = Navigation_2{[Id = "dbo", ItemKind = "Schema"]}[Data],
  TableNavigation = Navigation_3{[Id = "Merge", ItemKind = "Table"]}?[Data]?
in
  TableNavigation;
