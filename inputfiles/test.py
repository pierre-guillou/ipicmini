
#--------------------------------------------------------------

# Global timestep output options
timeStepToStartOutputAt=0
forceOutputAtFirstCall=False

# Global screenshot output options
imageFileNamePadding=0
rescale_lookuptable=False

# Whether or not to request specific arrays from the adaptor.
requestSpecificArrays=False

# a root directory under which all Catalyst output goes
rootDirectory=''

# makes a cinema D index table
make_cinema_table=False

#--------------------------------------------------------------
# Code generated from cpstate.py to create the CoProcessor.
# paraview version 5.6.0
#--------------------------------------------------------------

from paraview.simple import *
from paraview import coprocessing

# --------------------------------------------------------------
# The following loads TTK's plugins.
# Topology Toolkit 0.9.7
# --------------------------------------------------------------
import glob
import os
from os.path import join as ttk_path_join

ttk_plugins_path = "/usr/local/lib/plugins/"
for x in glob.glob(
    ttk_path_join(ttk_plugins_path, "*.so" if os.name == "posix" else "*.dll")
):
    LoadPlugin(x, ns=globals())

# ----------------------- CoProcessor definition -----------------------

def CreateCoProcessor():
  def _CreatePipeline(coprocessor, datadescription):
    class Pipeline:
      # state file generated using paraview version 5.6.0

      # ----------------------------------------------------------------
      # setup the data processing pipelines
      # ----------------------------------------------------------------

      # trace generated using paraview version 5.6.0
      #
      # To ensure correct image size when batch processing, please search 
      # for and uncomment the line `# renderView*.ViewSize = [*,*]`

      #### disable automatic camera reset on 'Show'
      paraview.simple._DisableFirstRenderCameraReset()

      # create a new 'Legacy VTK Reader'
      # create a producer from a simulation input
      taylorGreen_B_0vtk = coprocessor.CreateProducer(datadescription, 'particles')

      # create a new 'Calculator'
      calculator1 = Calculator(Input=taylorGreen_B_0vtk)
      calculator1.Function = 'mag(B)'

      # create a new 'TTK ScalarFieldNormalizer'
      tTKScalarFieldNormalizer1 = TTKScalarFieldNormalizer(Input=calculator1)
      tTKScalarFieldNormalizer1.ScalarField = 'Result'

      # create a new 'TTK PersistenceDiagram'
      tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=tTKScalarFieldNormalizer1)
      tTKPersistenceDiagram1.ScalarField = 'Result'
      tTKPersistenceDiagram1.InputOffsetField = 'Result'
      tTKPersistenceDiagram1.EmbedinDomain = 0

      # create a new 'TTK CinemaWriter'
      tTKCinemaWriter1 = TTKCinemaWriter(Input=tTKPersistenceDiagram1,
          DatabasePath='data/cinema.cdb')
      tTKCinemaWriter1.OverrideDatabase = 0

      # create a new 'Parallel PolyData Writer'
      parallelPolyDataWriter1 = servermanager.writers.XMLPPolyDataWriter(Input=tTKCinemaWriter1)

      # register the writer with coprocessor
      # and provide it with information such as the filename to use,
      # how frequently to write the data, etc.
      coprocessor.RegisterWriter(parallelPolyDataWriter1, filename='data/catalyst/ph_%t.pvtp', freq=1, paddingamount=0)

      # create a new 'Threshold'
      threshold1 = Threshold(Input=tTKPersistenceDiagram1)
      threshold1.Scalars = ['CELLS', 'Persistence']
      threshold1.ThresholdRange = [0.01, 0.9999999999999999]

      # create a new 'TTK TopologicalSimplification'
      tTKTopologicalSimplification1 = TTKTopologicalSimplification(Domain=tTKScalarFieldNormalizer1,
          Constraints=threshold1)
      tTKTopologicalSimplification1.ScalarField = 'Result'
      tTKTopologicalSimplification1.InputOffsetField = 'Result'
      tTKTopologicalSimplification1.Vertexidentifierfield = 'Birth'
      tTKTopologicalSimplification1.OutputOffsetScalarField = ''

      # create a new 'TTK ScalarFieldCriticalPoints'
      tTKScalarFieldCriticalPoints1 = TTKScalarFieldCriticalPoints(Input=tTKTopologicalSimplification1)
      tTKScalarFieldCriticalPoints1.ScalarField = 'Result'
      tTKScalarFieldCriticalPoints1.InputOffsetfield = 'Result'

      # create a new 'Parallel UnstructuredGrid Writer'
      parallelUnstructuredGridWriter1 = servermanager.writers.XMLPUnstructuredGridWriter(Input=tTKScalarFieldCriticalPoints1)

      # register the writer with coprocessor
      # and provide it with information such as the filename to use,
      # how frequently to write the data, etc.
      coprocessor.RegisterWriter(parallelUnstructuredGridWriter1, filename='data/catalyst/critPoints_%t.pvtu', freq=10, paddingamount=0)

      # create a new 'Parallel Image Data Writer'
      parallelImageDataWriter1 = servermanager.writers.XMLPImageDataWriter(Input=taylorGreen_B_0vtk)

      # register the writer with coprocessor
      # and provide it with information such as the filename to use,
      # how frequently to write the data, etc.
      coprocessor.RegisterWriter(parallelImageDataWriter1, filename='data/catalyst/sim_%t.pvti', freq=100, paddingamount=0)

      # ----------------------------------------------------------------
      # finally, restore active source
      SetActiveSource(parallelPolyDataWriter1)
      # ----------------------------------------------------------------
    return Pipeline()

  class CoProcessor(coprocessing.CoProcessor):
    def CreatePipeline(self, datadescription):
      self.Pipeline = _CreatePipeline(self, datadescription)

  coprocessor = CoProcessor()
  # these are the frequencies at which the coprocessor updates.
  freqs = {'particles': [1, 10, 100]}
  coprocessor.SetUpdateFrequencies(freqs)
  if requestSpecificArrays:
    arrays = []
    coprocessor.SetRequestedArrays('particles', arrays)
  coprocessor.SetInitialOutputOptions(timeStepToStartOutputAt,forceOutputAtFirstCall)

  if rootDirectory:
      coprocessor.SetRootDirectory(rootDirectory)

  if make_cinema_table:
      coprocessor.EnableCinemaDTable()

  return coprocessor


