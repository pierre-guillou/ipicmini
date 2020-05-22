# pylint: disable=invalid-name, missing-docstring, import-error
from paraview import simple

# read every other persistence diagram
CinemaReader = simple.TTKCinemaReader(DatabasePath="data/pdiags.cdb")
CinemaFilter = simple.TTKCinemaQuery(InputTable=CinemaReader)
CinemaFilter.SQLStatement = """SELECT it.*, printf(
  "%s_%s_(%s-%s-%s)_%s",
  it.CaseName, it.ScalarField, it.B0x, it.B0y, it.B0z, it.ns
) AS Case_Field_B0_ns
FROM InputTable0 AS it
WHERE TimeStep % 2 = 0"""
ProductReader = simple.TTKCinemaProductReader(Input=CinemaFilter)

# get a distance matrix from these diagrams
DistMat = simple.TTKPersistenceDiagramDistanceMatrix(Input=ProductReader)
DistMat.NumberofPairs = 20

# reduce the distance matrix to 3D coordinates
DimRed = simple.TTKDimensionReduction(Input=DistMat)
DimRed.SelectFieldswithaRegexp = 1
DimRed.Regexp = "Diagram.*"
DimRed.Components = 3
DimRed.InputIsaDistanceMatrix = 1
DimRed.UseAllCores = 0

# generate points from 3D coordinates
t2p = simple.TableToPoints(Input=DimRed)
t2p.XColumn = "Component_0"
t2p.YColumn = "Component_1"
t2p.ZColumn = "Component_2"
t2p.KeepAllDataArrays = 1
tetra = simple.Tetrahedralize(Input=t2p)

# generate a heat map from distance matrix
# save output distance matrix, heat map and point cloud
simple.SaveData("data/distmat.csv", Input=DimRed)
simple.SaveData("data/distmat.vtu", simple.CleantoGrid(Input=tetra))
