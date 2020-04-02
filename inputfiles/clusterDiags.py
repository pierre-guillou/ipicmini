from paraview.simple import *

# read every other persistence diagram
CinemaReader = TTKCinemaReader(DatabasePath="data/pdiags.cdb")
CinemaFilter = TTKCinemaQuery(InputTable=CinemaReader)
CinemaFilter.SQLStatement = "SELECT * FROM InputTable0 WHERE TimeStep % 2 = 0"
ProductReader = TTKCinemaProductReader(Input=CinemaFilter)

# get a distance matrix from these diagrams
PDClustering = TTKPersistenceDiagramClustering(Input=ProductReader)
PDClustering.Numberofclusters = 3
PDClustering.Maximalcomputationtimes = 10.0
PDClustering.OutputaDistanceMatrix = 1

# find source
PDClustering_1 = FindSource("TTKPersistenceDiagramClustering1")

# reduce the distance matrix to 3D coordinates
DimRed = TTKDimensionReduction(
    Input=OutputPort(PDClustering_1, 3), ModulePath="default"
)
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

# save output distance matrix and point cloud
SaveData("data/distmat.csv", CleantoGrid(Input=DimRed))
SaveData("data/distmat.vtu", CleantoGrid(Input=tetra))