#--------------------------------------------------------------
# Global variable that will hold the pipeline for each timestep
# Creating the CoProcessor object, doesn't actually create the ParaView pipeline.
# It will be automatically setup when coprocessor.UpdateProducers() is called the
# first time.
coprocessor = CreateCoProcessor()

#--------------------------------------------------------------
# Enable Live-Visualizaton with ParaView and the update frequency
coprocessor.EnableLiveVisualization(True, 1)

# ---------------------- Data Selection method ----------------------

def RequestDataDescription(datadescription):
    "Callback to populate the request for current timestep"
    global coprocessor

    # setup requests for all inputs based on the requirements of the
    # pipeline.
    coprocessor.LoadRequestedData(datadescription)

# ------------------------ Processing method ------------------------

def DoCoProcessing(datadescription):
    "Callback to do co-processing for current timestep"
    global coprocessor

    # Update the coprocessor by providing it the newly generated simulation data.
    # If the pipeline hasn't been setup yet, this will setup the pipeline.
    coprocessor.UpdateProducers(datadescription)

    # Write output data, if appropriate.
    coprocessor.WriteData(datadescription);

    # Write image capture (Last arg: rescale lookup table), if appropriate.
    coprocessor.WriteImages(datadescription, rescale_lookuptable=rescale_lookuptable,
        image_quality=0, padding_amount=imageFileNamePadding)

    # Live Visualization, if enabled.
    coprocessor.DoLiveVisualization(datadescription, "localhost", 22222)
