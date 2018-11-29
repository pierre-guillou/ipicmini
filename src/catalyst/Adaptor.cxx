#include "Adaptor.h"

#include <iostream>

#include <vtkCPDataDescription.h>
#include <vtkCPInputDataDescription.h>
#include <vtkCPProcessor.h>
#include <vtkCPPythonScriptPipeline.h>
#include <vtkCellData.h>
#include <vtkCellType.h>
#include <vtkDoubleArray.h>
#include <vtkIntArray.h>
#include <vtkNew.h>
#include <vtkPointData.h>
#include <vtkPoints.h>
#include <vtkPolyData.h>

namespace
{
vtkCPProcessor* Processor = nullptr;
vtkPolyData* VTKGrid = nullptr;
const char* InputName = "particles";

//----------------------------------------------------------------------------
void BuildVTKGrid(const std::vector<double>& positions)
{
  // create the points information
  vtkNew<vtkDoubleArray> pointArray;
  pointArray->SetNumberOfComponents(3);
  pointArray->SetArray(
    const_cast<double*>(positions.data()), static_cast<vtkIdType>(positions.size()), 1);
  vtkNew<vtkPoints> points;
  points->SetData(pointArray);
  VTKGrid->SetPoints(points);

  // create the cells
  vtkIdType numCells = points->GetNumberOfPoints();
  VTKGrid->Allocate(numCells*2);
  for (vtkIdType cell = 0; cell < numCells; cell++)
  {
    VTKGrid->InsertNextCell(VTK_VERTEX, 1, &cell);
  }
}

//----------------------------------------------------------------------------
void UpdateVTKAttributes(const std::vector<double>& velocity, const std::vector<int>& collisions, vtkCPInputDataDescription* idd)
{
  if (idd->IsFieldNeeded("velocity", vtkDataObject::POINT) == true)
  {
    if (VTKGrid->GetPointData()->GetNumberOfArrays() == 0)
    {
      // velocity array
      vtkNew<vtkDoubleArray> velocityData;
      velocityData->SetName("velocity");
      velocityData->SetNumberOfComponents(3);
      velocityData->SetNumberOfTuples(static_cast<vtkIdType>(velocity.size() / 3));
      VTKGrid->GetPointData()->AddArray(velocityData);
    }
    vtkDoubleArray* velocityData =
      vtkDoubleArray::SafeDownCast(VTKGrid->GetPointData()->GetArray("velocity"));

    velocityData->SetArray(const_cast<double*>(velocity.data()), static_cast<vtkIdType>(velocity.size()), 1);
  }
  if (idd->IsFieldNeeded("collision", vtkDataObject::POINT) == true)
  {
    if (VTKGrid->GetPointData()->GetArray("collision") == nullptr)
    {
      // velocity array
      vtkNew<vtkIntArray> collisionData;
      collisionData->SetName("collision");
      collisionData->SetNumberOfComponents(1);
      collisionData->SetNumberOfTuples(static_cast<vtkIdType>(collisions.size()));
      VTKGrid->GetPointData()->AddArray(collisionData);
    }
    vtkIntArray* collisionData =
      vtkIntArray::SafeDownCast(VTKGrid->GetPointData()->GetArray("collision"));

    collisionData->SetArray(const_cast<int*>(collisions.data()), static_cast<vtkIdType>(collisions.size()), 1);
  }
}

//----------------------------------------------------------------------------
void BuildVTKDataStructures(const std::vector<double>& pos, const std::vector<double>& velocity, const std::vector<int>& collisions, vtkCPInputDataDescription* idd)
{
  if (VTKGrid == NULL)
  {
    // The grid structure isn't changing so we only build it
    // the first time it's needed. If we needed the memory
    // we could delete it and rebuild as necessary.
    VTKGrid = vtkPolyData::New();
  }
    BuildVTKGrid(pos);

  UpdateVTKAttributes(velocity, collisions, idd);
}
}

namespace Adaptor
{

//----------------------------------------------------------------------------
void Initialize(char* script)
{
  if (Processor == NULL)
  {
    Processor = vtkCPProcessor::New();
    Processor->Initialize();
  }
  else
  {
    Processor->RemoveAllPipelines();
  }
  vtkNew<vtkCPPythonScriptPipeline> pipeline;
  pipeline->Initialize(script);
  Processor->AddPipeline(pipeline);
}

//----------------------------------------------------------------------------
void Finalize()
{
  if (Processor)
  {
    Processor->Delete();
    Processor = NULL;
  }
  if (VTKGrid)
  {
    VTKGrid->Delete();
    VTKGrid = NULL;
  }
}

//----------------------------------------------------------------------------
void CoProcess(
  const std::vector<double>& pos, const std::vector<double>& velocity, const std::vector<int>& collisions, double time, unsigned int timeStep)
{
  vtkNew<vtkCPDataDescription> dataDescription;
  dataDescription->AddInput(InputName);
  dataDescription->SetTimeData(time, timeStep);

  if (Processor->RequestDataDescription(dataDescription) != 0)
  {
    vtkCPInputDataDescription* idd = dataDescription->GetInputDescriptionByName(InputName);
    BuildVTKDataStructures(pos, velocity, collisions, idd);
    idd->SetGrid(VTKGrid);
    Processor->CoProcess(dataDescription);
  }
}
} // end of Catalyst namespace

