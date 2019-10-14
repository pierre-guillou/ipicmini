#ifndef FEADAPTOR_HEADER
#define FEADAPTOR_HEADER

// For iPic3D arrays
#include "../include/Alloc.h"

#include <string>

namespace Adaptor {
void Initialize(const char *script, const int start_x, const int start_y,
                const int start_z, const int nx, const int ny, const int nz,
                const double dx, const double dy, const double dz,
                std::string caseName);

void Finalize(const std::string &script = "");

void CoProcess(double time, unsigned int timeStep, arr3_double Bx,
               arr3_double By, arr3_double Bz);
} // namespace Adaptor

#endif
