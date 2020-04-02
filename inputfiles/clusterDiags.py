from paraview.simple import *

# read every other persistence diagram
CinemaReader = TTKCinemaReader(DatabasePath="data/pdiags.cdb")
CinemaFilter = TTKCinemaQuery(InputTable=CinemaReader)
CinemaFilter.SQLStatement = "SELECT * FROM InputTable0 WHERE TimeStep % 2 = 0"
ProductReader = TTKCinemaProductReader(Input=CinemaFilter)

# get a distance matrix from these diagrams
DistMat = TTKPersistenceDiagramDistanceMatrix(Input=ProductReader)
DistMat.NumberofPairs = 20

# reduce the distance matrix to 3D coordinates
DimRed = TTKDimensionReduction(Input=DistMat)
DimRed.SelectFieldswithaRegexp = 1
DimRed.Regexp = "Diagram.*"
DimRed.Components = 3
DimRed.InputIsaDistanceMatrix = 1
DimRed.UseAllCores = 0

# generate points from 3D coordinates
t2p = TableToPoints(Input=DimRed)
t2p.XColumn = "Component_0"
t2p.YColumn = "Component_1"
t2p.ZColumn = "Component_2"
t2p.KeepAllDataArrays = 1
tetra = Tetrahedralize(Input=t2p)

# generate a heat map from distance matrix
hm = TTKMatrixToHeatMap(Input=DistMat)
hm.SelectFieldswithaRegexp = 1
hm.Regexp = "Diagram.*"

# save output distance matrix, heat map and point cloud
SaveData("data/distmat.csv", Input=DimRed)
SaveData("data/heatmap.vtu", CleantoGrid(Input=hm))
SaveData("data/distmat.vtu", CleantoGrid(Input=tetra))
